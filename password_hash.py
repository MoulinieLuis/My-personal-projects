import hashlib as hl

def hash_password(password):
    hashed_password = hl.sha256(password.encode()).hexdigest()
    return hashed_password

password = input("Enter your password: ")
hashed_password = hash_password(password)
print(f"The password hashed is: {hashed_password}")