t = int(input())
for _ in range(t):
    a = int(input())
    n = list(map(int,input().split()))
    n.sort()
    diff = n[0] - n[1]
    diff = abs(diff)
    print(diff)
    
