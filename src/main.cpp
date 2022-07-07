#define OLC_PGE_APPLICATION
#include "olcPixelGameEngine/olcPixelGameEngine.h"

class Example : public olc::PixelGameEngine
{
private:
	int m_width;
	int m_height;
	static constexpr int m_max_iteration = 10000;

	double map(double input, 
		const double input_start, 
		const double input_end, 
		const double output_start, 
		const double output_end) 
	{
		return output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start);
	}

	int getMandelbrotIterationsForPixel(const int px, const int py)
	{
		double x0 = map(px, 0, m_width, -2.00, 0.47);
		double y0 = map(py, 0, m_height, -1.12, 1.12);

		double x = 0.0;
		double y = 0.0;
		int iteration = 0;

		while (x*x + y*y <= 2*2 && iteration < m_max_iteration) {
			double xtemp = x*x - y*y + x0;
			y = 2*x*y + y0;
			x = xtemp;
			iteration += 1;
		}

		return iteration;
	}

	olc::Pixel palette(const int iteration)
	{
		return olc::PixelLerp(olc::BLACK, olc::WHITE, (float)iteration/m_max_iteration);
	}

public:
	Example()
	{
		sAppName = "Example";
	}

public:
	olc::rcode Construct(int32_t screen_w, int32_t screen_h)
	{
		m_width = screen_w;
		m_height = screen_h;
		return olc::PixelGameEngine::Construct(m_width, m_height, 1, 1);
	}

	bool OnUserCreate() override
	{
		// called once per frame
		for (int x = 0; x < m_width; x++) {
			for (int y = 0; y < m_height; y++) {
				int iter = getMandelbrotIterationsForPixel(x, y);
				auto pixel = palette(iter);
				Draw(x, y, pixel);
			}
		}

		return true;
	}

	bool OnUserUpdate(float fElapsedTime) override
	{
		return true;
	}
};


int main()
{
	Example demo;
	if (demo.Construct(200, 200*1.125))
		demo.Start();

	return 0;
}
