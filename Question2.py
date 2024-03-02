import sympy

def gcd_extended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = gcd_extended(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose a random prime e
    while True:
        e = sympy.randprime(2, phi - 1)
        if sympy.gcd(e, phi) == 1:
            break
    
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(text, public_key):
    e, n = public_key
    encrypted_text = [pow(ord(char), e, n) for char in text]
    return encrypted_text

def decrypt(encrypted_text, private_key):
    d, n = private_key
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in encrypted_text])
    return decrypted_text

def main():
    # Input prime indices
    index_p = int(input("Enter the index of the first prime number: "))
    index_q = int(input("Enter the index of the second prime number: "))

    # Get prime numbers corresponding to the indices
    p = sympy.prime(index_p)
    q = sympy.prime(index_q)

    # Generate keys
    public_key, private_key = generate_keys(p, q)
    print("\nPublic key =", public_key)
    print("Private key =", private_key)

    # Read sample text file
    with open("C:\\Users\\vdagg\\Downloads\\WebDevelopment_Neeharika\\5.3+CSS+Selectors\\sample.txt", "r") as file:

        text = file.read()

    # Encryption
    encrypted_text = encrypt(text, public_key)

    # Save encrypted content to a new file
    with open("Adella_encrypted.txt", "w") as file:
        file.write(','.join(map(str, encrypted_text)))

    print("Encryption complete. Encrypted content saved to Adella_encrypted.txt")

    # Decryption
    decrypted_text = decrypt(encrypted_text, private_key)

    # Save decrypted content to a new file
    with open("Adella_decrypted.txt", "w") as file:
        file.write(decrypted_text)

    print("Decryption complete. Decrypted content saved to Adella_decrypted.txt")

if __name__ == "__main__":
    main()
