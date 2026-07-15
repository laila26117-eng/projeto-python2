candidatos=[]

selecao=input("Você quer participar da seleção de estágio? ")

if selecao.lower()=="sim":
    for i in range(15):
        nomes=input("Digite seu nome : ")
        candidatos.append(nomes)

elif selecao.lower()=="não":
    print("Saindo do programa")
    
print("Os candidatos a vaga são:", candidatos)