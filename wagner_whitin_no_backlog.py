import random


"a) no backlog allowed"
def wagner_whitin(N, K, c, h, demand):
    """
    :param N: planning horizon
    :param K: production setup cost
    :param c: unit production cost
    :param h: unit holding cost
    :param demand: demand forecast
    :return: list-production decision
    """
    cost = [[float('inf') for i in range(N)] for j in range(N)]
    optCost = [float('inf')]*N  # optimal cost
    optCost.append(0)
    order = [float('inf')]*N  # optimal production plan, 0: no production, 1: production
    plan = [float('inf')] * N

    # Getting the lowest cost for each period
    for i in range(N-1, -2, -1):
        if i < (N-1):
            p = [0] * N
            for j in range(N):
                p[j] = cost[i+1][j]
            optCost[i + 1] = min(p)
        if i >= 0:
            for j in range(i, N):
                sum = 0
                for num in range(i, j + 1):
                    sum += demand[num]
                h_sum = 0
                c_sum = c * sum
                for num in range(i, j + 1):
                    h_sum = h_sum + h * (sum - demand[num])
                    sum = sum - demand[num]
                cost[i][j] = optCost[j + 1] + h_sum + K + c_sum


#cost = [[37, 42, 53, 51], [float("inf"), 28, 33, 30], [float("inf"), float("inf"), 17, 13], [float("inf"), float("inf"), float("inf"), 6]]
#optCost = [37, 28, 13, 6]  # optimal cost
#order = [1, 1, 1, 0]

    # Get the best production order in forward order
    i = 0
    while i <= N-1:
        if optCost[i] == cost[i][i]:
            order[i] = 1
            i = i+1
        else:
            order[i] = 0
            index = i
            for k in range(i, N):
                if optCost[i] == cost[i][k]:
                    index = k
                    order[i] = 1
                    break
            for k in range(i+1, index+1):
                order[k] = 0
            i = index + 1

    # Get the optimal production plan
    sum = 0
    for i in range(len(order)-1, -1, -1):
        if order[i] == 1:
            plan[i] = sum + demand[i]
            sum = 0
        else:
            sum += demand[i]
            plan[i] = 0
    print("The optimal production plan is {}, and the optimal cost is {}.".format(plan, optCost[0]))


demand = [random.randint(1, 20) for i in range(100)]
N = 100
K = 40
c = 0
h = 5
wagner_whitin(N, K, c, h, demand)





