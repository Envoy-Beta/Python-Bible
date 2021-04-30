#Get sentence from user

original = input("Please, enter a sentence: ").strip().lower()

#Split sentence into individual words

words = original.split()

#Loop through each word and convert them to Pig Latin

new_words = []

for word in words:
    # if words starts with a vowel, add 'yay' to word
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        # if word starts with a consonant, move firt consonant to the end, add 'ay'
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break 
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:] 
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

#Put words back together, into a sentence

output = " ".join(new_words)

#Output the final string

print(output)