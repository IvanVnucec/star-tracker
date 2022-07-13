#pragma once

#include <tracker/orientation.hpp>

class Star
{
private:
    Orientation m_orientation;
    double m_absmag;
 
public:
    Star(double ra, double dec, double absmag);
    double ra() const;
    double dec() const;
    double absmag() const;
};
