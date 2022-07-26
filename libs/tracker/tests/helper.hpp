#pragma once

#include <filesystem>

namespace Helper {

std::string get_catalog_path() {
    const auto path = std::filesystem::current_path() 
        / "../../../../libs/tracker/catalog/hygdata_v3.csv";
    return path.string();
}

}
