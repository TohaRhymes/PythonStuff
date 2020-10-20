fib_array = [1, 1]
with open('input.txt', 'r') as input_f, open('output.txt', 'w') as output_f:
    n = int(input_f.readline())
    while len(fib_array) < n:
        fib_array.append(fib_array[-1] + fib_array[-2])
    else:
        output_f.write(str(fib_array[-1]))
