.PHONY: all setup cmake build run test clean

all: build

setup:
	sudo apt-get install -y libpng-dev libgl1-mesa-dev

cmake:
	cmake -B build

build:
	cmake --build build

run: build
	./build/src/simulator

test: build
	cmake -E chdir build ctest

clean:
	cd build && make clean
