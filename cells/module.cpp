// Copyright (c) 2017, Softbank Robotics Europe
// All rights reserved.

// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:

// * Redistributions of source code must retain the above copyright notice, this
//   list of conditions and the following disclaimer.

// * Redistributions in binary form must reproduce the above copyright notice,
//   this list of conditions and the following disclaimer in the documentation
//   and/or other materials provided with the distribution.

// * Neither the name of the copyright holder nor the names of its
//   contributors may be used to endorse or promote products derived from
//   this software without specific prior written permission.

// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
// FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
// DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
// SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
// CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
// OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

	boost::python::class_<qidata::Image>("QiDataImage")
		.def_readwrite("data", &qidata::Image::data)
		.def_readwrite("tf", &qidata::Image::tf)
		.def_readwrite("ts", &qidata::Image::ts)
		.def_readwrite("colorspace", &qidata::Image::colorspace)
		.def_readwrite("camera_matrix", &qidata::Image::camera_matrix)
		.def_readwrite("distortion_coeffs", &qidata::Image::distortion_coeffs)
		.def_readwrite("rectification_matrix", &qidata::Image::rectification_matrix)
		.def_readwrite("projection_matrix", &qidata::Image::projection_matrix);
}
