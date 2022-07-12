#include "minunit.h"
#include <memory>
#include <vector>
#include <filesystem>
#include <tracker/catalog.hpp>

static const auto catalog_path = 
	std::filesystem::current_path() / "../../../../libs/tracker/catalog/hygdata_v3.csv"; 
static std::shared_ptr<Catalog> catalog;

void test_setup(void) {
	catalog = std::make_shared<Catalog>(catalog_path);
}

void test_teardown(void) {
}

MU_TEST(test_catalog_load_csv) {
	const std::vector<Star> stars = catalog->get_stars();

    mu_assert_int_eq(119614, stars.size());

	// id = 0
	mu_assert_double_eq(0.000, stars[0].ra());
	mu_assert_double_eq(0.000, stars[0].dec());
	mu_assert_double_eq(4.850, stars[0].absmag());

	// id = 1
	mu_assert_double_eq(0.000060, stars[1].ra());
	mu_assert_double_eq(1.089009, stars[1].dec());
	mu_assert_double_eq(2.390000, stars[1].absmag());

	// id = last
	mu_assert_double_eq(0.036059, 	stars[stars.size() - 1].ra());
	mu_assert_double_eq(-43.165974, stars[stars.size() - 1].dec());
	mu_assert_double_eq(13.589, 	stars[stars.size() - 1].absmag());
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
