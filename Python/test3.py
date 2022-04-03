# input
n = int(input())
dir = []
for i in range(n):
    dir.append(list(map(int, input().split())))
deleteDir = int(input())

queue = []
queue.append(deleteDir)
deleted = []
while queue:
    size = len(queue)
    for i in range(size):
        curNode = queue.pop(0)
        for j in range(len(dir)):
            # curNode是父目录
            if curNode == dir[j][1]:
                queue.append(dir[j][0])
                deleted.append(dir[j])
            # curNode是子目录
            if curNode == dir[j][0]:
                deleted.append(dir[j])

for i in range(len(dir)):
    if 0 in dir[i]:
        deleted.append(dir[i])

res = []
for element in dir:
    if element not in deleted:
        res.append(element)

for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i][0], res[i][1])
    else:
        print(res[i][0], res[i][1], end=' ')