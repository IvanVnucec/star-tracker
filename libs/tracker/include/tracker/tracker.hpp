#pragma once

#include <tracker/camera.hpp>
#include <tracker/catalog.hpp>
#include <tracker/orientation.hpp>

class Tracker : public Orientation {
private:
    Catalog m_catalog;
    Camera m_camera;

public:
    Tracker(const RaDec& ra_dec, const std::string& catalog_path);
    Camera camera();
};
