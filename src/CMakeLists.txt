cmake_minimum_required(VERSION 3.13)
project(simulation)

set(SOURCE_FILES 
    main.cpp
)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})

target_link_libraries(${PROJECT_NAME}
	PRIVATE
		libs::tracker
        -lX11
        -lGL
        -lpthread
        -lpng
        -lstdc++fs
)
