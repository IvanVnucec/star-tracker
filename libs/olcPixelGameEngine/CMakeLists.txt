cmake_minimum_required(VERSION 3.13)

project(olcPixelGameEngine)

add_library(${PROJECT_NAME} INTERFACE)
add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})
target_compile_features(${PROJECT_NAME} INTERFACE cxx_std_17)

target_compile_definitions(${PROJECT_NAME}
    INTERFACE
)

target_include_directories(${PROJECT_NAME}
    INTERFACE
        ${CMAKE_CURRENT_SOURCE_DIR}
)

target_link_libraries(${PROJECT_NAME}
	INTERFACE
        -lX11
        -lGL
        -lglut
        -lpthread
        -lpng
        -lstdc++fs
        -luser32
        -lgdi32
        -lopengl32
        -lgdiplus
        -lShlwapi
        -ldwmapi
        -lstdc++fs
)
