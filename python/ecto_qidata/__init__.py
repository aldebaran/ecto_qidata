
def makeQiDataCamera(filename):
	from ecto_qidata.camera import QiDataCamera
	from ecto_opencv import cv_bp
	import qidata

	c = cv_bp.Mat()
	cam = QiDataCamera()

	with qidata.open(filename) as _f:
		_tmp  = _f.raw_data.numpy_image

		fh3 = _f.raw_data.camera_info.camera_matrix[0]
		fv3 = _f.raw_data.camera_info.camera_matrix[0]
		c.fromarray(_tmp)
		cam.image = c

		cam.tf.tx = _f.transform.translation.x
		cam.tf.ty = _f.transform.translation.y
		cam.tf.tz = _f.transform.translation.z
		cam.tf.rx = _f.transform.rotation.x
		cam.tf.ry = _f.transform.rotation.y
		cam.tf.rz = _f.transform.rotation.z
		cam.tf.rw = _f.transform.rotation.w
		cam.ts.seconds = _f.timestamp.seconds
		cam.ts.nanoseconds = _f.timestamp.nanoseconds

	return cam