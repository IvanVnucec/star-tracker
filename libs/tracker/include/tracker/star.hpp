#pragma once

#include <tracker/orientation.hpp>

class Star : public Orientation
{
private:
    double m_absmag;
 
public:
    Star(double ra, double dec, double absmag);
    double absmag() const;
};
