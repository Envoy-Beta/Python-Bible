# Combining variables, lists, if statements, logic and data structures and for loops into only two lines
even_numbers = [x for x in range(101) if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in range(101) if x % 2 != 0]
print(odd_numbers)

# List of Lists
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
answers = [[w.upper(), w.lower(), len(w)] for w in words]
print(answers)