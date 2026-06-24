def binary_search(numbers, sn):
    l = 0
    r = len(numbers) - 1
    while True:
        if l > r:
            return -1
        mid = (l + r) // 2
        if numbers[mid] == sn:
            return mid
        elif sn > numbers[mid]:
            l = mid + 1
        else:
            r = mid - 1


numbers = list(map(int, input().split()))
sn = int(input())

print("Searched number index is: ", binary_search(numbers, sn))
