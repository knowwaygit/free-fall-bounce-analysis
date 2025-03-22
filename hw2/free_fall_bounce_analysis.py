# 初始高度h0
h0 = 100
# 重力加速度
g = 9.8

#计算第n次反弹的高度
def height(n):
    return h0 * (1/2)**n

#计算反弹的总路程
def distance(n):
    # 第一次下落的路程
    total_distance = h0
    # 总路程 = 初始下落 + 前n-1次往返（应用了等比数列求和公式） + 第n次上升
    total_distance = h0 + 2 * h0 * (1 - 0.5 ** (n-1)) + h0 * 0.5 ** n
    return total_distance

#计算第n次掉下并反弹到最高点时的总时间
def time(n):
    # 第一次下落的时间
    total_time = (2 * h0 / g)**0.5
    # 每次反弹和下落的时间
    for i in range(1, n):
        total_time += 2 * (2 * h0 * (1/2)**i / g)**0.5
    # 第n次反弹的时间
    total_time += (2 * h0 * (1/2)**n / g)**0.5
    return total_time


# 第n次掉下并反弹到最高点时
n = 10  # 可以改为任意正整数
height_n = height(n)
distance_n = distance(n)
time_n = time(n)


print(f"第{n}次掉下并反弹到最高点时，反弹了{height_n:.2f}米，总路程为{distance_n:.2f}米，总时间为{time_n:.2f}秒。")