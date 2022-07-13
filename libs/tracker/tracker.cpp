#include <tracker/tracker.hpp>
#include <filesystem>

static const std::string CATALOG_PATH = std::filesystem::current_path() / "catalog/hygdata_v3.csv";

Tracker::Tracker(const Orientation& orientation) :
m_orientation{ orientation },
m_catalog{ Catalog(CATALOG_PATH) } 
{
}

Orientation Tracker::get_orientation() {
    return m_orientation;
}
