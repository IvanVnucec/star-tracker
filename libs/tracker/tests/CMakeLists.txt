project(tracker_tests)

set(COMMON_LIBS
    libs::tracker
    -lrt 
    -lm 
)

add_executable(test_catalog test_catalog.cpp)
target_link_libraries(test_catalog PRIVATE ${COMMON_LIBS})
add_test(NAME test_catalog COMMAND test_catalog)
