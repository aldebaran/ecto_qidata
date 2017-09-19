#include <ecto/ecto.hpp>
#include <boost/python.hpp>
#include "camera.hpp"

ECTO_DEFINE_MODULE(qidata_cells)
{

	boost::python::class_<qidata_cells::Transform>("QIDATA_Transform")
		.def_readwrite("tx", &qidata_cells::Transform::tx)
		.def_readwrite("ty", &qidata_cells::Transform::ty)
		.def_readwrite("tz", &qidata_cells::Transform::tz)
		.def_readwrite("rx", &qidata_cells::Transform::rx)
		.def_readwrite("ry", &qidata_cells::Transform::ry)
		.def_readwrite("rz", &qidata_cells::Transform::rz)
		.def_readwrite("rw", &qidata_cells::Transform::rw);

	boost::python::class_<qidata_cells::Timestamp>("QIDATA_Timestamp")
		.def_readwrite("seconds", &qidata_cells::Timestamp::seconds)
		.def_readwrite("nanoseconds", &qidata_cells::Timestamp::nanoseconds);

	boost::python::class_<qidata_cells::Camera>("QIDATA_Camera")
		.def_readwrite("image", &qidata_cells::Camera::image)
		.def_readwrite("tf", &qidata_cells::Camera::tf)
		.def_readwrite("ts", &qidata_cells::Camera::ts);
}
