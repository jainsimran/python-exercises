#Strings are Arrays

str = "happy"
#loop 
for x in str:
    print(x)

# to check length
print(len(str))

# to check if a certain phrase or character is present in a string, 

if "app" in str:
    print("app is present in " + str)

if "tap" not in str:
    print("tap is not present in " + str)

#Slicing Strings
print(str[-4:-2]) # it will not include -2 postion. 

#replace string 
print(str.replace('h', 'D'))

# combine string and number
text = "I will become {} old on {} March 2021!"
print(text.format(25, 13))

text2 = "I like to order {1} number of items, my budget is ${0} and I want to till {2}-{3}-{4}" # use index number to arrange it in order you wish
print(text2.format(500, 10, 10, 10, 2021))

#using "" inside string 
print("I like to visit \"Mexico\", But love staying in \"Canada\". ")