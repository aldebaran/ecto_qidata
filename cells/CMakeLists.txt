
# Bind "Camera" struct in Python via ecto
ectomodule(camera DESTINATION ecto_qidata INSTALL
  camera.hpp
  module.cpp
)
link_ecto(camera
  OPENCV3_CORE
  OPENCV3_IMGPROC
)

# Create a separate library that will be staged so that it can be imported
# by other cells projects
qi_create_lib(ecto_qidata
  camera.hpp
  SHARED
)

# As there is no source for now, linker needs a hint to guess the language
set_target_properties(ecto_qidata PROPERTIES LINKER_LANGUAGE CXX)

qi_use_lib(ecto_qidata
  OPENCV3_CORE
  OPENCV3_IMGPROC
)

qi_stage_lib(ecto_qidata)

qi_install_header(
  camera.hpp
  SUBFOLDER ecto_qidata
)