# Copyright (c) 2017, Softbank Robotics Europe
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.

# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Third-party libraries
import cv2
import ecto
from ecto_opencv import cv_bp # not directly used, by it imports all cv bindings
from image import Colorspace
import numpy
import qidata

# Local modules
from .camera import QiDataImage

class imread(ecto.Cell):
	def declare_params(self,p):
		p.declare("mode", "Opening mode for the image", "UNCHANGED")
		p.declare("image_file","Path to image file", "")
		return

	def declare_io(self, p, i, o):
		o.declare("qidata_image", "QiDataImage", QiDataImage())
		return

	def process(self, i, o):
		cam = QiDataImage()
		with qidata.open(self.params.get("image_file").get()) as _f:
			# Retrieve image, convert it if necessary, then put it in a Cv::Mat
			# and in QiDataImage
			if ("COLOR" == self.params.get("mode").get() and Colorspace("BGR") != _f.raw_data.colorspace):
				# convert
				_tmp = _f.raw_data.render().numpy_image
				colorspace = 13 # AL_code for BGR
			elif ("GRAYSCALE" == self.params.get("mode").get() and Colorspace("Gray") != _f.raw_data.colorspace):
				_tmp = _f.raw_data.render().numpy_image
				_tmp = cv2.cvtColor(_tmp, cv2.COLOR_BGR2GRAY)
				colorspace = 0 # AL_code for Gray
			else:
				# no convert
				_tmp = _f.raw_data.numpy_image
				colorspace = _f.raw_data.colorspace.al_code
			cam.data.fromarray(_tmp)
			cam.colorspace = colorspace

			# Register the camera's position
			cam.tf.tx = _f.transform.translation.x
			cam.tf.ty = _f.transform.translation.y
			cam.tf.tz = _f.transform.translation.z
			cam.tf.rx = _f.transform.rotation.x
			cam.tf.ry = _f.transform.rotation.y
			cam.tf.rz = _f.transform.rotation.z
			cam.tf.rw = _f.transform.rotation.w

			# Register the image's timestamp
			cam.ts.seconds = _f.timestamp.seconds
			cam.ts.nanoseconds = _f.timestamp.nanoseconds

			# Register the calibration
			cam.camera_matrix.fromarray(numpy.array(_f.raw_data.camera_info.camera_matrix))
			cam.distortion_coeffs = ecto.list_of_floats(_f.raw_data.camera_info.distortion_coeffs)
			cam.rectification_matrix.fromarray(numpy.array(_f.raw_data.camera_info.rectification_matrix))
			cam.projection_matrix.fromarray(numpy.array(_f.raw_data.camera_info.projection_matrix))

		o.get("qidata_image").set(cam)
		return ecto.OK

class imread_stereo(ecto.Cell):
	def declare_params(self,p):
		p.declare("mode", "Opening mode for the image", "UNCHANGED")
		p.declare("image_file","Path to image file", "")
		return

	def declare_io(self, p, i, o):
		o.declare("qidata_image_main", "QiDataImage", QiDataImage())
		o.declare("qidata_image_secondary", "QiDataImage", QiDataImage())
		return

	def process(self, i, o):
		cams = []
		cam1 = QiDataImage()
		cam2 = QiDataImage()
		with qidata.open(self.params.get("image_file").get()) as _f:
			# Retrieve image, convert it if necessary, then put it in a Cv::Mat
			# and in QiDataImage
			images = []
			if hasattr(_f.raw_data, "left_image"):
				images.append(_f.raw_data.left_image)
				images.append(_f.raw_data.right_image)
			elif hasattr(_f.raw_data, "top_image"):
				images.append(_f.raw_data.top_image)
				images.append(_f.raw_data.bottom_image)
			else:
				raise RuntimeError("Given image is not stereo")

			for img in images:
				cam = QiDataImage()

				if ("COLOR" == self.params.get("mode").get() and Colorspace("BGR") != _f.raw_data.colorspace):
					# convert
					_tmp = img.render().numpy_image
					colorspace = 13 # AL_code for BGR

				elif ("GRAYSCALE" == self.params.get("mode").get() and Colorspace("Gray") != _f.raw_data.colorspace):
					_tmp = img.render().numpy_image
					_tmp = cv2.cvtColor(_tmp, cv2.COLOR_BGR2GRAY)
					colorspace = 0 # AL_code for Gray
				else:
					# no convert
					_tmp = img.numpy_image
					colorspace = _f.raw_data.colorspace.al_code
				cam.data.fromarray(_tmp)
				cam.colorspace = colorspace

				# Register the camera's position
				cam.tf.tx = _f.transform.translation.x
				cam.tf.ty = _f.transform.translation.y
				cam.tf.tz = _f.transform.translation.z
				cam.tf.rx = _f.transform.rotation.x
				cam.tf.ry = _f.transform.rotation.y
				cam.tf.rz = _f.transform.rotation.z
				cam.tf.rw = _f.transform.rotation.w

				# Register the image's timestamp
				cam.ts.seconds = _f.timestamp.seconds
				cam.ts.nanoseconds = _f.timestamp.nanoseconds

				# Register the calibration
				cam.camera_matrix.fromarray(numpy.array(img.camera_info.camera_matrix))
				cam.distortion_coeffs = ecto.list_of_floats(img.camera_info.distortion_coeffs)
				cam.rectification_matrix.fromarray(numpy.array(img.camera_info.rectification_matrix))
				cam.projection_matrix.fromarray(numpy.array(img.camera_info.projection_matrix))

				cams.append(cam)

		o.get("qidata_image_main").set(cams[0])
		o.get("qidata_image_secondary").set(cams[1])
		return ecto.OK
