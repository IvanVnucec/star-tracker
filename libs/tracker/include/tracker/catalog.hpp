#pragma once

#include <string>
#include <vector>
#include <tracker/star.hpp>

class Catalog
{

public:
    Catalog(std::string path);
    std::vector<Star> get_stars();

private:
    std::vector<Star> m_stars;
    std::vector<Star> read_csv(std::string path);
};
