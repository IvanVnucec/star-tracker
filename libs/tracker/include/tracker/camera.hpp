#pragma once

#include <vector>
#include <tracker/star.hpp>
#include <Eigen/Dense>

using CameraCCD = Eigen::MatrixXd;

class Camera {
private:
    static constexpr unsigned m_pixel_w = 400;
    static constexpr unsigned m_pixel_h = 400;
    static constexpr unsigned m_cx = m_pixel_w / 2;
    static constexpr unsigned m_cy = m_pixel_h / 2;
    static constexpr unsigned m_f = 1000; // px/m
    static constexpr double m_fov = 70.0; // deg
    Eigen::Matrix<double, 3, 4> m_proj_matrix;
    CameraCCD m_ccd;
    std::vector<Star> world_to_camera_coords(const Orientation& ori, const std::vector<Star>& stars);
    std::vector<Star> get_stars_in_fov(const Orientation& ori, const std::vector<Star>& stars);

public:
    Camera();
    void capture(const Orientation& ori, const std::vector<Star>& stars);
    CameraCCD ccd() const;
    unsigned pixel_w() const;
    unsigned pixel_h() const;
};
