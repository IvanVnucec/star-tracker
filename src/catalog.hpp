#pragma once

#include <string>
#include <vector>

namespace Catalog
{

    using Data = std::vector<std::pair<std::string, std::vector<int>>>;

    class Catalog
    {

    public:
        Catalog(std::string path);

    private:
        Data m_data;
        Data read_csv(std::string path);
    };

}
