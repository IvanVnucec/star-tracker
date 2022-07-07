#include "minunit.h"

MU_TEST(test_template) {
    mu_check(1 == 1);
}

MU_TEST_SUITE(test_suite) {
	MU_RUN_TEST(test_template);
}

int main(int argc, char *argv[]) {
	MU_RUN_SUITE(test_suite);

	MU_REPORT();

	return MU_EXIT_CODE;
}
