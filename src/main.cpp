#include <iostream>
#include "catalog.hpp"

int main()
{
	Catalog::Catalog catalog("/home/ivan/Desktop/star-tracker/star-catalog/hygdata_v3.csv");

	std::cout << "hello" << std::endl;

	return 0;
}
