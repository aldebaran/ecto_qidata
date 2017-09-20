cmake_minimum_required(VERSION 2.8)
project(ecto_qidata)

find_package(qibuild REQUIRED)
find_package(ecto REQUIRED)
include(${ecto_DIR}/../share/cmake/ectoMacros.cmake OPTIONAL)

add_subdirectory(cells)
