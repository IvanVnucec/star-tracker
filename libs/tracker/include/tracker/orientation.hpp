#pragma once

#include <Eigen/Dense>

using RaDec = Eigen::Vector2d;
using XYZ = Eigen::Vector3d;

class Orientation {
private:
    RaDec m_ra_dec;
    XYZ m_xyz;

    RaDec calc_ra_dec(const XYZ& xyz);
    XYZ calc_xyz(const RaDec& ra_dec);

public:
    Orientation(const RaDec& ra_dec);
    Orientation(const XYZ& xyz);

    RaDec ra_dec() const;
    XYZ   xyz() const;
    Orientation ori() const;

    template <typename T>
    void set_orientation(const T& ori) { *this = Orientation(ori); }
};
