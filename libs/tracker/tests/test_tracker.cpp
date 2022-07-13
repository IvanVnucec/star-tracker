#include "minunit.h"
#include "utils.hpp"
#include <tracker/tracker.hpp>

void test_setup(void) {
}

void test_teardown(void) {
}

MU_TEST(test_tracker_get_orientation) {
	const Orientation ori_ref(RaDec(0, 0));

	Tracker tracker(ori_ref, Utils::get_catalog_path());
	const Orientation ori_tra = tracker.get_orientation();

	mu_check(ori_ref.get_ra_dec() == ori_tra.get_ra_dec());
}

MU_TEST(test_tracker_set_orientation) {
	Tracker tracker(RaDec(0, 0), Utils::get_catalog_path());

	const Orientation ori_new(RaDec(1.2, 1.3));
	tracker.set_orientation(ori_new);

	mu_check(tracker.get_orientation().get_ra_dec() == ori_new.get_ra_dec());
}

MU_TEST_SUITE(test_suite) {
	MU_SUITE_CONFIGURE(&test_setup, &test_teardown);

	MU_RUN_TEST(test_tracker_get_orientation);
	MU_RUN_TEST(test_tracker_set_orientation);
}

int main(int argc, char *argv[]) {
	MU_RUN_SUITE(test_suite);

	MU_REPORT();

	return MU_EXIT_CODE;
}
