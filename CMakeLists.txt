cmake_minimum_required(VERSION 3.13)
project(star-tracker)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME AND NOT BUILD_TESTING)
    set(BUILD_TESTING ON)
endif()

if(BUILD_TESTING)
    enable_testing()
    add_subdirectory(tests)
endif()
add_subdirectory(libs)
add_subdirectory(src)

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
    include(CTest)
endif()
