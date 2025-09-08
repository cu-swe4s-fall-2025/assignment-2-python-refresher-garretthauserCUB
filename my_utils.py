def get_column(file_name, query_column, query_value, result_column):
    output = []
    f = open(file_name, 'r')
    for line in f:
        row = line.strip().split(',')
        if row[query_column] == query_value:
            output.append(row[result_column])
    f.close()
    return output
