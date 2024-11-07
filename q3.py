sentence = input("Enter the String: ")
vowels = ('a','e','i','o','u','A','E','I','O','U')
vowel = 0
consonants = 0
longest_word = ''
for i in sentence:
    if i == ' ':
        continue
    elif i in vowels:
        vowel +=1                                                                                                             
    else:
        consonants +=1

words = sentence.split()
for word in words:
    if len(word)>len(longest_word):
        longest_word = word
        
reverse_sentence = sentence[::-1]

print(f"Number of vowels: {vowel}")
print(f"Number of consonants: {consonants}")
print(f"Longest word: {longest_word}")
print(f"Reversed sentence: {reverse_sentence}")







