#pragma once

#include <tracker/camera.hpp>
#include <tracker/catalog.hpp>
#include <tracker/orientation.hpp>

class Tracker : public Orientation, public Catalog, public Camera {
private:
public:
    Tracker(const RaDec& ra_dec, const std::string& catalog_path);
};
