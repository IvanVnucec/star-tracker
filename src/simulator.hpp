#pragma once

#define OLC_PGE_APPLICATION
#include "olcPixelGameEngine.h"
#include <tracker/tracker.hpp>

class Simulator : public olc::PixelGameEngine
{
public:
	Simulator(const Tracker& tracker)
	{
		sAppName = "Simulator";
        Construct(tracker.camera_pixel_w(), tracker.camera_pixel_h(), 1, 1);
	}

public:
    void start() 
    {
        PixelGameEngine::Start();
    }

	bool OnUserCreate() override
	{
		// Called once at the start, so create things here
		return true;
	}

	bool OnUserUpdate(float fElapsedTime) override
	{
		for (int x = 0; x < ScreenWidth(); x++) {
			for (int y = 0; y < ScreenHeight(); y++) {
				Draw(x, y, olc::Pixel(rand() % 255, rand() % 255, rand()% 255));	
            }
        }

        return true;
	}
};
