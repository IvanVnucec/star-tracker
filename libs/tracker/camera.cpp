#include <tracker/camera.hpp>
#include <Eigen/Dense>

using Eigen::MatrixXd;

Camera::Camera() :
m_ccd{ MatrixXd::Zero(m_pixel_w, m_pixel_h) }
{
}

void Camera::capture(const std::vector<Star>& stars)
{
    // TODO
    m_ccd = MatrixXd::Zero(m_pixel_w, m_pixel_h);
}

CameraCCD Camera::get_ccd()
{
    return m_ccd;
}

