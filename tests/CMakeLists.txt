project(tests)

set(COMMON_LIBS
    tracker
    -lm
)

add_executable(test_template test_template.cpp)
target_link_libraries(test_template PRIVATE ${COMMON_LIBS})
add_test(NAME test_template COMMAND test_template)
