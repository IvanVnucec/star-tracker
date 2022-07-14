#include <tracker/star.hpp>
#include <tracker/orientation.hpp>

Star::Star(double ra, double dec, double absmag) :
Orientation(RaDec(ra, dec)),
m_absmag{ absmag }
{
}

double Star::absmag() const
{
    return m_absmag;
}
