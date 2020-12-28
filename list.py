#replacing the value using index 
list = ['Apple', 'Banana', 'Watermelon', 'HoneyDew', 'Apple']
list[1:2] = ["Kiwi", "Mango"]
print(list)

#adding item in list 
list.append("Banana")
list.append("Watermelon")
print(list)

# looping list 
for x in list:
    if x == 'Mango':
        print(x)


# find Kiwi index

# for x in list: 
#     if x == "Apple":
#         print(x.index)

# print fruits which have 'a' character
newList = [x for x in list if "a" in x]
print(newList)

# print only apples from list 
appleList = [x for x in list if x == "Apple"]
print(appleList)

# print only first 3 items in list
first3Items = [x for x in range(3)]
print(first3Items)

# reverse the duplicate of list 
reverseList = list.copy()
reverseList.sort(reverse = True)
print(reverseList)
print(list)

# add reverse + list
list.extend(reverseList)
print(list)

totalLen = "total number of items in list is " + str(len(list)) #converted int to string to add both
print(totalLen)