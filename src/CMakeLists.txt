cmake_minimum_required(VERSION 3.13)
project(simulation)

set(TRACKER_APP ${PROJECT_NAME})
set(TRACKER_LIB tracker)

add_library(${TRACKER_LIB}
	catalog.cpp
	star.cpp
)

add_executable(${TRACKER_APP}
    main.cpp
)

# Tracker app settings
target_compile_features(${TRACKER_APP}
	PRIVATE
		cxx_std_17
)

target_link_libraries(${TRACKER_APP}
	PRIVATE
        ${TRACKER_LIB}
        -lX11
        -lGL
        -lpthread
        -lpng
        -lstdc++fs
)

# Tracker library settings
target_include_directories(${TRACKER_LIB}
    PRIVATE
	PUBLIC
		${CMAKE_CURRENT_SOURCE_DIR}
)

target_compile_features(${TRACKER_LIB}
	PRIVATE
		cxx_std_17
)

target_link_libraries(${TRACKER_LIB}
	PRIVATE
)
