import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, long(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p/q khong phai so nguyen to")
    elif p == q:
        raise ValueError("Loi (p == q)!!")
    n = p * q
    print "n = p * q = ", n
    phi = (p - 1) * (q - 1)
    print "phi = (p - 1)*(q - 1) = ", phi
    # Chon e ngau nhien va nguyen to cung nhau voi phi
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1 or e == 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    print "e = ", e
    # Tinh d voi de = 1 mod phi
    d = multiplicative_inverse(e, phi)
    print "d = ", d
    return ((e, n), (d, n))


def encrypt(pk, plaintext):

    key, n = pk
    print "Ban ma goc la:"
    print ' '.join([str(ord(char)) for char in plaintext])
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):

    key, n = pk

    plain = [chr((char ** key) % n) for char in ciphertext]
    print "Ban ma goc la:"
    print ' '.join([str(ord(char)) for char in plain])
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':

    print "--------------------------------------------------------------------"
    print "RSA Encrypter/ Decrypter"
    print "--------------------------------------------------------------------"
    p = int(raw_input("Nhap vao mot so nguyen to p: "))
    q = int(raw_input("Nhap vao mot so nguyen to q: "))
    print "Dang tao public/privare key. . ."
    public, private = generate_keypair(p, q)
    print "Public key la", public, " va Private key la", private
    print "--------------------------------------------------------------------"
    message = str(raw_input("Nhap vao mot tin nhan: "))
    print "--------------------------------------------------------------------"
    encrypted_msg = encrypt(public, message)
    print "Tin nhan duoc ma hoa la: "
    print ' '.join(map(lambda x: str(x), encrypted_msg))
    print "--------------------------------------------------------------------"
    print "Giai ma voi private key ", private, " . . ."
    decrypted_msg = decrypt(private, encrypted_msg)
    print "Tin nhan goc la: ", decrypted_msg