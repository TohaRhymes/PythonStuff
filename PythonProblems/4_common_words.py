def checkio(first, second):
    words_first = str(first).strip().split(",")
    words_second = str(second).strip().split(",")
    words_common = []

    for word in words_second:
        # лучше, чтобы words_second - был dict, так как сложность меньше
        if word in words_first:
            words_common.append(word)
    words_common.sort()
    answer = ''
    for word in words_common:
        answer += word + ','
    return answer.strip(',')


assert (checkio("hello,world", "hello,earth") == "hello")
# print(checkio("one,two,three", "four,five,six") == "")
# print(checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two")
