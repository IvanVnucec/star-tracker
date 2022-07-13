#include "minunit.h"
#include <tracker/tracker.hpp>

void test_setup(void) {
}

void test_teardown(void) {
}

MU_TEST(test_tracker_orientation) {
	const Orientation ori_ref(RaDec(0, 0));

	Tracker tracker(ori_ref);
	const Orientation ori_tra = tracker.get_orientation();

	mu_check(ori_ref.get_ra_dec() == ori_tra.get_ra_dec());
}

MU_TEST_SUITE(test_suite) {
	MU_SUITE_CONFIGURE(&test_setup, &test_teardown);

	MU_RUN_TEST(test_tracker_orientation);
}

int main(int argc, char *argv[]) {
	MU_RUN_SUITE(test_suite);

	MU_REPORT();

	return MU_EXIT_CODE;
}
