"""
Input: list of nums i.e.[2, 3, 4, 5] - nums represent a number of coins
Output: digit representing highest number of coins that can be collected, adjecent indexes cannot be used
Algorithm: greedy   
Loop through the list adding all the evens and compare it to all the odds.
"""

def max_coins(list):


    l = 0
    r = 2
    sum = 0
    max_sum = 0

    while r < len(list):
        sum = list[l] + list[r]
        if sum > max_sum:
            max_sum  = sum
        print(f'l: {l}\nvalue of l: {list[l]}\nr: {r}\nvalue of r: {list[r]}\nsum: {list[l] + list[r]}\nmax_sum: {max_sum}')
        print('_____________________________')
        r += 1
    
    print('-------------------------------------')

    l = 3
    r = 1
    while l < len(list):
        sum = list[l] + list[r]
        if sum > max_sum:
            max_sum  = sum
        print(f'l: {l}\nvalue of l: {list[l]}\nr: {r}\nvalue of r: {list[r]}\nsum: {list[l] + list[r]}\nmax_sum: {max_sum}')
        print('_____________________________')
        l += 1

    print(max_sum)
    # even_count = sum([list[i] for i in range(0, len(list)) if i % 2 == 0])
    # print(even_count)

    # odd_count = sum([list[i] for i in range(0, len(list)) if i % 2 == 1])
    # print(odd_count)

print(max_coins([2, 3, 2, 4, 5]))