#include "tracker/star.hpp"

Star::Star(double ra, double dec, double absmag)
{
    m_ra = ra;
    m_dec = dec;
    m_absmag = absmag;
}

double Star::ra() const
{
    return m_ra;
}

double Star::dec() const
{
    return m_dec;
}

double Star::absmag() const
{
    return m_absmag;
}
