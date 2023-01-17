#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open ('123.txt') as f:
    some_list = f.read()
new_list = filter(lambda word: 'abc' not in word, some_list)
print(list(new_list))

# some_list = ['hello', 'world', 'hi', 'banana', 'orange', 'abcder', 'ssss', 'abc', 'aaddd']
# new_list = filter(lambda word: 'abc' not in word, some_list)
# print(list(new_list))



