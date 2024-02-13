name = "Priyanshu"
age = 29
gender = "Male"

print(name)
print(age)
print(gender)

print(name, age, gender)

print("My name is", name)
print("My age is", age)
print("My gender is", gender)
# To print it in one line - Method 1:
print("My name is", name, "my age is", age, "my gender is", gender)
# To print using fstrings(F-Strings):
print(f"My name is {name}")
print(f"My age is {age}")
print(f"My gender is {gender}")
print(f"My name is {name} and my age is {age}, my gender is {gender}")

# Print: name = Priyanshu
print(f"name = {name}")  # Good for debugging
# Shortcut:
print(
    f"{name = }"
)  # Good for debugging. Ye waala zaada behtar hai, to debug, because it also shows the data-type.
print(f"{name, age = }")  # Ye tuple dega
print(f"{name =} {age = }")
