email = input("Digite seu email: ")

emailBanco = "plexc@gmail.com"
semhaBanco = "123@"

if (email ==  emailBanco):
    senha = input("Digite sua senha: ")
    if (senha == semhaBanco):
        print("Bem vindo PlexC!")
    else:
        print("Senha incorreta. Tente novamente.")
elif (email != emailBanco):
    print ("Não foi possível encontrar sua Conta do Google.")
        

