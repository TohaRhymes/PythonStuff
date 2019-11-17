from numpy import transpose


def arg_and_max(a1, a2):
    return [True, a1] if a1 > a2 else [False, a2]


def viterbi():
    p_good_coin = pi[coin['g']] * b[coin['g']][let[s[0]]]
    p_bad_coin = pi[coin['b']] * b[coin['b']][let[s[0]]]
    way_good_coin = ''
    way_bad_coin = ''
    for i in range(1, len(s)):
        sign_good, new_good = arg_and_max(p_good_coin * a[coin['g']][coin['g']] * b[coin['g']][let[s[i]]],
                                          p_bad_coin * a[coin['b']][coin['g']] * b[coin['g']][let[s[i]]])
        sign_bad, new_bad = arg_and_max(p_good_coin * a[coin['g']][coin['b']] * b[coin['b']][let[s[i]]],
                                        p_bad_coin * a[coin['b']][coin['b']] * b[coin['b']][let[s[i]]])
        p_good_coin = new_good
        p_bad_coin = new_bad
        way_good_coin, way_bad_coin = [(way_good_coin + '+ ' if sign_good else way_bad_coin + '- '),
                                       (way_good_coin + '+ ' if sign_bad else way_bad_coin + '- ')]

    return way_good_coin + '+' if p_good_coin > p_bad_coin else way_bad_coin + '-'


def forward_backward():
    back_alpha = [[0] * len(s) for i in range(2)]
    for j in coin.values():
        back_alpha[j][0] = pi[j] * b[j][let[s[0]]]

    for t in range(1, len(s)):
        for j in coin.values():
            for i in coin.values():
                back_alpha[j][t] += back_alpha[i][t - 1] * a[i][j] * b[j][let[s[t]]]

    forward_beta = [[0] * len(s) for i in range(2)]
    for j in coin.values():
        forward_beta[j][len(s) - 1] = 1
    for t in range(len(s) - 2, -1, -1):
        for i in coin.values():
            for j in coin.values():
                forward_beta[i][t] += forward_beta[j][t + 1] * a[i][j] * b[j][let[s[t + 1]]]

    sum_alpha = 0
    for j in coin.values():
        sum_alpha += back_alpha[j][len(s) - 1]
    p = [[0] * len(s) for i in range(2)]

    for t in range(0, len(s)):
        for j in coin.values():
            p[j][t] = back_alpha[j][t] * forward_beta[j][t] / sum_alpha

    return p


# pi - начальные вероятности - вероятность изначально оказаться в скрытом состоянии i.
# a - матрица переходов скрытых состояний - вероятность перехода из состояния i в состояние j
# b - матрица вероятности генерации открытых состояний - вероятность, сгенерировать открытое состояние O, находясь в i.


# letters: 0 = 'H', 1 = 'R'
let = {'H': 0, 'T': 1}
# good_coin = 0, bad_coin = 1
coin = {'g': 0, 'b': 1}

s = 'ОРОРОРООРРРРРРРРРРОООООООО'
# орел - head, решка -  tail
s = s.replace('О', 'H').replace('Р', 'T')

# test1

pi = [0.5, 0.5]
a = [[0.8, 0.2],
     [0.2, 0.8]]
b = [[0.5, 0.5],
     [0.1, 0.9]]
print('Answer1_Viterbi:\n' + viterbi())
print('Answer1_Forward-Backward:\n' + str(transpose(forward_backward())))

# test2

pi = [0.5, 0.5]
a = [[0.5, 0.5],
     [0.5, 0.5]]
b = [[0.5, 0.5],
     [0.51, 0.49]]
print('\nAnswer2_Viterbi:\n' + viterbi())
print('Answer2_Forward-Backward:\n' + str(transpose(forward_backward())))
