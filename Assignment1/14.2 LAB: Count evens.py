def count_evens(num1, num2, num3, num4, num5):
    count = 0
    for x in [num1, num2, num3, num4, num5]:
        if x % 2 == 0:
            count += 1
    
    return count
    

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    
    result = count_evens(num1, num2, num3, num4, num5)
    print(f'Total evens: { result }')