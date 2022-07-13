#pragma once

#include <tracker/camera.hpp>
#include <tracker/catalog.hpp>
#include <tracker/orientation.hpp>

class Tracker {
private:
    Orientation m_orientation;
    Catalog m_catalog;
    Camera m_camera;

public:
    Tracker(const Orientation& orientation, const std::string& catalog_path);
    Orientation get_orientation();
    void set_orientation(const Orientation& orientation);
};
