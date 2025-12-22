

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

minimus = []
slist = []
for i in range(n):
    slist.append(arr[i])
    slist.sort()
    if i >= k:
        slist.remove(arr[i - k])
    if i >= k - 1:
        minimus.append(slist[0])

print(max(minimus))