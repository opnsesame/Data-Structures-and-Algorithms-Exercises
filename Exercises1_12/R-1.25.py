#Write a short Python function that takes a string s, representing a
#sentence, and return a copy of the string with all punctuation removed.
s = input("please, input  .a sentence ?")
def removePun(s):
    for char in (",.?'/;:"):
        s = s.replace(char,"")
    return s
print(removePun(s))
