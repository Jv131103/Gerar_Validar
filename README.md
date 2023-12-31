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

# Gerador de CPF Brasileiro

Este código Python gera números de CPF brasileiro válidos. Este código é fornecido apenas para fins acadêmicos e não deve ser usado de forma ilegal ou antiética.

## Funcionamento

O código consiste em várias funções que geram números de CPF. Aqui está uma visão geral das funções principais:

- `gerar8digitos()`: Gera os 8 primeiros dígitos do CPF aleatoriamente.

- `gerarNonoDigito(escolher=None)`: Gera o nono dígito do CPF de acordo com a norma governamental ou permite que você escolha um estado específico (por sigla) para o nono dígito.

- `gerar_primeiro_digito(l)`: Gera o primeiro dígito verificador do CPF com base nos 8 primeiros dígitos.

- `gerar_segundo_digito(l, digito1)`: Gera o segundo dígito verificador do CPF com base nos 8 primeiros dígitos e no primeiro dígito verificador.

## Uso

Para usar o gerador de CPF, você pode simplesmente executar o código Python. Ele gera um número de CPF válido e exibe-o no console.

Exemplo de uso:

```python
python gerador_cpf.py
==============================================
|    CPF criado com êxito!                   |
|    Lembre-se, isso aqui é para fins        |
|    acadêmicos                              |
|============================================|
|                                            |
| LINHA DE GERADOR SEM PONTO: 12345678909    |
|____________________________________________|
|                                            |
| LINHA DE GERADOR COM EDIÇÃO: 123.456.789-09|
|                                            |
==============================================
```

## Aviso

Este código é apenas para fins acadêmicos e não deve ser usado para fins ilegais ou antiéticos, como falsificação de CPF. Respeite todas as leis e regulamentações locais ao usar este código.

Nota: Os CPFs gerados por este código são válidos na estrutura, mas não têm nenhuma associação com pessoas reais. Eles são gerados aleatoriamente apenas para fins de demonstração e aprendizado.

# Validador de CPF e CNPJ

Este código Python permite validar números de CPF (Cadastro de Pessoa Física) e CNPJ (Cadastro Nacional da Pessoa Jurídica). Ele verifica se os números estão em conformidade com as regras de formação de CPF e CNPJ no Brasil.

## Funcionamento

O código possui uma classe chamada `ValidarCadastro` que contém métodos para validar CPF e CNPJ. Aqui estão os principais métodos:

- `ValidarCPF()`: Valida um número de CPF, verificando se ele atende aos critérios de formação de CPF, incluindo os dígitos verificadores.

- `ValidarCNPJ()`: Valida um número de CNPJ, verificando se ele atende aos critérios de formação de CNPJ, incluindo os dígitos verificadores.

## Uso

Para usar o código, crie uma instância da classe `ValidarCadastro` com um número de CPF ou CNPJ como argumento e chame o método apropriado para validar o número. Por exemplo:

```python
x = ValidarCadastro("00018558955360")  # Isto é um CPF gerado automaticamente pelo nosso gerador de CPF
print(x.ValidarCNPJ())

y = ValidarCadastro("07373002000175")  # CNPJ de uma empresa puxado via pesquisa na web
print(y.ValidarCNPJ())
```

O código retornará "CPF" se o número for válido como CPF, "CNPJ" se for válido como CNPJ ou uma mensagem de erro se não for válido como nenhum dos dois.

Nota: Os CPFs usados nos exemplos são apenas para fins de demonstração e aprendizado. Eles não têm nenhuma associação com pessoas ou empresas reais.
