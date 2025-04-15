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

# Ex
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)

# Ex
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')

##########################################################
# Joining Strings

# Syntax:
'delimiter'.join(list_you_want_to_join)

# Ex
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)

# Ex
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)

