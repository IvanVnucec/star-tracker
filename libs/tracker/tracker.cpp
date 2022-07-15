#include <tracker/tracker.hpp>
#include <tracker/orientation.hpp>
#include <tracker/camera.hpp>

Tracker::Tracker(const RaDec& ra_dec, const std::string& catalog_path) :
Orientation(ra_dec),
m_catalog{ Catalog(catalog_path) },
m_camera{ Camera() }
{
}

CameraCCD Tracker::camera_capture()
{
    m_camera.capture(m_catalog.get_stars());
    return m_camera.ccd();
}

unsigned Tracker::camera_ccd_w()
{
    return m_camera.pixel_w();
}

unsigned Tracker::camera_ccd_h()
{
    return m_camera.pixel_h();
}
