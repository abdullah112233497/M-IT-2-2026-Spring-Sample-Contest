N = int(input())
A = list(map(int, input().split()))

visited = [False] * N
in_cycle = [False] * N

for i in range(N):
    if visited[i]:
        continue
    path = []
    cur = i
    while True:
        if visited[cur]:
            if cur in path:
                idx = path.index(cur)
                for node in path[idx:]:
                    in_cycle[node] = True
            break
        visited[cur] = True
        path.append(cur)
        cur = A[cur] - 1  # go to next node

# count rounds Takahashi can win
ans = sum(in_cycle)
print(ans)