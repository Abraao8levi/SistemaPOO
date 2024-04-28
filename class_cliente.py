class Cliente:
    def __init__(self, nome, cpf, idade, rg):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade  # Corrigido aqui
        self.__rg = rg
    
    def mostrar_dados(self):
        print("Nome...............: ", self.nome)
        print("CPF..................: ", self.cpf)
        print("Idade.............: ", self.idade)
        print("RG..................: ", self.__rg)
