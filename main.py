import math
try:
    num_1 = int(input("num 1 --> "))
    num_2 = int(input("num 1 --> "))
    num_2 += 1
    for i in range(1, 11):
        for j in range(num_1, num_2):
            print(i, '*', j, '=', i * j, end='\t\t')
        print()
except Exception as ex:
    print(f"error information:{ex}")
finally:
    print("exit")