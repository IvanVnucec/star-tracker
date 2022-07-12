#pragma once

class Star
{
private:
    double m_ra;
    double m_dec;
    double m_absmag;
 
public:
    Star(double ra, double dec, double absmag);
    double ra() const;
    double dec() const;
    double absmag() const;
};
