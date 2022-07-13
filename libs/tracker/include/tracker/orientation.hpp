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

    RaDec get_ra_dec() const;
    XYZ get_xyz() const;
};
