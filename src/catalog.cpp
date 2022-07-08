#include "catalog.hpp"
#include <string>
#include <fstream>

namespace Catalog
{

    static std::vector<std::string> split(const std::string &s, char seperator);

    Catalog::Catalog(std::string path)
    {
        m_ra_dec = read_csv(path);
        // TODO: handle data
    }

    // Reads a CSV file into a vector of <string, vector<int>> pairs where
    // each pair represents <column name, column values>
    RaDec Catalog::read_csv(std::string path)
    {
        RaDec result;
        std::ifstream file(path);
        std::string line, colname;

        if (! file.is_open())
            throw std::runtime_error("Could not open file");

        // skip csv header
        std::getline(file, line);

        // Read data, line by line
        while (std::getline(file, line))
        {
            std::vector<std::string> cols = split(line, ',');
            result["ra"].push_back(std::stod(cols[7]));
            result["dec"].push_back(std::stod(cols[8]));
        }

        // Close file
        file.close();

        return result;
    }

    static std::vector<std::string> split(const std::string &s, char seperator)
    {
        std::vector<std::string> output;
        std::string::size_type prev_pos = 0, pos = 0;

        while ((pos = s.find(seperator, pos)) != std::string::npos)
        {
            std::string substring(s.substr(prev_pos, pos - prev_pos));
            output.push_back(substring);
            prev_pos = ++pos;
        }

        output.push_back(s.substr(prev_pos, pos - prev_pos)); // Last word

        return output;
    }

} // namespace Catalog
