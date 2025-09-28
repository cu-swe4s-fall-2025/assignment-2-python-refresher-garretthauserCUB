#!/bin/bash

echo "Running print_fires.py"
echo "case 1: list forest fires in USA"
python print_fires.py --file_name "Agrofood_co2_emission.csv" --county_column 0 --country "United States of America" --forestFires_column "Forest fires"

echo "case 2: mean forest fires in USA"
python print_fires.py --file_name "Agrofood_co2_emission.csv" --county_column 0 --country "United States of America" --forestFires_column "Forest fires" --operation "mean"

echo "case 3: median forest fires in USA"
python print_fires.py --file_name "Agrofood_co2_emission.csv" --county_column 0 --country "United States of America" --forestFires_column "Forest fires" --operation "median"

echo "case 4: standard deviation of forest fires in USA"
python print_fires.py --file_name "Agrofood_co2_emission.csv" --county_column 0 --country "United States of America" --forestFires_column "Forest fires" --operation "stddev"
