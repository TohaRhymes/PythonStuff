def create_intervals(data):
    data_list = sorted(list(data))
    intervals_list = []
    start_number = data_list[0]
    previous_number = data_list[0]
    for i in range(1, len(data_list)):
        number = data_list[i]
        if number - 1 == previous_number:
            previous_number = number
        else:
            intervals_list.append((start_number, previous_number))
            start_number = number
            previous_number = number
    intervals_list.append((start_number, previous_number))
    return intervals_list

# print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)])
# print(create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)])
# print(create_intervals({4}) == [(4, 4)])
