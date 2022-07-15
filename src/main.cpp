#include <iostream>
#include <filesystem>
#include <tracker/tracker.hpp>

int main()
{
 	const auto catalog_path = 
		std::filesystem::current_path() / "libs/tracker/catalog/hygdata_v3.csv"; 

	Tracker tracker(RaDec(0, 0), catalog_path.string());
	const auto stars = tracker.get_stars();

	int i = 0;
	for (const auto& star : stars)
	{
		std::cout << i++ << " " 
		<< star.ra_dec()[0] << " " 
		<< star.ra_dec()[1] << " " 
		<< star.absmag() << "\n";
	}

	return 0;
}
