#include "minunit.h"
#include "helper.hpp"
#include <tracker/tracker.hpp>

void test_setup(void) {
}

void test_teardown(void) {
}

MU_TEST(test_tracker_constructor) {
	Tracker tracker(RaDec(0, 0), Helper::get_catalog_path());
}

MU_TEST_SUITE(test_suite) {
	MU_SUITE_CONFIGURE(&test_setup, &test_teardown);

	MU_RUN_TEST(test_tracker_constructor);
}

int main(int argc, char *argv[]) {
	MU_RUN_SUITE(test_suite);

	MU_REPORT();

	return MU_EXIT_CODE;
}
