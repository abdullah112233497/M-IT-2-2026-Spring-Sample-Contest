Q = int(input())  # number of strings

for _ in range(Q):
    s = input().strip()
    n = len(s)
    found = False

    # Try all possible lengths of B (from 1 to n//2)
    for i in range(1, n // 2 + 1):
        # Check if last two B's are identical and A is non-empty
        if n - 2*i > 0 and s[n-2*i:n-i] == s[n-i:]:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")