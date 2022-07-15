#include <tracker/tracker.hpp>
#include <tracker/orientation.hpp>
#include <tracker/camera.hpp>

Tracker::Tracker(const RaDec& ra_dec, const std::string& catalog_path) :
Orientation(ra_dec),
m_catalog{ Catalog(catalog_path) },
m_camera{ Camera() }
{
}

Camera Tracker::camera() {
    return m_camera;
}
