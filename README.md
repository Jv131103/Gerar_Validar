# Gerar_Validar
Gerador de CPF e Validador de CPF/CNPJ

## Informações sobre Estados e Validador de CPF

Este código Python contém informações sobre os estados brasileiros, incluindo suas siglas e nomes completos. Além disso, ele inclui um validador de CPF que verifica a validade de um número de CPF inserido.

## Estados

O código define um dicionário chamado `ESTADOS` que mapeia os números de base estadual para informações sobre os estados.

Exemplo:

```python
ESTADOS = {
    "1": {
        "estados": ["DF", "GO", "MS", "MT", "TO"],
        "nomes-completos": ["Distrito Federal", "Goiás", "Mato Grosso do Sul", "Mato Grosso", "Tocantins"]
    },
    # ...
    # Outros estados
    # ...
    "9": {
        "estados": ["PR", "SC"],
        "nomes-completos": ["Paraná", "Santa Catarina"]
    },
    "0": {
        "estados": ["RS"],
        "nomes-completos": ["Rio Grande do Sul"]
    }
}
```
O código inclui funções para verificar a qual estado pertence um número de base estadual e para buscar informações sobre os estados.

```python
# Verificar o estado para a base estadual "1"
resultado = verificar_estado("1", ESTADOS)
print(resultado)
# Saída: ["1", ["Distrito Federal", "Goiás", "Mato Grosso do Sul", "Mato Grosso", "Tocantins"]]

# Buscar informações sobre o estado para a base estadual "5"
info_estado = buscar_estados("5", ESTADOS)
print(info_estado)
# Saída: ["BA", "SE"]
```

## Validador de CPF

Além das informações sobre estados, o código inclui um validador de CPF que verifica a validade de um número de CPF inserido.

Exemplo de uso:

```python
# Verificar a validade de um CPF
cpf = "123.456.789-09"
analisar_cpf(cpf)
```
Este código Python é uma ferramenta útil para obter informações sobre os estados brasileiros e verificar a validade de números de CPF.
