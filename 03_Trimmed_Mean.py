N = int(input())
grades = list(map(int, input().split()))

# Sort the grades
grades.sort()

# Remove lowest N and highest N
trimmed = grades[N:-N]

# Compute average
average = sum(trimmed) / len(trimmed)

print(average)