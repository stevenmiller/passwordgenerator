import secrets
import string
import argparse

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('-l', '--length', type=int, default=12,
                        help='length of the password (default: 12)')
    args = parser.parse_args()
    password = generate_password(args.length)
    print(password)
