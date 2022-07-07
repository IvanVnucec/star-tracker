.PHONY: all setup build run test clean

all: build

setup:
	sudo apt-get install -y libpng-dev
	mkdir build
	cd build && cmake ..

build:
	cd build && make

run: build
	./build/src/star-tracker

test: build
	cd build && ctest

clean:
	cd build && make clean
