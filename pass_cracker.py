
from itertools import combinations_with_replacement as cwr

list = list(cwr('0123456789',8))
'''
list(cwr('', 3)) -> este comando cwr (combinations_with_replacement) dentro das aspas você passa a informação
de quais caracteres você deseja que ele veja as combinações.
o valor int ou numero inteiro do lado direito da virgula do parenteses significa o numero maximo de 
caracteres EX: cwr('abc',3) este codigo vai te retornar todas as combinações possiveis de 3 digitos/caracteres
de abc ou seja: aaa, aab, aac, ....
'''



for tentativa in list:
    print(tentativa)






