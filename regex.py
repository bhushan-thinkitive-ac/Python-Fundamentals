# Metacharacters
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE
#     to match.
# ()  Enclose a group of REs


import re

pattern = r"[A-Z]+yres"

text = '''
Battle Birds was an American air-war pulp magazine, published by Popular Publications. It was launched at the end of 1932, but did not sell well, and in 1934 the publisher turned it into an air-war hero pulp titled Dusty Ayres and His Battle Birds. Robert Sidney Bowen, an established pulp writer, provided the lead novel each month, and also wrote the short stories that filled out the issue. Bowen's stories were set in the future, with the United States menaced by an Asian empire called the Black Invaders. The change was not successful enough to be extended beyond the initial plan of a year, and Bowen wrote a novel in which, unusually for pulp fiction, Dusty Ayres finally defeated the invaders, to end the series. 
'''
print(re.search(pattern, text))
matches = re.finditer(pattern, text)

for match in matches:
    print(match)
