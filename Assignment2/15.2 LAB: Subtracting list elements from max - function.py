def get_max_int(nums):
    return max(nums)

    
if __name__ == '__main__':
    nums = []
    while True:
        int_val = int(input())
        if int_val == -1:
            break
        nums.append(int_val)

    max_int = get_max_int(nums)

    for i in nums:
        print(max_int - i)
