import random
import string

def generate_password(length=8):
    #generates a random password of given length
    if length < 8:
        print("Password length should be at least 8 characters for security.")
        return None
    
    #Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    #Ensure password contains at least one of each type
    all_chars = lowercase + uppercase + digits + special_chars
    password = (
        random.choice(lowercase) +
        random.choice(uppercase) + 
        random.choice(digits) + 
        random.choice(special_chars) +
        ''.join(random.choices(all_chars, k=length-4))
    )
    #Shuffle password for randomness
    password = ''.join(random.sample(password, len(password)))
    return password


