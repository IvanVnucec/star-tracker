#include <tracker/tracker.hpp>
#include <tracker/orientation.hpp>
#include <filesystem>

Tracker::Tracker(const Orientation& orientation, const std::string& catalog_path) :
m_orientation{ orientation },
m_catalog{ Catalog(catalog_path) } 
{
}

Orientation Tracker::get_orientation() {
    return m_orientation;
}

void Tracker::set_orientation(const Orientation& orientation) {
    m_orientation = orientation;
}
