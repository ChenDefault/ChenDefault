# 最小重量机器设计问题_优先队列分支限界法
import heapq

n, m, d = map(int, input().strip().split())
c = [0]
for i in range(n):
    tmp = [0] + list(map(int, input().strip().split()))
    c.append(tmp)
w = [0]
for i in range(n):
    tmp = [0] + list(map(int, input().strip().split()))
    w.append(tmp)

### ———————————————————— 优先队列 —————————————————————— ###

class node:
    def __init__(self, weight, choose, cost):
        self.weight = weight
        self.choose = choose
        self.cost = cost

    # 重载"<"运算符，按优先级排序，优先级定义为当前重量
    def __lt__(self, other):
        return self.weight < other.weight

h = []   # 小顶堆，当前重量越小对应着优先级越大
i = 1
cur_weight = 0
cur_choose = [None]
cur_cost = 0

while True:
    if i > n:  # 第一个叶子节点就对应着最优解
        min_weight = cur_weight
        ans = cur_choose[1:]
        break
    else:
        # 加入节点
        for j in range(1, m + 1):
            if cur_cost + c[i][j] <= d:    # 可行性剪枝
                tmp = cur_choose[:]
                tmp.append(j)
                tmpnode = node(cur_weight + w[i][j], tmp, cur_cost + c[i][j])
                heapq.heappush(h, tmpnode)

        # 取节点
        tmpnode = heapq.heappop(h)
        cur_weight, cur_choose, cur_cost = tmpnode.weight, tmpnode.choose, tmpnode.cost
        i = len(cur_choose)

print(min_weight)
for item in ans:
    print(item, end=' ')
