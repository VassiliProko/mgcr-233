word1 = input()
word2 = input()

count = 0
#count of matched characters

for x in range(len(word1)):
    if word1[x] == word2[x]:
        count += 1

print(f"{count} characters match")