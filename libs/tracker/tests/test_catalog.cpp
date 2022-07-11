#include "minunit.h"
#include <memory>
#include <vector>
#include "tracker/catalog.hpp"

static std::shared_ptr<Catalog> catalog;

void test_setup(void) {
	catalog = std::make_shared<Catalog>("/home/ivan/Desktop/star-tracker/star-catalog/hygdata_v3.csv");
}

void test_teardown(void) {
}

MU_TEST(test_catalog_load_csv) {
	const std::vector<Star> stars = catalog->get_stars();

    mu_assert_int_eq(123123, stars.size());

	// id = 0
	mu_assert_double_eq(0.0, stars[0].ra());
	mu_assert_double_eq(0.0, stars[0].dec());
	mu_assert_double_eq(0.0, stars[0].absmag());

	// id = 1
	mu_assert_double_eq(0.0, stars[1].ra());
	mu_assert_double_eq(0.0, stars[1].dec());
	mu_assert_double_eq(0.0, stars[1].absmag());

	// id = last
	mu_assert_double_eq(0.0, stars[stars.size() - 1].ra());
	mu_assert_double_eq(0.0, stars[stars.size() - 1].dec());
	mu_assert_double_eq(0.0, stars[stars.size() - 1].absmag());

}

MU_TEST_SUITE(test_suite) {
	MU_SUITE_CONFIGURE(&test_setup, &test_teardown);

	MU_RUN_TEST(test_catalog_load_csv);
}

int main(int argc, char *argv[]) {
	MU_RUN_SUITE(test_suite);

	MU_REPORT();

	return MU_EXIT_CODE;
}
