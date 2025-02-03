import random
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Pega palavras aleatórias em português do arquivo JSON
def get_portuguese_words(count=4):
    with open('pt-br.json', 'r', encoding='utf-8') as file:
        words = json.load(file)
    return random.sample(words, count)

# Gera senha com palavras em português e caracteres especiais/dígitos, se necessário
def generate_password(target_length=12, include_digits=False, include_special=False):
    password = ""
    
    # Determina a quantidade de palavras a ser gerada (com base no comprimento total)
    while len(password) < target_length:
        word_count = 1  # Inicia com uma palavra por vez
        words = get_portuguese_words(word_count)
        for word in words:
            password += word
        
        # Adiciona números ou caracteres especiais se necessário
        if include_digits:
            password += str(random.randint(0, 99))
        
        if include_special:
            password += random.choice(["@", "#", "$", "&", "_"])

    # Ajusta o tamanho da senha para não ultrapassar o tamanho máximo
    return password[:target_length]

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def home():
    password = ''
    target_length = 12  # Tamanho padrão da senha
    include_digits = False
    include_special = False
    
    if request.method == 'POST':
        target_length = int(request.form['length'])
        include_digits = 'digits' in request.form
        include_special = 'special' in request.form

        password = generate_password(target_length, include_digits, include_special)

    return render_template('index.html', password=password, length=target_length, use_digits=include_digits, use_special=include_special)

# Rodando o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
