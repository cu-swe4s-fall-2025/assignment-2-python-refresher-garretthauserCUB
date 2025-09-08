[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

completed get_column() function in my_utils.py code.

In print_filres.py code:
- changed country_columns = 1 to country_columns = 0.
This was done because 'Area' data is stored in first column, indexed from zero in Agrofood_co2_emmisions.csv.
- updated variavle name fires_column to forestFires_column.
This is done bacause there are two columns in Agrofood_co2_emmisions.csv that track fire data; Savana fires and Forest fires. The original fires_column = 4 corresponds to the Forest fire column in the dataset.

updated get_column() function in my_utils.py code to accept string values for result_column variable, and defaults to 1 if result_column is not passed a value when get_column() is called. Changed the value of variable forestFires_column from 4 to 'Forest fires'.