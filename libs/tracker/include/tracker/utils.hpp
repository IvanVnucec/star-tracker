#pragma once

#include <cmath>

namespace Utils {

template<typename T>
T rad_to_deg(const T& rad) {
    return rad / M_PI * 180.0;
}

template<typename T>
T deg_to_rad(const T& deg) {
    return deg / 180.0 * M_PI;
}

}
