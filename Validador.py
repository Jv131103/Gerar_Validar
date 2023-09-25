import re

class ValidarCadastro:
    def __init__(self, valor: str) -> None:
        self.valor = valor


    def __ValidarCPF(self) -> str:
        lista = []
        for val in self.valor[3:]:
            lista.append(val)
        if len(lista) == 11:
            juntar = "" #Vai puxar os 9 primeiros dígitos
            ultimos_verificadores = ""
            if int(lista[8]) not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
                return "CPF não possui nenhum estado remanescente"
            for number in lista[:9]:
                juntar += number
            if len(set(juntar)) == 1: 
                return "CPF não pode ser igual"
            
            d10 = self.__ValidarDigito10(juntar)
            d11 = self.__ValidarDigito11(juntar, d10)
            ultimos_verificadores += str(d10) + str(d11)
            if ultimos_verificadores == self.valor[12:]:
                return "CPF"
            else:
                return "Não é nem CNPJ e nem CPF"
        else:
            return "CPF deve conter 11 dígitos"


    def __ValidarDigito10(self, l: list, cont=10) -> int: 
        s = 0 
        for val in l:
            val = int(val)
            val *= cont 
            s += val 
            cont -= 1
        resto = s % 11 
        if resto < 2: 
            return 0
        else: 
            sub = 11 - resto
            return sub 
        
    def __ValidarDigito11(self, l: tuple, validacao1: int, cont=11) -> int:
        lista = []
        for x in l:
            lista.append(int(x))
        lista.append(validacao1)
        s = 0 
        for val in lista:
            val *= cont 
            s += val 
            cont -= 1
        resto = s % 11 
        if resto < 2:
            return 0 
        else: 
            sub = 11 - resto
            return sub

    

    def ValidarCNPJ(self) -> str:
        if len(self.valor) == 14:
            valor = re.sub(r'[^0-9]', '', self.valor)
            l_12_digitos = []
            for x in valor[0:12]:
                l_12_digitos.append(int(x))  # Converta para inteiros
            d13 = self.__Calcular_primeiro_verificador_cnpj(l_12_digitos)
            d14 = self.__Calcular_segundo_verificador_cnpj(l_12_digitos + [d13])
            if d13 == int(valor[12]) and d14 == int(valor[13]):
                return "CNPJ"
            else:
                return self.__ValidarCPF()
        else:
            return "Precisa ter 14 dígitos"

    def __Calcular_primeiro_verificador_cnpj(self, L: list) -> int:
        cont1 = 5
        soma = 0
        for valor in L:
            digito = int(valor)
            digito *= cont1
            soma += digito
            if cont1 == 2:
                cont1 = 9
            else:
                cont1 -= 1
        resultado_digito13 = soma % 11
        if resultado_digito13 < 2:
            return 0
        else:
            return 11 - resultado_digito13

    def __Calcular_segundo_verificador_cnpj(self, L: list) -> int:
        cont1 = 6
        soma = 0
        for valor in L:
            digito = int(valor)
            digito *= cont1
            soma += digito
            if cont1 == 2:
                cont1 = 9
            else:
                cont1 -= 1
        resultado_digito14 = soma % 11
        if resultado_digito14 < 2:
            return 0
        else:
            return 11 - resultado_digito14

x = ValidarCadastro("00002369819600") #Isto é um CPF gerado automáticamente
print(x.ValidarCNPJ())
y = ValidarCadastro("07373002000175") #CNPJ de uma empresa
print(y.ValidarCNPJ())
