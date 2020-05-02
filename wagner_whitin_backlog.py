import random


"b) backlog allowed"
def wagner_whitin(N, K, c, h, b, demand):
    """
    :param N: planning horizon
    :param K: production setup cost
    :param c: unit production cost
    :param h: unit holding cost
    :param b: unit backlog cost
    :param demand: demand forecast
    :return: list-production decision
    """
    cost = [[float('inf') for i in range(N)] for j in range(N)]
    optCost = [float('inf')] * N  # optimal cost
    optCost.append(0)
    optK = [[float('inf') for i in range(N)] for j in range(N)]
    order = [0] * N  # optimal production plan, 0: no production, 1: production
    plan = [0] * N

    # Getting the lowest cost for each period
    for i in range(N - 1, -2, -1):
        if i < (N - 1):
            p = [0] * N
            for j in range(N):
                p[j] = cost[i + 1][j]
            optCost[i + 1] = min(p)
        if i >= 0:
            for j in range(i, N):
                sum = 0
                for num in range(i, j + 1):
                    sum += demand[num]
                c_sum = c * sum
                c_star = float('inf')
                for k in range(i, j+1):
                    sumC = 0
                    for num in range(k, j+1):
                        sumC += demand[num]
                    h_sum = 0
                    b_sum = 0
                    for p in range(k, j+1):
                        h_sum = h_sum + h * (sumC - demand[p])
                        sumC = sumC - demand[p]
                    sumC = 0
                    for q in range(i, k):
                        sumC = sumC + demand[q]
                        b_sum = b_sum + b * sumC
                    c_cost = K + h_sum + b_sum + c_sum
                    if c_cost < c_star:
                        c_star = c_cost
                        optK[i][j] = k
                cost[i][j] = optCost[j + 1] + c_star

# cost [[25, 25, 20], [float('inf'), 20, 15], [float('inf'), float('inf'), 10]]
# optcost [20, 15, 10, 0]
# order [1, 0, 0]
# Inventory [20, 5, 0]
# optK = [[0, 1, 1], [inf, 1, 1], [inf, inf, 2]]
# [20, 5, 0]
    # Get the optimal production plan
    i = 0
    while i <= N - 1:
        production = 0
        if optCost[i] == cost[i][i]:
            plan[optK[i][i]] = demand[i]
            i = optK[i][i] + 1
        else:
            index = i
            for k in range(i, N):
                production += demand[k]
                if optCost[i] == cost[i][k]:
                    index = k
                    plan[optK[i][k]] = production
                    break
            i = index + 1
    print("The optimal production plan is {}, and the optimal cost is {}.".format(plan, optCost[0]))


demand = [random.randint(1, 20) for i in range(100)]
N = 100
K = 40
c = 0
h = 5
b = 10
wagner_whitin(N, K, c, h, b, demand)
