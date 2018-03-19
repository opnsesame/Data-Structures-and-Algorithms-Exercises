#Write a Python program that repeatedly reads lines from standard input
#until an EOFError is raised, and then output those lines in reverse 
#order (a user can indicate end of input by typing ctrl-D)
print("Enter/Paste your content. Ctrl-D to end input.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
for i in range(len(contents)):
    print(contents[0-i-1])
