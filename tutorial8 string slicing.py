### STRING SLICING ###
mystr="mdharunrashid"
print(len(mystr))
print(mystr[5])
print(mystr[0:5:2])
'''
STRINGS ---->IMMUTABLE
let the string, a="mdharunrashid"
suppose i want to INDEX 'h' from the string.To do this we need to know the index position of 'h'. Index position starts with 0.
syntax for indexing.....print(variable[index position])

Similarly we use SLICING to get a part of the string.
syntax for slicing....print(variable[start i position:stop i position(+1):step size])

a="mdharunrashid"
print(a[0:5:2])
print(a[::-1]-----syntax to print the string in reverse order

OUTPUT

 mhr
 dihsarnurahdm
'''

''' a="mdharunrashid"
    print(a[0:5:2])
    print(a[::-1])
'''
'''
variable.isalnum()----checks whether the string is alphanumeric or not. SPACE is not count as alphanumeric
variable.isalpha()----checks whether the string is alphabetic or not.
variable.endswith("word")....checks whether the word written in () present at the end of the string or not.
variable.count('letter')...counts the occurrence of the letter in the ()
variable.capitalize()....Capitalize the first letter of the string
variable.find('harun')....finds the index position in the string from which the word in () starts
variable.lower()... converts the string into lower case
variable.upper()....converts the string into upper case


mystr="md harun rashid"
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith('rashid'))
print(mystr.count('a'))
print(mystr.capitalize())
print(mystr.find('harun'))
print(mystr.upper())

OUTPUT

False
False
True
2
Md harun rashid
3
MD HARUN RASHID

'''










