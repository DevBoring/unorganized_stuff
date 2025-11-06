def find_digit_length(n):
    remaining = n
    length = 1
    while True:
        if length == 1:
            count = 3
        elif length % 2 == 0:
            count = 4 * (5 ** ((length - 2) // 2))
        else:
            count = 4 * (5 ** ((length - 3) // 2)) * 3
        
        if remaining <= count:
            return length
        remaining -= count
        length += 1

n = int(input().strip())
print(find_digit_length(n))