#include "minunit.h"
#include <tracker/orientation.hpp>
#include <cmath>

void test_setup(void) {
}

void test_teardown(void) {
}

MU_TEST(test_orientation_constr_ra_dec) {
    Orientation orientation(RaDec(1.1, 2.2));

    XYZ xyz = orientation.xyz();

    // https://keisan.casio.com/exec/system/1359534351
    // Warning: in program there are spherical coords and not ra, dec
	mu_assert_double_eq(-0.2669418242416, xyz[0]);
	mu_assert_double_eq(-0.5244765271023, xyz[1]);
	mu_assert_double_eq( 0.8084964038196, xyz[2]);
}

MU_TEST(test_orientation_constr_xyz) {
    Orientation orientation(XYZ(100, 200, 300));

    RaDec ra_dec = orientation.ra_dec();

    // https://keisan.casio.com/exec/system/1359533867
    // Warning: in program there are spherical coords and not ra, dec
	mu_assert_double_eq(1.1071487177941, ra_dec[0]);
	mu_assert_double_eq(0.9302740141155, ra_dec[1]);
}

MU_TEST(test_orientation_set_orientation_ra_dec) {
    Orientation orientation(RaDec(0, 0));

	RaDec ra_dec_set(1, 2);
    orientation.set_orientation(ra_dec_set);

	RaDec ra_dec_get = orientation.ra_dec();

	mu_check(ra_dec_set == ra_dec_get);
}

MU_TEST(test_orientation_set_orientation_xyz) {
    Orientation orientation(XYZ(0, 0, 0));

	XYZ xyz_set(1, 2, 3);
    orientation.set_orientation(xyz_set);

	XYZ xyz_get = orientation.xyz();

	mu_check(xyz_set == xyz_get);
}

MU_TEST(test_orientation_known_values) {
    Orientation orientation(RaDec(0.0, 0.0));
    XYZ xyz = orientation.xyz();
	mu_assert_double_eq(1.0, xyz[0]);
	mu_assert_double_eq(0.0, xyz[1]);
	mu_assert_double_eq(0.0, xyz[2]);

	orientation = RaDec(M_PI_2, 0.0);
    xyz = orientation.xyz();
	mu_assert_double_eq(0.0, xyz[0]);
	mu_assert_double_eq(1.0, xyz[1]);
	mu_assert_double_eq(0.0, xyz[2]);

	orientation = RaDec(M_PI, 0.0);
    xyz = orientation.xyz();
	mu_assert_double_eq(-1.0, xyz[0]);
	mu_assert_double_eq(0.0, xyz[1]);
	mu_assert_double_eq(0.0, xyz[2]);

	orientation = RaDec(M_PI + M_PI_2, 0.0);
    xyz = orientation.xyz();
	mu_assert_double_eq(0.0, xyz[0]);
	mu_assert_double_eq(-1.0, xyz[1]);
	mu_assert_double_eq(0.0, xyz[2]);

	orientation = RaDec(0.0, M_PI_2);
    xyz = orientation.xyz();
	mu_assert_double_eq(0.0, xyz[0]);
	mu_assert_double_eq(0.0, xyz[1]);
	mu_assert_double_eq(1.0, xyz[2]);

	orientation = RaDec(0.0, -M_PI_2);
    xyz = orientation.xyz();
	mu_assert_double_eq(0.0, xyz[0]);
	mu_assert_double_eq(0.0, xyz[1]);
	mu_assert_double_eq(-1.0, xyz[2]);
}

MU_TEST_SUITE(test_suite) {
	MU_SUITE_CONFIGURE(&test_setup, &test_teardown);

	MU_RUN_TEST(test_orientation_constr_ra_dec);
	MU_RUN_TEST(test_orientation_constr_xyz);
	MU_RUN_TEST(test_orientation_set_orientation_ra_dec);
	MU_RUN_TEST(test_orientation_set_orientation_xyz);
	MU_RUN_TEST(test_orientation_known_values);
}

int main(int argc, char *argv[]) {
	MU_RUN_SUITE(test_suite);

	MU_REPORT();

	return MU_EXIT_CODE;
}
