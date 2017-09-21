#pragma once
#include <opencv2/core.hpp>

namespace qidata
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

  struct Image
  {
    cv::Mat data;
    Transform tf;
    Timestamp ts;
  };
}