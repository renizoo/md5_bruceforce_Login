import hashlib
from random import randint

senha = input("Senha: \n")

hashi = hashlib.md5(senha.encode()).hexdigest()

print("cripto1: " + hashi)

hashlopp = randint(10, 99)
print(hashlopp)

hashi2 = hashlib.md5(hashi.encode()).hexdigest()

print("cripto2: " + hashi2)
lista = []
lista.append(hashi)
lista.append(hashi2)
print(lista)
print("lista 1: " + lista[0])
i = 1

for i in range(hashlopp):
    hashii = (hashlib.md5(lista[i - 1].encode()).hexdigest())
    print(hashii)
    lista.append(hashii)

#autenticacao

senha2 = input("Digite a senha:\n")

hashi = hashlib.md5(senha2.encode()).hexdigest()

hashi2 = hashlib.md5(hashi.encode()).hexdigest()

lista2 = []
lista2.append(hashi)
lista2.append(hashi2)
print(lista2)

i = 1

for i in range(hashlopp):
    hashii = (hashlib.md5(lista2[i - 1].encode()).hexdigest())
    print(hashii)
    lista2.append(hashii)

if lista[-1] == lista2[-1]:
    print("Logado")
else:
    print("Senhas invalidas")
