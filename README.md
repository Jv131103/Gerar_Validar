# Gerar_Validar
Gerador de CPF e Validador de CPF/CNPJ

# Informações sobre Estados

Este código Python contém informações sobre os estados brasileiros, incluindo suas siglas e nomes completos. Ele também inclui uma função para verificar a qual estado pertence um número de base estadual.

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
O código também inclui funções para verificar a qual estado pertence um número de base estadual e para buscar informações sobre os estados.
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

Este Projeto futuramente será integrado a `WEB`
