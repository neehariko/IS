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

    # Input text to encrypt
    text = input("\nEnter your text: ")
    encrypted_text = encrypt(text, public_key)
    print("\nEncrypted Text =", encrypted_text)

if __name__ == "__main__":
    main()
