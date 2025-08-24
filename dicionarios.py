"""

import pprint

spam = ['eggs', 'bacon', 'milk']
animals = ['cat', 'dog']
#print(spam == animals)

dic_spam = {'name': 'andre', 'mood': 'sad', 'age': '38'}
dic_animals = {'name': 'andre', 'age': '28', 'mood': 'sad'}
list_test = [dic_spam, dic_animals]
dic_test = {'list1': dic_spam, 'list2': dic_animals}
#dic_test['list1']['name'] = input("Coloque um valor qualquer aqui: ")
print(dic_spam)
dic_spam.setdefault('origin','Osasco')
print(dic_spam)

dic_spam.setdefault('origin', 'SP')
pprint.pprint(dic_spam)

"""
import pprint

message = 'Vou e deixo o que ficar pra trás, nosso brever amor se despedira'
dic_count = {}

for c in message:
    dic_count.setdefault(c, 0)
    dic_count[c] = dic_count[c]+1

pprint.pprint(dic_count)