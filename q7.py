lis1 = []
lis2 = []
word1 = input('Enter the word1: ')
word2 = input('Enter the word2: ')
for i in word1:
    if i == ' ':
        continue
    else:
        lis1.append(i)
for j in word2:
    if j == ' ':
        continue
    else:
        lis2.append(j)
lis1 = sorted((lis1))
lis2 = sorted((lis2))

if lis1  == lis2:
    print('The words are anagrams')
else:
    print('The words are not anagrams')



