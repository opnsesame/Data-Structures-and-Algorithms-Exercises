'''
Write a Python program that inputs a document and then outputs a barchart
plot of the frequencies of each alphabet character that appears in
that document.
'''
import numpy as np
import matplotlib.pyplot as plt
import re
import string
from collections import Counter

f = open('t.txt')
str = f.read()
str = re.sub(r'[\n\.\ \?+_0123456789\(\\,!#\[\]\"\=\/\&\*\;\:\-\)\']', '', str)
str = str.lower()
#letter_count = Counter(str)
#letter_count = {k: letter_count.get(k, 0) for k in str}
#print("Frequency count of letter:\n", letter_count)
#print(letter_count.items())
#print(str)
x = np.arange(len(Counter(str)))
plt.xticks(x, Counter(str).keys())
plt.bar(x, Counter(str).values())
plt.show()
