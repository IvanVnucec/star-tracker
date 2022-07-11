project(tests)

set (CMAKE_CXX_FLAGS "-lrt -lm")
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/../src")

add_executable(test_template test_template.cpp)
target_link_libraries(test_template PRIVATE libs::lib1)
add_test(NAME test_template COMMAND test_template)
