cmake_minimum_required(VERSION 3.13)
project(simulation)

add_executable(${PROJECT_NAME}
    main.cpp
)

# Tracker app settings
target_compile_features(${PROJECT_NAME}
	PRIVATE
		cxx_std_17
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE
        tracker
		Eigen3::Eigen3
        #olcPixelGameEngine
)
