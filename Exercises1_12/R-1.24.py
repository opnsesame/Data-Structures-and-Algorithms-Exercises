#Write a short Python function that counts the number of vowels
#in a given character string
s = 'aeiou123aaeiouUA'
s = s.lower()
def countVowel(s):
    count = 0
    for letter in s:
        if letter in 'aeiou':
            count += 1
    return count
print(countVowel(s))
