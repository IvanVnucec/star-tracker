#include <tracker/star.hpp>
#include <tracker/orientation.hpp>

Star::Star(RaDec ra_dec, double absmag) :
Orientation(ra_dec),
m_absmag{ absmag }
{
}

double Star::absmag() const
{
    return m_absmag;
}
