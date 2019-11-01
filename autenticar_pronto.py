#usr/bin/python
import time
import itertools, string
import hashlib
import sys
# import signal
import threading

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):

        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

verify = True

# comeco abrindo o arquivo

with open("cad.txt", "r+") as file:
    lines = file.readlines()

# print("Usuario cadastrados:\n")
# print(lines)
# mostrando as senhas cadastradas
for j in range(len(lines) - 1):
    line = lines[j+1].split(";", 1)
    print("Senha do usuario "+line[0]+": "+line[1].rstrip("\n"))
# loop para decisao


# comeco abrindo o arquivo DIFICIL

with open("cadDificultar.txt", "r+") as file:
    lines2 = file.readlines()

print("\n")
# print("Usuario cadastrados:\n")
# print(lines)
# mostrando as senhas cadastradas
for j in range(len(lines) - 1):
    line2 = lines2[j+1].split(";", 2)
    print("Senha do usuario Dificil "+line2[0]+": "+line2[1])


while verify:

    escolha = input("""    ______________________
    Digite 1 para | ENTRAR NORMAL
    Digite 2 para | BRUTEFORCE NORMAL
    Digite 3 para | ENTRAR DIFICIL 
    Digite 4 para | BRUTEFORCE DIFICIL
    __________________________\n""")
    if escolha == "1":
        for i in range(len(lines) - 1):
            test = 0
            login = input("Digite o usuario:\n")
            senha = input("Digite a senha:\n")
            hashi = hashlib.md5(senha.encode()).hexdigest()

            for j in range(len(lines) - 1):
                line = lines[j+1].split(";", 1)
                # print(line)
                # print(line[1])
                if line[0] == login and line[1].rstrip("\n") == hashi:
                    print("Senha digitada em md5: " + hashi)
                    print("Senha cadastrada em md5: "+line[1])
                    test = 1
            if test == 1:
                print("Usuario logado com sucesso\n")
                break
            else:
                print("Usuario ou senha incorretos, tente novamente\n")
                break

    if escolha == "2":

        print("Welcome to quebrando a senha!")
        comeco = time.time()

        while True:
            for j in range(len(lines) - 1):
                loop_control = False
                line = lines[j+1].split(";", 1)
                inputt = (line[1].rstrip("\n"))
                chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
                print(chrs)

                print("[+] Start Time: ", time.strftime('%H:%M:%S'))
                start_time = time.time()
                # t = threading.Thread(target=animate)
                #             # t.start()
                total_pass_try = 0
                for n in range(1, 31 + 1):
                    # print("teste")
                    characterstart_time = time.time()
                    print("\n[!] I'm at ", n, "-character")

                    for xs in itertools.product(chrs, repeat=n):
                        saved = ''.join(xs)
                        stringg = saved
                        m = hashlib.md5()
                        m.update(bytes(saved, encoding='utf-8'))
                        total_pass_try += 1
                        if m.hexdigest() == inputt:
                            # time.sleep(10)

                            print("\n[!] found ", stringg)
                            print("\n[-] End Time: ", time.strftime('%H:%M:%S'))
                            print("\n[-] Total Keyword attempted: ", total_pass_try)
                            print("\n---Md5 cracked at %s seconds ---" % (time.time() - start_time))
                            # globall = True
                            loop_control = True
                            break
                            # sys.exit("Thank You !")

                    print("\n[!]", n, "-character finished in %s seconds ---" % (time.time() - characterstart_time))
                    if loop_control:
                        break
            print("\n\nTempo para quebrar {0} hashs: {1}".format(len(lines) - 1, time.time() - comeco))
            break
    # nao esta funcionando ainda
    if escolha == "3":
        for i in range(len(lines2) - 1):
            test = 0
            login = input("Digite o usuario:\n")
            senha = input("Digite a senha:\n")
            hashi = hashlib.md5(senha.encode()).hexdigest()
            hashi2 = hashlib.md5(hashi.encode()).hexdigest()
            lista = []
            listaHash = []
            lista.append(hashi)
            lista.append(hashi2)
            j = 1
            print(lines2)

            for i in range(len(lines2)):
                listaHash.append(line2[i][2].rstrip("\n"))

            print(listaHash)
            #
            # for i in range(len(listaHash)-1):
            #     hashii = (hashlib.md5(lista[i - 1].encode()).hexdigest())
            #     print(hashii)
            #     lista.append(hashii)
            #
            # for i in range(len(listaHash)-1):
            #     hashii = (hashlib.md5(lista[i - 1].encode()).hexdigest())
            #     print(hashii)
            #     lista.append(hashii)
            #
            # if lista[-1] == lista2[-1]:
            #     print("Logado")
            #     print(lista[-1] + "\n" + lista[-1])
            # else:
            #     print("Senhas invalidas")

    if escolha == "4":

        print("Welcome to quebrando a senha!")
        comeco = time.time()

        while True:
            for j in range(len(lines2) - 1):
                loop_control = False
                line = lines2[j+1].split(";", 2)
                inputt = ("Senha "+str(j+1)+": "+line[1].rstrip("\n"))
                print(inputt)
                chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
                print(chrs)

                print("[+] Start Time: ", time.strftime('%H:%M:%S'))
                start_time = time.time()
                # t = threading.Thread(target=animate)
                #             # t.start()
                total_pass_try = 0
                for n in range(1, 31 + 1):
                    # print("teste")
                    characterstart_time = time.time()
                    print("\n[!] I'm at ", n, "-character")

                    for xs in itertools.product(chrs, repeat=n):
                        saved = ''.join(xs)
                        stringg = saved
                        m = hashlib.md5()
                        m.update(bytes(saved, encoding='utf-8'))
                        total_pass_try += 1
                        if m.hexdigest() == inputt:
                            # time.sleep(10)

                            print("\n[!] found ", stringg)
                            print("\n[-] End Time: ", time.strftime('%H:%M:%S'))
                            print("\n[-] Total Keyword attempted: ", total_pass_try)
                            print("\n---Md5 cracked at %s seconds ---" % (time.time() - start_time))
                            # globall = True
                            loop_control = True
                            break
                            # sys.exit("Thank You !")

                    print("\n[!]", n, "-character finished in %s seconds ---" % (time.time() - characterstart_time))
                    if loop_control:
                        break
            print("\n\nTempo para quebrar {0} hashs: {1}".format(len(lines) - 1, time.time() - comeco))
            break
