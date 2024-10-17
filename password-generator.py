import random
import string

def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = lowercase + uppercase + digits + special_chars

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    password += random.choices(all_chars, k=length-4)

    random.shuffle(password)

    return ''.join(password)

password_length = 12
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
