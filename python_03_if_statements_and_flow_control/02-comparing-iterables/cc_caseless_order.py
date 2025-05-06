string1 = input("Enter a string: ")
string2 = input("Enter another string: ")
# Compare the strings in a case-insensitive manner
if string1.lower() < string2.lower():
    print(f"{string1} comes before {string2} in case-insensitive order.")
elif string1.lower() > string2.lower():
    print(f"{string1} comes after {string2} in case-insensitive order.")
else:
    print(f"{string1} and {string2} are equal in case-insensitive order.")
# Compare the strings in a case-sensitive manner
if string1 < string2:
    print(f"{string1} comes before {string2} in case-sensitive order.")      
elif string1 > string2:
    print(f"{string1} comes after {string2} in case-sensitive order.")
else:
    print(f"{string1} and {string2} are equal in case-sensitive order.")