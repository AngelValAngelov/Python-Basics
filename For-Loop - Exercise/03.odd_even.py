import sys

n = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for number in range(1 , n + 1):
    num = float(input())
    if number % 2 == 0:
        even_sum = even_sum + num
        if num > even_max:
            even_max = num
        if num < even_min:
            even_min = num
    else:
        odd_sum = odd_sum + num
        if num > odd_max:
            odd_max = num
        if num < odd_min:
            odd_min = num
if odd_sum !=0:
    print(f"OddSum={odd_sum:.2f},")
else:
    print(f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")
if even_sum != 0:
    print(f"EvenSum={even_sum:.2f},")
else:
    print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")

