#pragma once

#include <string>
#include <vector>
#include <unordered_map>

namespace Catalog
{

    using RaDec = std::unordered_map<std::string, std::vector<double>>;

    class Catalog
    {

    public:
        Catalog(std::string path);

    private:
        RaDec m_ra_dec;
        RaDec read_csv(std::string path);
    };

}
