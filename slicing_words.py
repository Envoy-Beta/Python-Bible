# Slicing Words

word = "supercalifragilisticexpialidocious"
word[0]
print(word[0])

print(word[2])


#Slicing Format
# Variable[start:end:step]
word[0:5:1]
print(word[0:5:1]
)

#Print starting from letter "c" up until index 9 and count every element between them
word[5:9:1]
print(word[5:9:1])

# Print every starting from "c"
word[5:]
print(word[5:])

# Print every word, starting from "c"
word[5::2]
print(word[5::2])

# Print every letter up until "l" but not including it
word[:7]

print(word[:7])

# Print "u" with slicing, starting from the end of a word. The first number at the end of a string is represented by the vaule "-1"
word[-2]

print(word[-2])

word.index('cali')

print(word.index('cali'))

# Slice out "cali"
word.index('fragi')

print(word.index('fragi'))

#Use slicing format: variable[start:end:step]
word[word.index("cali"):word.index("fragi")]
