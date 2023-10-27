arr = [5, 8, 6, 4, 9, 2, 7, 3]
max_berry = set()
for i in range(len(arr)):
    sum_ = arr[i-1] + arr[i] + arr[(i+1) % len(arr)]
    max_berry.add(sum_)
print(max(max_berry))