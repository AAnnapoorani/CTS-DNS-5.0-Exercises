products = [10, 20, 30, 40, 50, 60]

target = 40

# Linear Search
for i in range(len(products)):
    if products[i] == target:
        print("Linear Search Found at index", i)
        break

# Binary Search
low = 0
high = len(products) - 1

while low <= high:

    mid = (low + high) // 2

    if products[mid] == target:
        print("Binary Search Found at index", mid)
        break

    elif products[mid] < target:
        low = mid + 1

    else:
        high = mid - 1