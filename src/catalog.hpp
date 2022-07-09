#pragma once

#include <string>
#include <vector>
#include "star.hpp"

namespace Catalog
{

    class Catalog
    {

    public:
        Catalog(std::string path);
        std::vector<Star::Star> get_stars();

    private:
        std::vector<Star::Star> m_stars;
        std::vector<Star::Star> read_csv(std::string path);
    };

}
