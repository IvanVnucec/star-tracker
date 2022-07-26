#include "minunit.h"
#include <tracker/camera.hpp>
#include <vector>
#include <cmath>

void test_setup(void) {
}

void test_teardown(void) {
}

MU_TEST(test_camera_capture_one_star_in_the_middle) {
	Camera camera;

	std::vector<Star> stars{ Star(RaDec(0, M_PI_2), 0) };

	camera.capture(RaDec(0, M_PI_2), stars);

	mu_assert_double_eq(1.0, camera.ccd()(camera.pixel_w()/2, camera.pixel_h()/2));
}

MU_TEST(test_camera_capture_one_star_in_the_middle_off_screen) {
	Camera camera;

	std::vector<Star> stars{ Star(RaDec(M_PI, 0), 0) };

	camera.capture(RaDec(0, 0), stars);

	mu_assert_double_eq(0.0, camera.ccd()(camera.pixel_w()/2, camera.pixel_h()/2));
}

MU_TEST_SUITE(test_suite) {
	MU_SUITE_CONFIGURE(&test_setup, &test_teardown);

	MU_RUN_TEST(test_camera_capture_one_star_in_the_middle);
	MU_RUN_TEST(test_camera_capture_one_star_in_the_middle_off_screen);
}

int main(int argc, char *argv[]) {
	MU_RUN_SUITE(test_suite);

	MU_REPORT();

	return MU_EXIT_CODE;
}
