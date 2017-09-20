#include <ecto/ecto.hpp>
#include <boost/python.hpp>
#include "camera.hpp"

ECTO_DEFINE_MODULE(camera)
{

	boost::python::class_<qidata::Transform>("QiDataTransform")
		.def_readwrite("tx", &qidata::Transform::tx)
		.def_readwrite("ty", &qidata::Transform::ty)
		.def_readwrite("tz", &qidata::Transform::tz)
		.def_readwrite("rx", &qidata::Transform::rx)
		.def_readwrite("ry", &qidata::Transform::ry)
		.def_readwrite("rz", &qidata::Transform::rz)
		.def_readwrite("rw", &qidata::Transform::rw);

	boost::python::class_<qidata::Timestamp>("QiDataTimestamp")
		.def_readwrite("seconds", &qidata::Timestamp::seconds)
		.def_readwrite("nanoseconds", &qidata::Timestamp::nanoseconds);

	boost::python::class_<qidata::Camera>("QiDataCamera")
		.def_readwrite("image", &qidata::Camera::image)
		.def_readwrite("tf", &qidata::Camera::tf)
		.def_readwrite("ts", &qidata::Camera::ts);
}
