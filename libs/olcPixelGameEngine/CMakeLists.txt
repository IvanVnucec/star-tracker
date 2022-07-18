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

set(LIBS -lstdc++fs -lpthread)
if (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    list(APPEND LIBS -lX11 -lGL -lpthread -lpng )
elseif (${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    list(APPEND LIBS -luser32 -lgdi32 -lopengl32 -lgdiplus -lShlwapi -ldwmapi)
endif()

target_link_libraries(${PROJECT_NAME}
    INTERFACE
        ${LIBS}
)
