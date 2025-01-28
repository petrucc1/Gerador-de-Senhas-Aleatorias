import string
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Função para gerar a senha
def generator_password(length, use_digits, use_special):
    # Definindo os caracteres permitidos
    chars = string.ascii_letters  # Letras maiúsculas e minúsculas

    if use_digits:
        chars += string.digits  # Adicionando números
    
    if use_special:
        chars += string.punctuation  # Adicionando caracteres especiais

    # Gerando senha aleatória
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def home():
    password = ''
    if request.method == 'POST':
        # Recebendo dados do formulário
        length = int(request.form['length'])
        use_digits = 'digits' in request.form
        use_special = 'special' in request.form

        # Gerando a senha
        password = generator_password(length, use_digits, use_special)

    return render_template('index.html', password=password)

# Rodando o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
