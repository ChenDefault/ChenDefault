# 6_4最小重量机器设计问题, FIFO先进先出分支限界法
from queue import Queue

n, m, d = map(int, input().strip().split())
c = [0]
for i in range(n):
    tmp = [0] + list(map(int, input().strip().split()))
    c.append(tmp)
w = [0]
for i in range(n):
    tmp = [0] + list(map(int, input().strip().split()))
    w.append(tmp)

### ———————————————————— FIFO队列 ———————————————————— ###

q = Queue()
i = 1
min_weight = 2e10
cur_weight = 0
cur_choose = [None]
cur_cost = 0

while True:
    if i > n:    # 叶子节点
        if cur_weight < min_weight:     # 符合要求的更小重量及选择
            min_weight = cur_weight
            best_choose = cur_choose
        if q.empty():    # 处理完所有节点，退出
            break
        else:
            cur_weight, cur_choose, cur_cost = q.get()

    else:     # 非叶子节点
        for j in range(1, m + 1):
            # 做可行性剪枝
            if cur_cost + c[i][j] <= d:
                tmp = cur_choose[:]
                tmp.append(j)
                q.put([cur_weight + w[i][j], tmp, cur_cost + c[i][j]])

        # 取下一个节点
        cur_weight, cur_choose, cur_cost = q.get()
        i = len(cur_choose)

print(min_weight)
for item in best_choose[1:]:
    print(item, end=' ')

"""
输入：
3 3 4
1 2 3
3 2 1
2 2 2
1 2 3
3 2 1
2 2 2

输出：
4
1 3 3
"""
