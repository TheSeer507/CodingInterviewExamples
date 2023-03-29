<<<<<<< HEAD
#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#Best Practice Example

def to_camel_case(text):
    removed = text.replace('-',' ').replace('_',' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])

#2nd Best practice example  One liner
def second_to_camel_case(word):
    return word[:1] + word.title()[1:].replace('_','').replace('-','')

text = "the-stealth-warrior"
word = "The_Stealth_Warrior"

print(to_camel_case(text))
print(second_to_camel_case(word))
=======
#Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#Best Practice Example

def to_camel_case(text):
    removed = text.replace('-',' ').replace('_',' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])

#2nd Best practice example  One liner
def second_to_camel_case(word):
    return word[:1] + word.title()[1:].replace('_','').replace('-','')

text = "the-stealth-warrior"
word = "The_Stealth_Warrior"

print(to_camel_case(text))
print(second_to_camel_case(word))
>>>>>>> 1f12b88269c68e4e1b02aa59849a43f9ea5c59a0
