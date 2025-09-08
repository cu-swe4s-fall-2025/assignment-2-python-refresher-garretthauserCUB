import my_utils as mu

country = 'United States of America'
county_column = 0
forestFires_column = 4
file_name = 'Agrofood_co2_emission.csv'
forestFires = mu.get_column(file_name,
                            county_column,
                            country,
                            forestFires_column)
print(forestFires)
