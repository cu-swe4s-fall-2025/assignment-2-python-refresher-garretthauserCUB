#!/bin/bash

echo "Running print_fires.py"
echo "case 1: working"
python print_fires.py --file_name "Agrofood_co2_emission.csv" --county_column 0 --country "United States of America" --forestFires_column "Forest fires"
echo "case 2: missing argument"
python print_fires.py --file_name "Agrofood_co2_emission.csv" --country "United States of America" --forestFires_column "Forest fires"
echo "case 3: wrong country column"
python print_fires.py --file_name "Agrofood_co2_emission.csv" --county_column 1 --country "United States of America" --forestFires_column "Forest fires"
echo "Finished"
