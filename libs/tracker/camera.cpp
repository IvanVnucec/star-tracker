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

CameraCCD Camera::ccd() const
{
    return m_ccd;
}

unsigned Camera::pixel_w() const
{
    return m_pixel_w;
}
unsigned Camera::pixel_h() const
{
    return m_pixel_h;
}
