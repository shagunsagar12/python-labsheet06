str1 = "listen"
str2 = "silent"

if set(str1) == set(str2) and sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")