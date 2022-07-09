cmake_minimum_required(VERSION 3.13)

set(SOURCE_FILES 
    main.cpp
    catalog.cpp
    star.cpp
)

add_executable(star-tracker ${SOURCE_FILES})

target_link_libraries(star-tracker -lX11 -lGL -lpthread -lpng -lstdc++fs)
