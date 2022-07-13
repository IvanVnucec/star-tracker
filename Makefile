.PHONY: all setup cmake build run test clean

all: build

setup:
	sudo apt-get install -y ninja-build libpng-dev libgl1-mesa-dev

cmake:
	cmake -GNinja -B build

build:
	cmake --build build

run: build
	./build/src/simulation

test: build
	cmake -E chdir build ctest

clean:
	cd build && make clean
