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
    int colorspace;
    cv::Mat camera_matrix;
    std::vector<float> distortion_coeffs;
    cv::Mat rectification_matrix;
    cv::Mat projection_matrix;
  };
}