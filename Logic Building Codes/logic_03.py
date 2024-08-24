# WAP to find unique numbers in an array and count their occurance.
# WAP to find unique words in a sentence and count their occurance.
# ******WAP to find unique characters in a sentence and count their occurance.
import pandas as pd
l1=[12,56,89,75,12,43,56,89,12,78]
s1=set()
count=0

for i in l1:
    s1.add(i)

print(s1)
count=pd.Series(l1).value_counts()
print("Element Count")
print(count)
