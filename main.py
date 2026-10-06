from time import sleep


class SistemaFinanceiro:
    def __init__(self):
        self.receitas = []
        self.despesas = []

    def cadastrar_receita(self):
        valor = float(input("Digite o valor da receita : "))
        descricao = input("Digite a descrição da receita : ")
        self.receitas.append({"valor": valor, "descricao": descricao})
        print(
            "Receita cadastrada com sucesso!", "Deseja cadastrar outra receita? (s/n)"
        )
        pergunta = input().lower()
        if pergunta == "s":
            self.cadastrar_receita()
        else:
            menu()

    def cadastrar_despesa(self):
        try:
            valor = float(input("Digite o valor da despesa : "))
        except ValueError:
            print("Valor inválido, tente novamente. \n")
            sleep(3)
            self.cadastrar_despesa()
        descricao = input("Digite a descrição da despesa : ")
        print(
            "Categorias disponíveis:\n Alimentação\n Transporte\n Moradia\n Lazer\n Saúde\n Educação\n Outros"
        )
        if not self.receitas:
            print(
                "Não há receitas cadastradas. Cadastre uma receita antes de cadastrar uma despesa.",
                "Deseja cadastrar uma receita agora? (s/n)",
            )
            pergunta = input().lower()
            if pergunta == "s":
                self.cadastrar_receita()
            else:
                return
        try:
            categoria = input("Escolha a categoria da despesa : ")
            if categoria not in [
                "Alimentação",
                "Transporte",
                "Moradia",
                "Lazer",
                "Saúde",
                "Educação",
                "Outros",
            ]:
                raise ValueError("Categoria inválida")
        except ValueError:
            print("Opção inválida, tente novamente. \n")
            sleep(3)
            self.cadastrar_despesa()
        else:
            self.despesas.append(
                {"valor": valor, "descricao": descricao, "categoria": categoria}
            )
        print(
            "Despesa cadastrada com sucesso!", "Deseja cadastrar outra despesa? (s/n)"
        )
        pergunta = input().lower()
        if pergunta == "s":
            self.cadastrar_despesa()
        else:
            menu()

    def calcular_saldo(self):
        total_receitas = sum(receita["valor"] for receita in self.receitas)
        print(f"Total de receitas: {total_receitas}")
        total_despesas = sum(despesa["valor"] for despesa in self.despesas)
        print(f"Total de despesas: {total_despesas}")
        saldo = total_receitas - total_despesas
        if saldo < 0:
            print(f"Seu saldo está negativo : {saldo}")
        print(saldo)
        print(input("\nPressione Enter para voltar ao menu... "))
        sleep(3)
        menu()

    def historico_transacoes(self):
        print("\nHistórico de Receitas ")
        for receita in self.receitas:
            print(f"Valor: {receita['valor']}, Descrição: {receita['descricao']}")
        print("\nHistórico de Despesas ")
        for despesa in self.despesas:
            print(
                f"Valor: {despesa['valor']}, Descrição: {despesa['descricao']}, Categoria: {despesa['categoria']}"
            )
        print(input("\nPressione Enter para voltar ao menu... "))
        sleep(3)
        menu()

    def exportar_informacoes(self):
        with open("historico_transacoes.txt", "w") as arquivo:
            arquivo.write("Histórico de Receitas\n")
            for receita in self.receitas:
                arquivo.write(
                    f"Valor: {receita['valor']}, Descrição: {receita['descricao']}\n"
                )
            arquivo.write("\nHistórico de Despesas\n")
            for despesa in self.despesas:
                arquivo.write(
                    f"Valor: {despesa['valor']}, Descrição: {despesa['descricao']}, Categoria: {despesa['categoria']}\n"
                )
        print("Informações exportadas com sucesso para 'historico_transacoes.txt'. \n")
        sleep(3)
        menu()

    def importar_informacoes(self):
        try:
            with open("historico_transacoes.txt", "r") as arquivo:
                linhas = arquivo.readlines()
                self.receitas = []
                self.despesas = []
                for linha in linhas:
                    if linha.startswith("Valor:"):
                        partes = linha.strip().split(", ")
                        valor = float(partes[0].split(": ")[1])
                        descricao = partes[1].split(": ")[1]
                        if "Categoria" in linha:
                            categoria = partes[2].split(": ")[1]
                            self.despesas.append(
                                {
                                    "valor": valor,
                                    "descricao": descricao,
                                    "categoria": categoria,
                                }
                            )
                        else:
                            self.receitas.append(
                                {"valor": valor, "descricao": descricao}
                            )
            print("Informações importadas com sucesso de 'historico_transacoes.txt'."
                  "\nVoltando ao menu... \n")
            sleep(3)
            menu()
        except FileNotFoundError:
            print("Arquivo 'historico_transacoes.txt' não encontrado.")
            sleep(3)
            menu()

    def menu(self):
        print(
            " Sistema Financeiro ".center(50, "="),
            "\n\n 1 - Cadastrar receita",
            "\n 2 - Cadastrar despesa",
            "\n 3 - Calcular saldo",
            "\n 4 - Historico de transações",
            "\n 5 - Exportar informações para arquivo",
            "\n 6 - Importar informações de arquivo",
            "\n 7 - Sair",
        )
        try:
            pergunta = int(input("\nEscolha uma opcão : "))
        except ValueError:
            print("Opção inválida, tente novamente. \n")
            sleep(3)
            self.menu()
        else:
            if pergunta == 1:
                self.cadastrar_receita()
            elif pergunta == 2:
                self.cadastrar_despesa()
            elif pergunta == 3:
                self.calcular_saldo()
            elif pergunta == 4:
                self.historico_transacoes()
            elif pergunta == 5:
                self.exportar_informacoes()
            elif pergunta == 6:
                self.importar_informacoes()
            elif pergunta == 7:
                print("Ate breve...")
                exit()
            else:
                print("Opção inválida")
                self.menu()


sistema = SistemaFinanceiro()
menu = sistema.menu
sistema.menu()
