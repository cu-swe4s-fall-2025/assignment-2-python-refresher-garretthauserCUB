import my_utils as mu

country = 'Afghanistan'
county_column = 0
forestFires_column = 'Forest fires'
file_name = 'Agrofood_co2_emission.csv'
forestFires = mu.get_column(file_name,
                            county_column,
                            country,
                            forestFires_column)
print(forestFires)
