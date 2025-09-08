def get_column(file_name, query_column, query_value, result_column=1):
    output = []
    f = open(file_name, 'r')
    header = []
    for line in f:
        row = line.strip().split(',')
        if header == []:
            header = row
            if type(result_column) is str:
                result_column = header.index(result_column)
        if row[query_column] == query_value:
            output.append(row[result_column])
    f.close()
    return output
