import random
import array
import secrets
import string
import getpass
import hashlib
import os

MIN_LEN = 8
MAX_LEN = 512

CHARSETS = {
    'randvars': string.ascii_letters + string.digits,
    'numerical_digits': string.digits,
    'lowercase_letters': string.ascii_lowercase,
    'uppercase_letters': string.ascii_uppercase,
    'ymbols': string.punctuation
}

def generate_password(length, complexity_rules):
    if length < MIN_LEN or length > MAX_LEN:
        raise ValueError("Password length must be between {} and {}".format(MIN_LEN, MAX_LEN))

    password = []
    for charset, min_chars in complexity_rules.items():
        for _ in range(min_chars):
            password.append(secrets.choice(CHARSETS[charset]))

    char_pool = array.array('u', string.ascii_letters + string.digits + string.punctuation)
    random.shuffle(char_pool)

    for _ in range(length - sum(complexity_rules.values())):
        password.append(secrets.choice(char_pool))

    random.shuffle(password)
    return ''.join(password)

def store_password(password, username):
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    with open('passwords.txt', 'a') as f:
        f.write(f"{username}:{salt.hex()}:{hashed_password.hex()}\n")

def retrieve_password(username):
    with open('passwords.txt', 'r') as f:
        for line in f:
            stored_username, salt, hashed_password = line.strip().split(':')
            if stored_username == username:
                return hashed_password
    return None

def delete_password(username):
    with open('passwords.txt', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            stored_username, _, _ = line.strip().split(':')
            if stored_username!= username:
                f.write(line)
        f.truncate()

def main():
    username = input("Enter your username: ")
    password_length = int(input("Enter the desired password length: "))
    complexity_rules = {
        'randvars': int(input("Enter the minimum number of random variables: ")),
        'numerical_digits': int(input("Enter the minimum number of numerical digits: ")),
        'lowercase_letters': int(input("Enter the minimum number of lowercase letters: ")),
        'uppercase_letters': int(input("Enter the minimum number of uppercase letters: ")),
        'ymbols': int(input("Enter the minimum number of symbols: "))
    }

    password = generate_password(password_length, complexity_rules)
    print(f"Your new password is: {password}")
    store_password(password, username)

    while True:
        print("1. Retrieve password")
        print("2. Delete password")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            retrieved_password = retrieve_password(username)
            if retrieved_password:
                print(f"Your password is: {retrieved_password}")
            else:
                print("Password not found")
        elif choice == '2':
            delete_password(username)
            print("Password deleted")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
