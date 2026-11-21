# In this i will tell you how to solve tuple to dict conversion

tup = (1,2,[43,32,65],"a","b","c",(32,21,43))

val = {}
char = ord("a") # ord("any_charcther") it will give us its ascii value

for i in tup:
    val[chr(char)] = i # This line will take 97 which was ascii of a and convert it into chr which was small a
    # chr keyword is used for type conversional of int to chr
    char += 1 # Just adding one in char so it become 98 that was b

print(val)