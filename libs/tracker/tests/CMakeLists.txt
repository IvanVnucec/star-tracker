project(tests)

set(COMMON_LIBS
    Eigen3::Eigen3
    tracker
    -lm
)

add_executable(test_camera test_camera.cpp)
target_compile_features(test_camera PRIVATE cxx_std_17)
target_link_libraries(test_camera PRIVATE ${COMMON_LIBS})
add_test(NAME test_camera COMMAND test_camera)

add_executable(test_catalog test_catalog.cpp)
target_compile_features(test_catalog PRIVATE cxx_std_17)
target_link_libraries(test_catalog PRIVATE ${COMMON_LIBS})
add_test(NAME test_catalog COMMAND test_catalog)

add_executable(test_orientation test_orientation.cpp)
target_compile_features(test_orientation PRIVATE cxx_std_17)
target_link_libraries(test_orientation PRIVATE ${COMMON_LIBS})
add_test(NAME test_orientation COMMAND test_orientation)

add_executable(test_tracker test_tracker.cpp)
target_compile_features(test_tracker PRIVATE cxx_std_17)
target_link_libraries(test_tracker PRIVATE ${COMMON_LIBS})
add_test(NAME test_tracker COMMAND test_tracker)
