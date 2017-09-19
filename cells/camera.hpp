#include <opencv2/core.hpp>

namespace qidata_cells
{

  struct Timestamp
  {
    int seconds;
    int nanoseconds;
  };

  struct Transform
  {
    float tx;
    float ty;
    float tz;
    float rx;
    float ry;
    float rz;
    float rw;
  };

  struct Camera
  {
    cv::Mat image;
    Transform tf;
    Timestamp ts;
  };
}