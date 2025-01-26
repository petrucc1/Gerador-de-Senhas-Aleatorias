import string
import random

# Combinando todos os caracteres possíveis (letras maiúsculas e minúsculas, números, símbolos e espaços em branco)
generator = string.printable

# Gerando senha aleatória
while True:
    password = ''.join(random.choice(generator) for _ in range(12))
    if (any(c.isupper() for c in password)
            and sum(c.islower() for c in password) >= 6
            and any(c.isdigit() for c in password)):
        break

print(password)