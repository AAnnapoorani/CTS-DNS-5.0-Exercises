#Bubble Sort

orders = [5000, 1200, 9000, 3000, 7000]

n = len(orders)

for i in range(n):

    for j in range(0, n-i-1):

        if orders[j] > orders[j+1]:

            temp = orders[j]
            orders[j] = orders[j+1]
            orders[j+1] = temp

print("Sorted Orders:")
print(orders)

#Quick Sort

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:

        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


orders = [5000, 1200, 9000, 3000, 7000]

print(quick_sort(orders))