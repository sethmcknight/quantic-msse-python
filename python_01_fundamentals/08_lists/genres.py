genres = []
genres.append("western")
genres.append("kung fu")
genres.insert(1, "zombie")
genres.append("musical")
genres.insert(2, "scifi")
genres.insert(-1, "biopic")
del genres[3]
genres.remove("scifi")
genres.remove("western")
del_genre = genres.pop(1)
print(f"We deleted {del_genre}s.")
print(genres)

# Lists can contain different data types
mixed_types = [17, "spam", 43.9]

# .remove() removes the first occurrence of a value from the list
nums = [2, 5, 1, 5, 3, 5]
nums.remove(5)
print(nums)

# what does pop do?
test = ["a", "b", "c", "d"]
del test[0]
test.remove("b")
print(test.pop())
print(test)