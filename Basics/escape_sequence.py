# Escape Sequence - always comes in " "

"""
\n -> New Line
\t -> Tab
\\ -> \
\" -> "
\' -> '
\b -> backspace

"""
print("My name is Priyanshu. \nMy age is 29. \nMale")
print("My name is Priya\\nshu")

# Output: My name is "Priyanshu"
print("My name is \"Priyanshu\"")
print('My name is "Priyanshu"')

# Output: a"\\"xyz'"\
print('a"\\\\"xyz\'"\\')

# Output: a"\/\"xyz'"\
print('a"\\/\\"xyz\'"\\')