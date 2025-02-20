num_int = int(input())

values = []

for x in range(num_int):
    values.append(int(input()))

threshold = int(input())

for x in range(num_int):
    if values[x] <= threshold:
        print(f"{values[x]},", end="")

print()


