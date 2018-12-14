# There are 14 types of punctuation marks that are commonly used in 
# English grammar. They are the period, question mark, 
# exclamation point, comma, semicolon, colon, dash, hyphen,
# parentheses, brackets, braces, apostrophe, quotation marks,
# and ellipsis(...).
characters_to_remove = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

our_string = "Is it five o'clock yet?"

# remove punctuation
for indv_char in our_string:
   if indv_char not in characters_to_remove:
       print(indv_char, end='') #print without new line

print('') # just to print a new line at the end