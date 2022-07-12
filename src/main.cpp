#include <iostream>
#include <filesystem>
#include <tracker/catalog.hpp>

int main()
{
	const auto catalog_path = 
		std::filesystem::current_path() / "libs/tracker/catalog/hygdata_v3.csv"; 

	Catalog catalog(catalog_path);
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
