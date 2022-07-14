#include <tracker/tracker.hpp>
#include <tracker/orientation.hpp>

Tracker::Tracker(const RaDec& ra_dec, const std::string& catalog_path) :
Orientation(ra_dec),
Catalog(catalog_path)
{
}
