ESTADOS = {"1": {"estados": ["DF", "GO", "MS", "MT", "TO"],
                 "nomes-completos":["Distrito-federal", "Goiás", "Mato-Grosso do Sul", "Mato Grosso", "Tocantins"]},
           "2": {"estados": ["AC", "AM", "AP", "PA", "RO", "RR"],
                 "nomes-completos": ["Acre", "Amapá", "Pará", "Rondônia", "Roraima"]},
           "3": {"estados": ["CE", "MA", "PI"],
                 "nomes-completos": ["Ceará", "Maranhão", "Piauí"]},
           "4": {"estados": ["AL", "PB", "PE", "RN"],
                 "nomes-completos": ["Alagoas", "Paraíba", "Pernambuco", "Rio Grande do Norte"]},
           "5": {"estados": ["BA", "SE"],
                  "nomes-completos": ["Bahia", "Ceará"]},
           "6": {"estados": ["MG"],
                  "nomes-completos": ["Minas Gerais"]},
           "7": {"estados": ["ES", "RJ"],
                  "nomes-completos": ["Espírito Santo", "Rio de Janeiro"]},
           "8": {"estados": ["SP"],
                  "nomes-completos": ["São Paulo"]},
           "9": {"estados": ["PR", "SC"],
                 "nomes-completos": ["Paraná", "Santa Catarina"]},
           "0": {"estados": ["RS"],
                 "nomes-completos": ["Rio Grande do Sul"]}}


def gerar_d(lista):
    if lista == None:
        d = {"status":"sem sucesso",
                 "Base-Estadual": "Erro na base",
                 "Estados-pertencentes": "Não declarados, por motivo de erro",
                 "retorno-nao-esperado" : None,
                 "retorno-requisicao": False}
        return d
    else:
        d = {"status": "sucesso",
                "Base-Estadual": lista[0],
                "Estados-pertencentes": lista[1],
                "retorno-requisicao": True}
        return d


def verificar_estado(numero_base_estadual:str, d=ESTADOS, h=False):
    try:
        if not dict(d):
            print("Houve um problema!")
            print("Esperado para d: dict()")
            print(f"valor inserido: {d}")
            return None
        elif numero_base_estadual not in d:
            print("Id error!")
            if not isinstance(numero_base_estadual, str):
                print(f"Tipo esperado: type {type(str(numero_base_estadual))}")
                print(f"Tipo inserido: type {type(numero_base_estadual)}")
                print(f"numero_base_estadual deve ser do tipo string")
            print(f"Esperado conforme a regra estadual: {[i for i in d]}\nParâmetro inserido:'{numero_base_estadual}'")
            print("O id dos estados deve ser prescrito conforme as regras de base do estado")
            return None
        else:
            l = [buscar_id(numero_base_estadual), buscar_estados(numero_base_estadual, ESTADOS, h)]
            return l
    except Exception as e:
        print("Houve uma exception em verificar_estado:")
        print(f"status ocorrido: {e}")
        return None


def buscar_id(id, d=ESTADOS):
    try:
        for x in d:
            if id in x:
                print(f"O CPF é Respectivo da base estadual {x}")
                return x
        else:
            print(f"O CPF não pertence a nenhuma base")
            return None
    except Exception as e:
        print("Houve um exception em buscar_id:")
        print(e)
        return None


def buscar_estados(base, d=ESTADOS, habilitar=False):
    try:
        if habilitar == True:
            for i in d:
                if base == i:
                    print("Estados pertencentes:")
                    for x in range(0, len(d[i]["nomes-completos"])-1):
                        print(d[i]["nomes-completos"][x], end=", ")
                    print(d[i]["nomes-completos"][-1])
                    return d[i]["nomes-completos"]
        else:
            for i in d:
                if base == i:
                    print("Estados pertencentes:")
                    for x in range(0, len(d[i]["nomes-completos"])-1):
                        print(d[i]["estados"][x], end=", ")
                    print(d[i]["estados"][-1])
                    return d[i]["estados"]
    except Exception as e:
        print("Houve uma Exception na função buscar_estados")
        print(f"Exception: {e}")

