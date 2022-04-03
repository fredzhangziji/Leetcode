# 输入的list个数
n = int(input())
res = []
for i in range(n):
    attendance = input().split()
    # 统计未正常出勤次数
    absentCnt = 0
    contLateAndLeaveearlyCnt = 0
    flag = True
    
    for element in attendance:
        if element == 'absent':
            contLateAndLeaveearlyCnt = 0 # 连续迟到早退清零
            absentCnt += 1
            if absentCnt > 1:
                flag = False
                res.append('false')
                break
        if element == 'late' or 'leaveearly':
            contLateAndLeaveearlyCnt += 1
            if contLateAndLeaveearlyCnt > 1:
                flag = False
                res.append('false')
                break
        if element == 'present':
            contLateAndLeaveearlyCnt = 0 # 连续迟到早退清零
    
    if flag == False:
        continue
    if len(attendance) < 7:
        res.append('true')
    else:
        for i in range(len(attendance) - 7 + 1):
            if flag == False:
                break

            window = attendance[i: i + 7]
            totalBadCnt = 0
            for element in window:
                if element == 'late' or element == 'leaveearly' or element == 'absent':
                    totalBadCnt += 1
                    if totalBadCnt > 3:
                        flag = False
                        res.append('false')
                        break
                        
        if flag == True:
            res.append('true')

for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i])
    else:
        print(res[i], end=' ')