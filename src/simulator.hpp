#pragma once

#define OLC_PGE_APPLICATION
#include "olcPixelGameEngine.h"
#include <tracker/tracker.hpp>
#include <memory>

class Simulator : public olc::PixelGameEngine
{
private:
	std::shared_ptr<Tracker> m_tracker;

public:
	Simulator(std::shared_ptr<Tracker>& tracker) :
	m_tracker{ tracker }
	{
		sAppName = "Simulator";
        Construct(tracker->camera_pixel_w(), tracker->camera_pixel_h(), 1, 1);
	}

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
		//m_tracker->capture();
		CameraCCD ccd = m_tracker->camera_ccd();

		for (int x = 0; x < ScreenWidth(); x++) {
			for (int y = 0; y < ScreenHeight(); y++) {
				olc::Pixel p = PixelLerp(olc::BLACK, olc::WHITE, ccd(x, y));
				Draw(x, y, p);
            }
        }

        return true;
	}
};
