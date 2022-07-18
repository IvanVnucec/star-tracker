cmake_minimum_required(VERSION 3.13)
project(simulator LANGUAGES CXX)

add_executable(${PROJECT_NAME}
    main.cpp
)

# Tracker app settings
target_compile_features(${PROJECT_NAME}
	PRIVATE
		cxx_std_17
)

target_compile_options(${PROJECT_NAME} 
	PRIVATE
    	-Wall -Werror -O0 -ggdb -Wno-unknown-pragmas
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE
        tracker
		Eigen3::Eigen3
        olcPixelGameEngine
)
