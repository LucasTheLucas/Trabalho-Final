'''
Lucas Novaes Dias
'''

alunos = {}

def menu():
    print("1 - Adicionar aluno\n2 - Listar alunos\n3 - Remover aluno\n4 - Procurar aluno\n5 - Listar aprovados\n6 - Listar reprovados\n7 - Procurar pelo nome do aluno\n8 - Média da turma B1\n9 - Média da turma B2\n10 - Média da turma geral\n11 - Diário da turma\n0 - Sair")
    opcao = int(input("Digite sua opção: "))
    return opcao

def Add_Aluno():
    RA = input("Digite o RA do aluno: ")
    nome = ""
    while len(nome) < 3 or len(nome) > 27:
        nome = input("Digite o nome do aluno: ")
    b1 = -1
    b2 = -1
    while b1 > 10 or b1 < 0:
        b1 = int(input("Digite a nota de B1: "))
    while b2 > 10 or b2 < 0:
        b2 = int(input("Digite a nota de B2: "))

    aluno = {"nome":nome,"b1":b1,"b2":b2, "ativo":True}
    alunos[RA] = aluno

def Listar_Alunos():
    tem_aluno = False
    for RA, aluno in alunos.items():
        if aluno["ativo"]:
            print(RA," - ",aluno["nome"])
            tem_aluno = True
    if(tem_aluno == False):
        print("Nenhum aluno encontrado!")

def Remover_aluno():
    RA_informado = input("Digite o RA do aluno: ")
    alunos[RA_informado] = {"nome":"","b1":-1,"b2":-1, "ativo":False}

def Procurar_Aluno():
    RA_informado = input("Digite o RA do aluno: ")
    for RA in alunos:
        if(RA == RA_informado):
            print("Aluno ativo")

def Aprovados():
    print("APROVADOS:")
    for RA in alunos:
        if(alunos[RA]["ativo"]):
            media = (alunos[RA]["b1"] + alunos[RA]["b2"])/2
            if media >= 7:
                print(alunos[RA]["nome"])
    print("")

def Reprovados():
    print("REPROVADOS:")
    for RA in alunos:
        if(alunos[RA]["ativo"]):
            media = (alunos[RA]["b1"] + alunos[RA]["b2"])/2
            if media < 7:
                print(alunos[RA]["nome"])
    print("")

def Procurar_Nome():
    nome = input("Digite o nome do aluno!")
    for RA in alunos:
        if(alunos[RA]["ativo"]):
            if(alunos[RA]["nome"] == nome):
                print("Aluno ativo!")

def Media_B1():
    media = 0
    alunos_final = 0
    for RA in alunos:
        if(alunos[RA]["ativo"]):
            alunos_final += 1
            media += alunos[RA]["b1"]
    return(media/alunos_final)

def Media_B2():
    media = 0
    alunos_final = 0
    for RA in alunos:
        if(alunos[RA]["ativo"]):
            alunos_final += 1
            media += alunos[RA]["b2"]
    return(media/alunos_final)
            
def Media_Total():
    media = 0
    alunos_final = 0
    for RA in alunos:
        if(alunos[RA]["ativo"]):
            alunos_final += 2
            media += alunos[RA]["b1"]
            media += alunos[RA]["b2"]
    media = media/alunos_final
    return(media)

def Diario():
    print("-------------------------------------------")
    print("Diario da turma:")
    print("-------------------------------------------")
    print("RA    Nome        B1   B2   Media")
    for RA in alunos:
        if(alunos[RA]["ativo"]):
            print(f"{RA}     {alunos[RA]['nome']}       {alunos[RA]['b1']}   {alunos[RA]['b2']}   {(alunos[RA]['b1']+alunos[RA]['b2'])/2}")
    
    print(f"Media da Turma     {Media_B1()} {Media_B2()} {Media_Total()}")

while True:
    opcao = menu()
    match opcao:
        case 1:
            Add_Aluno()

        case 2:
            Listar_Alunos()

        case 3:
            Remover_aluno()

        case 4:
            Procurar_Aluno()

        case 5:
            Aprovados()
        
        case 6: 
            Reprovados()

        case 7:
            Procurar_Nome()

        case 8:
            print("A média em B1 da turma foi de ",Media_B1())

        case 9:
            print("A média em B2 da turma foi de ",Media_B2())

        case 10:
            print("A média da turma foi de: ",Media_Total())

        case 11: 
            Diario()

        case 0:
            break
        
    