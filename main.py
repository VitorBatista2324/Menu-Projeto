def exibir_menu():
    print("\nMenu Principal:")
    print("1. Registre-se")
    print("2. Login")
    print("3. Admin")
    print("4. Leitor")
    print("5. Inserir notícias")
    print("6. Buscar notícias")
    print("7. Excluir notícias")
    print("8. Sair")

while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1-8): ")

    if escolha == '1':
        print("Você selecionou 'Registrar'.")
        # Implemente a lógica para exibir as últimas notícias aqui.
    elif escolha == '2':
        print("Você selecionou 'Login'.")
        # Implemente a lógica para exibir as categorias de notícias aqui.
    elif escolha == '3':
        print("Você selecionou 'Admin'.")
        # Implemente a lógica para permitir ao usuário realizar uma busca.
    elif escolha == '4':
        print("Você selecionou 'Leitor'.")
        # Implemente a lógica para gerenciar notificações.
    elif escolha == '5':
        print("Você selecionou 'Inserir notícias'.")
        # Implemente a lógica para a gestão da conta do usuário.
    elif escolha == '6':
        print("Você selecionou 'Buscar notícias'.")
        # Exiba informações sobre a equipe e a missão do projeto.
    elif escolha == '7':
        print("Você selecionou 'Excluir Notícias'.")
        # Implemente a lógica para entrar em contato com a equipe.
    elif escolha == '8':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida (1-8).")
