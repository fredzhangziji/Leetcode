import sys

n = sys.stdin.readline().strip()
ans = 0
for i in range(int(n)):
    line = sys.stdin.readline().strip()

    values = map(int, line.split())
    print(values)
    # for v in values:
    #     ans += v

print(ans)