#include <tracker/catalog.hpp>
#include <string>
#include <fstream>
#include <iostream>

static std::vector<std::string> split(const std::string &s, char seperator);

Catalog::Catalog(std::string path)
{
    m_stars = read_csv(path);
    // TODO: handle data
}

// Reads a CSV file into a vector of <string, vector<int>> pairs where
// each pair represents <column name, column values>
std::vector<Star> Catalog::read_csv(std::string path)
{
    std::vector<Star> stars;
    std::ifstream file(path);
    std::string line, colname;

    if (!file.is_open())
        throw std::runtime_error("Could not open a file at " + path);

    // skip csv header
    std::getline(file, line);

    // Read data, line by line
    while (std::getline(file, line))
    {
        std::vector<std::string> cols = split(line, ',');
        double ra = std::stod(cols[7]);
        double dec = std::stod(cols[8]);
        double absmag = std::stod(cols[14]);

        auto star = Star(ra, dec, absmag);
        stars.push_back(star);
    }

    // Close file
    file.close();

    return stars;
}

std::vector<Star> Catalog::get_stars()
{
    return m_stars;
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
