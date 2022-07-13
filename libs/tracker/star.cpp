#include <tracker/star.hpp>
#include <tracker/orientation.hpp>

Star::Star(double ra, double dec, double absmag) :
m_orientation{ Orientation(RaDec(ra, dec)) },
m_absmag{ absmag }
{
}

double Star::ra() const
{
    return m_orientation.get_ra_dec()[0];
}

double Star::dec() const
{
    return m_orientation.get_ra_dec()[1];
}

double Star::absmag() const
{
    return m_absmag;
}
