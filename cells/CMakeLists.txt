ectomodule(qidata_cells DESTINATION ecto_qidata INSTALL
    module.cpp
)
link_ecto(qidata_cells
  OPENCV3_CORE
  OPENCV3_IMGPROC
)
