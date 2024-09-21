# функция для вычисления правильных выражений с глубиной depth
def depthLowerSum(pairs, depth, memo):
    # проверка на вычисление значение для данной пары
    if memo[pairs][depth] != -1:
        return memo[pairs][depth]
    # если количсетво пар равно 0 и глубина 1
    if pairs == 0 or depth == 1:
        memo[pairs][depth] = 1
        return 1
    s = 0
    # рекурсивное вычисление суммы для каждой пары
    for i in range(pairs):
        s += depthLowerSum(i, depth - 1, memo) * \
            depthLowerSum(pairs - 1 - i, depth, memo)
    # сохранение результата в массив nemo
    memo[pairs][depth] = s
    return s

if __name__ == '__main__':
    f = open('input_6.4.txt')
    N, D = 161, 161
    memo = []
    for i in range(N):
        memo.append([-1] * D)
    while True:
        line = f.readline()
        if line == '':
            break
        # разбиение строки на числа длины и глубины
        length, depth = [int(x) for x in line.split()]
        pairs = int(length / 2)
        # Выводим разницу между суммами для глубины depth и depth-1
        print(depthLowerSum(pairs, depth, memo)
              - depthLowerSum(pairs, depth - 1, memo))

