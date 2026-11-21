import os



# 1. Remove duplicates from a list without using set().
# Tests list traversal and duplicate checking.

lis = [1,2,3,2,3,4,5]
new_list = []
for i in lis:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# 2. Find the second-largest number in a list.
# Tests sorting and iteration.

sort_list = sorted(lis)
print(sort_list[-2])

# if have duplicate values like [10,20,30,30] then last and second last number are same it throws error
# Then you should use
lis_2 = [10,20,30,30,40]
sort_list_2 = sorted(set(lis_2))
print(sort_list_2[-2])

# 3. Count the frequency of each character in a string using a dictionary.
# Tests dictionary operations.

def countFrequencyOfACharacter(n):
    val = {}
    for i in n:
        if i not in val:
            val[i] = 0
        val[i]+=1
    return val

charchter = "aabbcccddeeef"
print(countFrequencyOfACharacter(charchter))

# 4. Find common elements between two lists using sets.
# Tests set intersection.

lis_one = [1,2,3,4,5]
lis_two = [4,5,6,7,8]

print(set(lis_one).intersection(set(lis_two)))

# 5. Check whether two strings are anagrams.
# Tests dictionaries or sorting.

string_one = "abc"
string_two = "bca"

dic_string_one = {}
dic_string_two = {}

for i in string_one:
    if i not in dic_string_one:
        dic_string_one[i] = 0
    dic_string_one[i] +=1

for i in string_two:
    if i not in dic_string_two:
        dic_string_two[i] = 0
    dic_string_two[i] +=1

print(dic_string_one == dic_string_two)



# 6. Reverse a list without using reverse() or slicing.
# Tests loops and indexing.

numbers = [1,2,3,4,5,6]
char = []
for i in numbers:
    char.insert(0,i)
print(char)



# 7. Find the first non-repeating character in a string.
# Tests dictionary frequency counting.

# Using For Loop
string_four = "aaabccdeefgg"
non_repeating = {}

for i in string_four:
    if i not in non_repeating:
        non_repeating[i] = 0
    non_repeating[i] += 1

for i in non_repeating:
    if non_repeating[i] == 1:
        print(i)
        break


# Using Dictinoaries
dict_copy = {}
for i in string_four:
    if i not in dict_copy:
        dict_copy[i] = 0
    dict_copy[i] += 1
sorted_data = {k: dict_copy[k] for k in sorted(dict_copy, key=dict_copy.get)}
print(min(sorted_data, key=sorted_data.get))

# if want all key of minimum value 1 then

min_val = min(sorted_data.values())
min_keys = [k for k, v in sorted_data.items() if v == min_val]
print(min_keys)


# 8. Merge two dictionaries.
# Tests dictionary update and unpacking.
dict1 = {"name": "Ratikant", "age": 25, "city": "Pune"}
dict2 = {"age": 26, "language": "Python", "experience": "3.5 years"}

# for index , (key , value ) in enumerate(dict1.items() , start=1):
#     print(f"{index} => {key} & {value}")

for j in dict2:
    if j not in dict1:
        dict1[j] = dict2[j]
    if j in dict1:
        dict1[j] = dict2[j]

print()
print(dict1)

# another Way
dict3 = {}
for i in dict1:
    if i not in dict3:
        dict3[i] = dict1[i]
for i in dict2:
    if i not in dict3:
        dict3[i] = dict2[i]
print(dict3)

         