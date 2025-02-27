word1 = input()
word2 = input()

count = 0
#count of matched characters

for x in range(min(len(word1), len(word2))):
    if word1[x] == word2[x]:
        count += 1

if count == 1:
    print(f"{count} character matches")
else:
    print(f"{count} characters match")