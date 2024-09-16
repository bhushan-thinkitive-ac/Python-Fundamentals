# modes to operate file in python

# 'r' for reading the file
# 'w' for writing the file
# 'a' for appending the file


# f = open('yourfile.txt', 'w')
# f.write("Hello world")
####################################
# f = open('yourfile.txt', 'a')
# f.write("Hello world")
# f.close()
#####################################
# with (open('yourfile.txt', 'a')) as f:
#     f.write("Hello world")
#####################################
# f = open('myfile.txt', 'r')
# text = f.read()
# f.close()
# print(text)
######################################

# f = open('yourfile.txt', 'r')

# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# f = open('yourfile.txt', 'w')
# lines = ['My name is bhushan\n', 'My surname is chaudhari\n', 'My age is 24 ']
# f.writelines(lines)
# f.close()
