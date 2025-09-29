#!/bin/bash

test -e ssshtest || curl -s -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest

source ssshtest

run test_print_fires_list python src/print_fires.py --file_name tests/functional_tests/functional_test_data.csv --county_column 0 --country Angola --forestFires_column "Forest fires"
assert_in_stdout 14510
assert_in_stdout 15184
assert_in_stdout 16368
assert_in_stdout 15318
assert_in_stdout 18570
assert_exit_code 0

run test_print_fires_mean python src/print_fires.py --file_name tests/functional_tests/functional_test_data.csv --county_column 0 --country Angola --forestFires_column "Forest fires" --operation mean
assert_in_stdout 15990
assert_exit_code 0

run test_print_fires_median python src/print_fires.py --file_name tests/functional_tests/functional_test_data.csv --county_column 0 --country Angola --forestFires_column "Forest fires" --operation median
assert_in_stdout 15318
assert_exit_code 0

run test_print_fires_stddev python src/print_fires.py --file_name tests/functional_tests/functional_test_data.csv --county_column 0 --country Angola --forestFires_column "Forest fires" --operation stddev
assert_in_stdout 1420.6
assert_exit_code 0
