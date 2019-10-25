import hashlib

verify = True
cont = 0
with open('cad.txt', 'w+') as file:
    file.write("usuario;senha\n")
    while verify:
        cont +=1
        usuario = input("Digite o usuario\n")
        senha = input("Digite a senha\n")
        while len(senha) > 20:
            senha = input("Digite a senha, com no maximo 4 caracteres\n")
        hashi = hashlib.md5(senha.encode()).hexdigest()
        file.write((usuario + ";" + hashi + '\n'))
        teste = input("Deseja sair ? Digite 1 para continuar 2 para sair\n")
        if teste == "1":
            verify = True
        else:
            break
print("Usuarios cadastrados com sucesso!!!")

# user = input("senha")
# hashi = hashlib.md5(user.encode()).hexdigest()
# print(hashi)
#
