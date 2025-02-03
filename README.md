# Gerador de Senhas Aleatórias
Gera senhas seguras com critérios personalizados.

DEMO: https://gerador-de-senhas-aleatorias-e-seguras.onrender.com/

## Objetivo  
Criar um gerador de senhas seguras seguindo boas práticas de segurança da informação.  

O gerador deverá atender aos seguintes critérios:  
- Mínimo de 12 caracteres (letras maiúsculas, minúsculas, números e caracteres especiais).  
- Geração de frases fáceis de lembrar.  
- Senhas compostas por palavras em português e, quando solicitado, inclusão de números e caracteres especiais.
- Evita o uso de palavras comuns ou padrões previsíveis.

## Funcionalidades
- Escolha do tamanho personalizado da senha (de 12 a 30 caracteres). 
- Inclusão ou exclusão de números e símbolos na senha.  
- Senhas formadas por palavras em português retiradas de um arquivo JSON, que são misturadas com números e caracteres especiais, se solicitado.  

## Tecnologias Utilizadas  
- Python 3.13.1  
- Flask (framework web para criação do aplicativo)  
- random (para geração de palavras e números aleatórios)
- json (para leitura de um arquivo de palavras em português)
- Jinja2 (para renderização de templates no Flask)

## Material Acessado
- [Documentação do Python sobre a biblioteca random](https://docs.python.org/pt-br/3.13/library/random.html#)
- [Documentação do Python sobre a biblioteca secrets](https://docs.python.org/pt-br/3.13/library/secrets.html#module-secrets)
- [Como gerar chave aleatória em Python](https://pt.stackoverflow.com/questions/541504/como-gerar-chave-aleat%C3%B3ria-em-python)
- [Documentação do Python sobre a biblioteca string](https://docs.python.org/pt-br/3.13/library/string.html)
- [Documentação do Python sobre tipos embutidos](https://docs.python.org/pt-br/3.13/library/stdtypes.html)
- [Desmistificando o significado dos Underscores (_) em Python](https://medium.com/@leandrodestefani/desmistificando-o-significado-dos-underscores-em-python-6b0a78ec9f4c)
- [Documentação do PEP8 sobre estilos de nomenclatura](https://pep8.org/#descriptive-naming-styles)
- [What's the meaning of underscores (_ & __) in Python variable names? (Dan Bader)](https://www.youtube.com/watch?v=ALZmCy2u0jQ)
- [Documentação do Flask | Quick Start](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Documentação do Python sobre a biblioteca json](https://docs.python.org/pt-br/3.13/library/json.html)