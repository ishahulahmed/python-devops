sample_str = "This is a sample string"
sample_str_list = list(sample_str)
print(sample_str_list)

sample_str_tuple = tuple(sample_str)
print(sample_str_tuple)

# Accept input from a user
user_input = input("Enter a number:")
print(user_input, type(user_input))

# Enter a number:33
# 33 <class 'str'>

# add_10 = user_input + 10
# print(add_10)
# TypeError: can only concatenate str (not "int") to str