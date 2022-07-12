#pragma once

#include <vector>
#include <tracker/star.hpp>
#include <Eigen/Dense>

using CameraCCD = Eigen::MatrixXd;

class Camera {
private:
    static const unsigned m_pixel_w = 400;
    static const unsigned m_pixel_h = 400;
    CameraCCD m_ccd;

public:
    Camera();
    void capture(const std::vector<Star>& stars);
    CameraCCD get_ccd();
};
