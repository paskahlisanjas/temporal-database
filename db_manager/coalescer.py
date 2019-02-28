def normalize_date(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date

def rearrange_interval(interval_a, interval_b):
    early, late = interval_a, interval_b
    if early[0] > late[0]:
        early, late = interval_b, interval_a
    return (early, late)

def mergeable(interval_a, interval_b):
    early, late = rearrange_interval(interval_a, interval_b)
    return early[1] == late[0]

def merge_range(early, late):
    return [early[0], late[1]]

def tail(ls):
    last_idx = len(ls) - 1
    return (last_idx, ls[last_idx])

def tune_result(result, columns):
    len_columns = len(columns)
    tuned_result = [result[0]]
    index = 1
    while index <= len(result) - 1:
        single_entity = True
        comparable_idx, comparable = tail(tuned_result)
        for column_index in range(len_columns):
            if comparable[column_index] != result[index][column_index]:
                single_entity = False
                break
        interval_a = [comparable[len_columns], comparable[len_columns + 1]]
        interval_b = [result[index][len_columns], result[index][len_columns + 1]]
        if single_entity and mergeable(interval_a, interval_b):
            merged = [result[index][column_index] for column_index in range(len_columns)]
            early, late = rearrange_interval(interval_a, interval_b)
            merged += merge_range(early, late)
            print(tuned_result)
            tuned_result[comparable_idx] = merged
        else:
            tuned_result += [result[index]]
        index += 1
    return tuned_result
