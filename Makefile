.PHONY: all setup cmake build run test clean

all: build

setup:
	sudo apt-get install -y libpng-dev

cmake:
	cmake -B build

build:
	cmake --build build

run: build
	./build/src/simulation

test:
	cmake -E chdir build ctest

clean:
	cd build && make clean
