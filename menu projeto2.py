noticias = []
admins = {}
users = {}
usuario_logado = None

while True:
    print("\nMenu Geral")
    print("1. Cadastrar Administrador")
    print("2. Login")
    print("3. Cadastrar Usuário")
    print("0. Sair")
    choice = input("Escolha uma opção: ")

    if choice == '1':
        username = input("Digite o nome de usuário do administrador: ")
        password = input("Digite a senha do administrador: ")
        admins[username] = password
        print("Administrador cadastrado com sucesso.")
    elif choice == '2':
        username = input("Nome de usuário: ")
        password = input("Senha: ")

        if username in admins and admins[username] == password:
            print("Login bem-sucedido como administrador.")
            usuario_logado = username
        elif username in users and users[username] == password:
            print("Login bem-sucedido como usuário.")
            usuario_logado = username
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")
    elif choice == '3':
        username = input("Digite o nome de usuário do usuário: ")
        password = input("Digite a senha do usuário: ")
        users[username] = password
        print("Usuário cadastrado com sucesso.")
    elif choice == '0':
        break
    else:
        print("Opção inválida. Tente novamente.")

    while usuario_logado:
        if usuario_logado in admins:
            print("\nMenu do Administrador")
            print("1. Inserir Notícia")
            print("2. Listar Notícias")
            print("3. Excluir Notícia")
            print("4. Editar Notícia")
            print("5. Buscar Notícia")
            print("6. Logout")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                titulo = input("Título da notícia: ")
                conteudo = input("Conteúdo da notícia: ")
                noticias.append({"titulo": titulo, "conteúdo": conteudo, "autor": usuario_logado, "comentarios": [], "curtidas": 0})
                print("Notícia inserida com sucesso.")
            elif choice == '2':
                print("\nLista de Notícias:")
                for i, noticia in enumerate(noticias):
                    print(f"{i + 1}. Título: {noticia['titulo']}")
                    print(f"   Autor: {noticia['autor']}")
                    print(f"   Curtidas: {noticia['curtidas']}")
                    print("   Comentários:")
                    for comentario in noticia['comentarios']:
                        print(f"       {comentario}")
                if not noticias:
                    print("Nenhuma notícia disponível.")
            elif choice == '3':
                titulo = input("Digite o título da notícia a ser excluída: ")
                for noticia in noticias:
                    if noticia['titulo'] == titulo:
                        noticias.remove(noticia)
                        print(f"Notícia '{titulo}' excluída com sucesso.")
                        break
                else:
                    print(f"Notícia '{titulo}' não encontrada.")
            elif choice == '4':
                titulo = input("Digite o título da notícia a ser editada: ")
                for noticia in noticias:
                    if noticia['titulo'] == titulo and noticia['autor'] == usuario_logado:
                        novo_conteudo = input("Novo conteúdo da notícia: ")
                        noticia['conteúdo'] = novo_conteudo
                        print("Notícia editada com sucesso.")
                        break
                else:
                    print(f"Notícia '{titulo}' não encontrada ou você não tem permissão para editá-la.")
            elif choice == '5':
                titulo = input("Digite o título da notícia que deseja buscar: ")
                for noticia in noticias:
                    if noticia['titulo'] == titulo:
                        print(f"Título: {noticia['titulo']}")
                        print(f"Conteúdo: {noticia['conteúdo']}")
                        print(f"Autor: {noticia['autor']}")
                        break
                else:
                    print(f"Notícia '{titulo}' não encontrada.")
            elif choice == '6':
                usuario_logado = None
        elif usuario_logado in users:
            print("\nMenu do Usuário")
            print("1. Listar Notícias")
            print("2. Buscar Notícia")
            print("3. Comentar Notícia")
            print("4. Curtir Notícia")
            print("5. Logout")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                print("\nLista de Notícias:")
                if noticias:
                    for i, noticia in enumerate(noticias):
                        print(f"{i + 1}. Título: {noticia['titulo']}")
                        print(f"   Autor: {noticia['autor']}")
                        print(f"   Curtidas: {noticia['curtidas']}")
                        print("   Comentários:")
                        for comentario in noticia['comentarios']:
                            print(f"       {comentario}")
                else:
                    print("Nenhuma notícia disponível.")
            elif choice == '2':
                titulo = input("Digite o título da notícia que deseja buscar: ")
                for noticia in noticias:
                    if noticia['titulo'] == titulo:
                        print(f"Título: {noticia['titulo']}")
                        print(f"Conteúdo: {noticia['conteúdo']}")
                        print(f"Autor: {noticia['autor']}")
                        break
                else:
                    print(f"Notícia '{titulo}' não encontrada.")
            elif choice == '3':
                titulo = input("Digite o título da notícia para comentar: ")
                for noticia in noticias:
                    if noticia['titulo'] == titulo:
                        comentario = input("Digite seu comentário: ")
                        noticia['comentarios'].append(f"{usuario_logado}: {comentario}")
                        print("Comentário adicionado com sucesso.")
                        break
                else:
                    print(f"Notícia '{titulo}' não encontrada.")
            elif choice == '4':
                titulo = input("Digite o título da notícia para curtir: ")
                for noticia in noticias:
                    if noticia['titulo'] == titulo:
                        noticia['curtidas'] += 1
                        print(f"Você curtiu a notícia '{titulo}'.")
                        break
                else:
                    print(f"Notícia '{titulo}' não encontrada.")
            elif choice == '5':
                usuario_logado = None
