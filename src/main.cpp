#include <iostream>
#include <filesystem>
#include <tracker/tracker.hpp>
#include "simulator.hpp"

int main()
{
 	const auto catalog_path = 
		std::filesystem::current_path() / "libs/tracker/catalog/hygdata_v3.csv"; 

	Tracker tracker(RaDec(0, 0), catalog_path.string());

	Simulator sim(tracker);
	sim.start();

	return 0;
}
