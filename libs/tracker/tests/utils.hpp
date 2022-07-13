#pragma once

#include <filesystem>

namespace Utils {

std::string get_catalog_path() {
    return std::filesystem::current_path() / "../../../../libs/tracker/catalog/hygdata_v3.csv";
}

}
