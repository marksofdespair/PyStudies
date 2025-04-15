# Not actual meth sorry
##########################################################
# Formatting Methods
#.lower() returns the string with all lowercase characters.
#.upper() returns the string with all uppercase characters.
#.title() returns the string in title case, which means the first letter of each word is capitalized.

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author)
print(poem_author_fixed)

##########################################################
# Splitting Strings

# .split()
# is performed on a string, takes one argument, and returns a list of 
# Preview: Docs A substring is a sequence of characters that are part of an original string.
# substrings found between the given argument (which in the case of .split() is known as the delimiter). The following syntax should be used:

string_name.split(delimiter)

# If you do not provide an argument for .split() it will default to splitting at spaces.

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

# Ex
line_one = "The sky has given over"

line_one_words = line_one.split()
