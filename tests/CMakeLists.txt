cmake_minimum_required(VERSION 3.13)

set (CMAKE_CXX_FLAGS "-lrt -lm")
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/../src")

add_executable(test_template test_template.cpp)
add_test(NAME test_template COMMAND test_template)
