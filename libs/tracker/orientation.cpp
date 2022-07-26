#include <tracker/orientation.hpp>
#include <math.h>

// ra_dec in radians
Orientation::Orientation(const RaDec& ra_dec) :
m_ra_dec{ ra_dec },
m_xyz{ calc_xyz(m_ra_dec) }
{
}

Orientation::Orientation(const XYZ& xyz) :
m_ra_dec{ calc_ra_dec(xyz) },
m_xyz{ xyz }
{
}

// ra_dec in radians
RaDec Orientation::ra_dec() const {
    return m_ra_dec;
}

XYZ Orientation::xyz() const {
    return m_xyz;
}

Orientation Orientation::ori() const {
    return *this;
}

RaDec Orientation::calc_ra_dec(const XYZ& xyz) {
    const double x = xyz[0];
    const double y = xyz[1];
    const double z = xyz[2];

    const double ra = std::atan2(y, x);
    const double dec  = M_PI_2 - std::atan2(std::sqrt(x*x + y*y), z); 

    return RaDec(ra, dec);
}

// ra_dec in radians
XYZ Orientation::calc_xyz(const RaDec& ra_dec) {
    const double ra  = ra_dec[0]; 
    const double dec = ra_dec[1];
 
    const double x = std::cos(dec) * std::cos(ra);
    const double y = std::cos(dec) * std::sin(ra);
    const double z = std::sin(dec);

    return XYZ(x, y, z);
}
