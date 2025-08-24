def hello(param):
    final = ''
    list_len = len(param)
    print(list_len)
    counter = 1
    for i in param:
        final += i
        print(counter)
        if (counter != list_len):
            final += ", "
        if (counter == list_len-1):
            final += "and "
        counter += 1
    return final

spam = ['a', 'b', 't', 'c']

result = hello(spam)

print(result)
