def group_equal(els):
    if len(els) == 0:
        return []
    answer_list = [[els[0]]]
    for i in range(1, len(els)):
        el = els[i]
        if el == answer_list[len(answer_list) - 1][0]:
            answer_list[len(answer_list) - 1].append(el)
        else:
            answer_list.append([el])
    return answer_list


print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]) == [[1, 1], [4, 4, 4], ["hello", "hello"], [4]])
print(group_equal([1, 2, 3, 4]) == [[1], [2], [3], [4]])
print(group_equal([1]) == [[1]])
print(group_equal([]) == [])
