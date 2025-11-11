# try:
#     w, h = list([int(i) for i in input("Enter width and height: ").split()])
# except ValueError:
#     print("Please enter exactly two numbers separated by space.")
#     exit()

# print("width:",w)
# print("width:",h)
# n=5
# for _ in range(n):
#     h = int(input("Enter a number: "))


# w = list(map(int, input().split()))

# for num in w:
#     print(num)


def strStr(haystack, needle):
    # Use Python's built-in find() method
    return haystack.find(needle)
print(strStr("sadbutsad","sad"))