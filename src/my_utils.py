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
            output.append(int(float(row[result_column])))
    f.close()
    return output


def find_mean(data):
    return sum(data) / len(data)


def find_median(data):
    data.sort()
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n // 2 - 1] + data[n // 2]) / 2


def find_stddev(data):
    mean = find_mean(data)
    stddev = sum((x - mean) ** 2 for x in data) / len(data)
    return stddev ** 0.5


def main(file_name, query_column, query_value, result_column, operation):
    forestFires = get_column(file_name,
                             query_column,
                             query_value,
                             result_column)
    if operation == 'list':
        return forestFires
    elif operation == 'mean':
        mean = find_mean(forestFires)
        return mean
    elif operation == 'median':
        median = find_median(forestFires)
        return median
    elif operation == 'stddev':
        stddev = find_stddev(forestFires)
        return stddev
