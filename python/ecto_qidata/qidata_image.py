
# Third-party libraries
import cv2
import ecto
from ecto_opencv import cv_bp
from image import Colorspace
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
		c = cv_bp.Mat()
		cam = QiDataImage()
		with qidata.open(self.params.get("image_file").get()) as _f:
			# Retrieve image, convert it if necessary, then put it in a Cv::Mat
			# and in QiDataImage
			_tmp  = _f.raw_data.numpy_image
			if ("COLOR" == self.params.get("mode").get() and Colorspace("BGR") != _f.raw_data.colorspace):
				# convert
				_tmp = _f.raw_data.render().numpy_image
			elif ("GRAY" == self.params.get("mode").get() and Colorspace("Gray") != _f.raw_data.colorspace):
				_tmp = _f.raw_data.render().numpy_image
				_tmp = cv2.cvtColor(_tmp, cv2.COLOR_BGR2GRAY)
			else:
				# no convert
				_tmp = _f.raw_data.numpy_image
			c.fromarray(_tmp)
			cam.data = c

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

			# Future: Register camera's calibration
			# fh3 = _f.raw_data.camera_info.camera_matrix[0]
			# fv3 = _f.raw_data.camera_info.camera_matrix[0]

		o.get("qidata_image").set(cam)
		return ecto.OK
