import random
import argparse
import string


LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = '!@#$%^&*()'
ALL_CHARS = LOWER + UPPER + DIGITS + SYMBOLS

def generate_password(length):
    if length < 4:
        raise ValueError('O comprimento deve ser pelo menos 4 para incluir todos os tipos de caracteres.')

    password = [
        random.choice(LOWER),
        random.choice(UPPER),
        random.choice(DIGITS),
        random.choice(SYMBOLS)
    ]

    password += [random.choice(ALL_CHARS) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description='Gerador de Senhas Seguras')
    parser.add_argument('--length', type=int, default=12, help='Comprimento da senha (mínimo 4)')
    args = parser.parse_args()
    try:
        senha = generate_password(args.length)
        print(f'Senha gerada: {senha}')
    except ValueError as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    main()
