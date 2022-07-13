#pragma once

#include <string>
#include <vector>
#include <tracker/star.hpp>

class Catalog
{

public:
    Catalog(const std::string& path);
    std::vector<Star> get_stars();

private:
    std::vector<Star> m_stars;
    std::vector<Star> read_csv(const std::string& path);
};
