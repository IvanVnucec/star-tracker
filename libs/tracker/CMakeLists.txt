cmake_minimum_required(VERSION 3.13)
project(tracker)

add_library(${PROJECT_NAME}
	camera.cpp
	catalog.cpp
	star.cpp
)

target_include_directories(${PROJECT_NAME}
	PUBLIC
		$<INSTALL_INTERFACE:include>
		$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
	PRIVATE
		${CMAKE_CURRENT_SOURCE_DIR}
)

target_compile_features(${PROJECT_NAME}
	PRIVATE
		cxx_std_17
)

target_link_libraries(${PROJECT_NAME}
	PRIVATE
		Eigen3::Eigen3
)

if(BUILD_TESTING)
    enable_testing()
	add_subdirectory(tests)
endif()
