books = ["Python", "Java", "C++", "Data Structures"]

search_book = "Java"

# Linear Search
for i in range(len(books)):

    if books[i] == search_book:
        print("Book Found at Index", i)
        break


# Binary Search
books.sort()

low = 0
high = len(books) - 1

while low <= high:

    mid = (low + high) // 2

    if books[mid] == search_book:
        print("Book Found using Binary Search")
        break

    elif books[mid] < search_book:
        low = mid + 1

    else:
        high = mid - 1