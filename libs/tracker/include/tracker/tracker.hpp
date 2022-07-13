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
    Tracker(const Orientation& orientation);
    Orientation get_orientation();
};
