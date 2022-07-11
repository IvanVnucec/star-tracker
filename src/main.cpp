#include <iostream>
#include "catalog.hpp"

int main()
{
	Catalog catalog("/home/ivan/Desktop/star-tracker/star-catalog/hygdata_v3.csv");
	const auto stars = catalog.get_stars();

	int i = 0;
	for (const auto& star : stars)
	{
		std::cout << i++ << " " 
		<< star.ra() << " " 
		<< star.dec() << " " 
		<< star.absmag() << "\n";
	}

	return 0;
}
