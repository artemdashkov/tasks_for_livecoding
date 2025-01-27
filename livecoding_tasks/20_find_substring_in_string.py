"""
12. Поиск подстроки в строке
"""
# way 1
string = "this any string"
sub_string = "any"
print(sub_string in string, "\n")

# way 2
try:
    string.index(sub_string)
    print(f"#2\t sub_string: '{sub_string}' is in string: '{string}'. Index is {string.index(sub_string)}")
except ValueError:
    print(f"#2\t sub_string: '{sub_string}' is NOT in string: '{string}'")
finally:
    print("#2\t Try-except construction is finished\n")

# way 3
try:
    string.find(sub_string)
    print(f"#3\t sub_string: '{sub_string}' is in string: '{string}'. Index is {string.find(sub_string)}")
except ValueError:
    print(f"#3\t sub_string: '{sub_string}' is NOT in string: '{string}'")
finally:
    print("#3\t Try-except construction is finished\n")

# way 4
try:
    string.count(sub_string)
    print(f"#4\t sub_string: '{sub_string}' is in string: '{string}'. Index is {string.count(sub_string)}")
except ValueError:
    print(f"#4\t sub_string: '{sub_string}' is NOT in string: '{string}'")
finally:
    print("#4\t Try-except construction is finished")