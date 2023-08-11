import random
import string

def generate_password(length, complexity):
    characters = string.ascii_letters
    if complexity >= 1:
        characters += string.digits
    if complexity >= 2:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password = generate_password(length=12, complexity=2)
print("Generated Password:", password)