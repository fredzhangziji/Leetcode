nums = list(map(int, input().split()))
k = int(input())
print(nums)

# 小于k的整数的数量
lessThanKCnt = 0
for i in nums:
    if i < k:
        lessThanKCnt += 1
res = lessThanKCnt

# 滑动窗口找含有最多的小于k的整数的窗口
for i in range(len(nums) - lessThanKCnt + 1):
    window = nums[i: i + lessThanKCnt]
    win = 0
    for j in window:
        if j < k:
            win += 1
        # 找最小交换次数
        res = min(res, lessThanKCnt - win)

print(res)