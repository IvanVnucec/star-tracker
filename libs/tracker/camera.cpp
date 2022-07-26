#include <tracker/camera.hpp>
#include <Eigen/Dense>
#include <tracker/utils.hpp>
#include <cmath>
#include <iostream>

using Eigen::MatrixXd;

Camera::Camera() :
m_proj_matrix{ (Eigen::Matrix<double, 3, 4>() << m_f, 0, m_cx, 0,  0, m_f, m_cy, 0,  0, 0, 1, 0).finished() },
m_ccd{ MatrixXd::Zero(m_pixel_w, m_pixel_h) }
{
}

std::vector<Star> Camera::world_to_camera_coords(const Orientation& ori, const std::vector<Star>& stars)
{
    std::vector<Star> stars_in_camera_coords = stars;

    // https://math.stackexchange.com/a/476311/922153
    XYZ a = Orientation(RaDec(0.0, 0.0)).xyz();
    XYZ b = ori.xyz();

    Eigen::Vector3d v = a.cross(b);
    double s = v.norm();
    double c = a.dot(b);

    Eigen::Matrix3d v_x;
    v_x << 0, -v[2], v[1], v[2], 0, -v[0], -v[1], v[0], 0;

    Eigen::Matrix4d R = Eigen::Matrix4d::Identity() + v_x + v_x * v_x * (1.0 - c) / s / s;
    (void)R;
    for (std::vector<Star>::size_type i = 0; i < stars_in_camera_coords.size(); i++) {
        //XYZ cam_coords = R * stars_in_camera_coords[i].xyz();
        //stars_in_camera_coords[i].set_orientation(cam_coords);
    }

    return stars_in_camera_coords;
}

void Camera::capture(const Orientation& ori, const std::vector<Star>& stars)
{
    const auto stars_in_camera_coords = world_to_camera_coords(ori, stars);
    const auto stars_in_fov = get_stars_in_fov(ori, stars_in_camera_coords);

    for (const auto& star : stars_in_fov) {
        /*
        // convert to Homogenous coords
        Eigen::Vector4d xyz_hom;
        xyz_hom << star.xyz(), 1.0;

        Eigen::Vector3d pixel = (m_proj_matrix * xyz_hom);

        // to Euclidean coords
        pixel /= pi
        */

        const double X = star.xyz()[0];
        const double Y = star.xyz()[1];
        const double Z = star.xyz()[2];
        int px = std::round(m_f * X / Z + m_cx);
        int py = std::round(m_f * Y / Z + m_cy);
        std::cout << "Pixel: " << px << " " << py << std::endl;
        std::cout << "star.xyz(): " << star.xyz() << std::endl;

        // TODO: maybe point spread function and star magnitude
        m_ccd(px, py) = 1.0;
    }
}

std::vector<Star> Camera::get_stars_in_fov(const Orientation& ori, const std::vector<Star>& stars)
{
    std::vector<Star> stars_in_fov;

    for (const auto& star : stars) {
        XYZ uv1 = star.xyz().normalized();
        XYZ uv2 =  ori.xyz().normalized();
        std::cout << "dot\n" << "uv1: " << uv1 << "\nuv2: " << uv2 << "\nuv1 dot uv2: " << uv1.dot(uv2) << std::endl;
        double angle = std::acos(uv1.dot(uv2));

        if (std::abs(angle) < m_fov / 2.0)
            stars_in_fov.push_back(star);
    }

    return stars_in_fov;
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