def puxar_digitos(cpf):
    l_d = []
    for d in range(0, len(cpf) - 2):
        l_d.append(int(cpf[d]))
    return l_d

def ValidarDigito1(l, cont=10):
    s = 0
    for val in l:
        val *= cont
        s += val
        cont -= 1
    resto = s % 11
    if resto < 2:
        return 0
    else:
        sub = 11 - resto
        return sub
    
def ValidarDigito2(l, validacao1, cont=11):
    l.append(validacao1)
    s = 0
    for val in l:
        val *= cont
        s += val
        cont -= 1
    resto = s % 11
    if resto < 2:
        return 0
    else:
        sub = 11 - resto
        return sub


def analisar_cpf(cpf, hab=False):
    try:
        uniao = ""
        verificar = puxar_digitos(cpf)
        # Verificar se todos os dígitos são iguais
        if len(set(verificar)) == 1:
            raise ValueError("CPF inválido! Todos os dígitos são iguais.")
        d1 = ValidarDigito1(verificar)
        d2 = ValidarDigito2(verificar, d1)
        uniao += str(d1) + str(d2)
        if uniao == cpf[9:]: 
            print(f"O CPF {cpf} é válido!")
            if cpf[8] in ESTADOS:
                print(gerar_d(verificar_estado(cpf[8], ESTADOS, hab)))
            else:
                print(f"Este CPF não pertence a nenhum estado")
        else:
            print(f"CPF {cpf} inválido!")
            raise ValueError(f"O CPF {cpf} é inválido!")
    except ValueError as ve:
        print("Ocorreu uma inserção inválida em analisar_cpf!")
        print(ve)
        d = gerar_erro(cpf, str(ve))
        print(d)
    except Exception as e:
        print("Ocorreu uma Exception em analisar_cpf!")
        print("retorno:", e)


def gerar_erro(cpf, erro):
    if erro == "CPF inválido! Deve ter 11 dígitos.":
        d = {"status": "Erro de cadastro",
                 "motivo": "CPF não possuí 11 dígitos",
                 "CadastroUsuario": cpf,
                 "CadastroEsperado": "11 dígitos"}
        return d
    elif erro == "CPF inválido! Deve conter apenas dígitos numéricos.":
        d = {"status": "Erro de cadastro",
                 "motivo": "CPF contém caracteres diferentes de números",
                 "CadastroUsuario": cpf,
                 "CadastroEsperado": "dígitos numéricos"}
        return d
    elif erro == f"O CPF {cpf} é inválido!":
        d = {"status": "CPF inválido",
                "motivo": "CPF não reconhecido",
                "CadastroUsuario": cpf,
                "CadadtroEsperado": "É preciso inserir um CPF que seja válido"}
        return d
    elif erro == "CPF inválido! Todos os dígitos são iguais.":
        d = {"status": "CPF inválido",
                "motivo": "CPF possuí dígitos verificadores iguais",
                "CadastroUsuario": cpf,
                "CadadtroEsperado": "É preciso inserir um CPF que contenha valores diferentes uns dos outros"}
        return d
    else:
        return "Erro não cadastrado para gerar Dict"


def gerar_cpf():
    while True:
        try:
            print("==" * 30)
            cpf = input("Digite o seu CPF: [digite exit ou ! para sair] ").strip().replace(".", "").replace("-", "")
            if cpf.lower() in ["exit", '!']:
                break
            
            if len(cpf) != 11:
                raise ValueError("CPF inválido! Deve ter 11 dígitos.")
            
            if not cpf.isdigit():
                raise ValueError("CPF inválido! Deve conter apenas dígitos numéricos.")
            analisar_cpf(cpf, True)
        except ValueError as ve:
            print("Erro!")
            print(ve)
            d = gerar_erro(cpf, str(ve))
            print(d)
        except Exception as e:
            print("Houve uma exceção em Main:")
            print(e)
        finally:
            print("==" * 30)


if __name__ == "__main__":
    gerar_cpf()
    #Estdar com mais CPFs de teste para validar igualdade na soma dos dígitos do CPF [11, 22, 33, 44, 55, 66, 77, 88, 99]
