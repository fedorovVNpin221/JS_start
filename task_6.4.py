def depthLowerSum(pairs, depth, memo):
    '''
    exp that have lower or equal depth than 'depth'
    '''
    if memo[pairs][depth] != -1:
        return memo[pairs][depth]
    if pairs == 0 or depth == 1:
        memo[pairs][depth] = 1
        return 1
    s = 0
    for i in range(pairs):
        s += depthLowerSum(i, depth - 1, memo) * \
            depthLowerSum(pairs - 1 - i, depth, memo)
    memo[pairs][depth] = s
    return s

    f = open('input.txt')
    N, D = 161, 161
    memo = []
    for i in range(N):
        memo.append([-1] * D)
    while True:
        line = f.readline()
        if line == '':
            break
        length, depth = [int(x) for x in line.split()]
        pairs = int(length / 2)
        print(depthLowerSum(pairs, depth, memo)
              - depthLowerSum(pairs, depth - 1, memo))
