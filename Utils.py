from hashlib import md5, sha1, sha224, sha256, sha512, sha384, sha512
from base64 import b64decode, b32decode, b85decode
from Crypto.Hash import MD2, MD4
from Session import Var_results
from base45 import b45decode
from base58 import b58decode
from binascii import Error
from re import search, sub


class Identifier:

    def identify_value(string):

        red_bold = "\x1b[1;31m"
        reset = "\x1b[0m"

        hashlen = len(string)

        if hashlen == 32 and all(chr in "0123456789abcdef" for chr in string):
            return "Try these options => {MD5/MD4/MD2}"
        elif hashlen == 40 and string.isalnum():
            return "SHA-1"
        elif hashlen == 56 and all(chr in "0123456789abcdef" for chr in string):
            return "SHA-224"
        elif hashlen == 64 and all(chr in "0123456789abcdef" for chr in string):
            return "SHA-256"
        elif hashlen == 96 and all(chr in "0123456789abcdef" for chr in string):
            return "SHA-384"
        elif hashlen == 128 and all(chr in "0123456789abcdef" for chr in string):
            return "SHA-512"
        else:
            def is_base64(string):
                if len(string) % 4 != 0:
                    return False
                
                for check in string.split():
                    if check.isnumeric():
                        return False

                valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
                if not all(char in valid_chars for char in string):
                    return False
                
                try:
                    b64decode(string)
                except (TypeError, Error):
                    return False

                return True

            def is_base32(string):
                for check in string.split():
                    if check.isnumeric():
                        return False
                else:
                    base32_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567")
                    return all(chr in base32_chars for chr in string)

            def is_base58(string):
                for check in string.split():
                    if check.isnumeric():
                        return False
                else:
                    base58_chars = set("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
                    return all(chr in base58_chars for chr in string)

            def is_base85(string):
                for check in string.split():
                    if check.isnumeric():
                        return False
                else:
                    base85_chars = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")
                    return all(chr in base85_chars for chr in string)

            def is_base45(string):
                for check in string.split():
                    if check.isnumeric():
                        return False
                else:
                    base45_chars = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:")
                    return all(chr in base45_chars for chr in string)
            
            def is_vigenere(string):
                string = sub(r'[^a-zA-Z0-9]', '', string)

                return search(r'[^a-zA-Z]', string) is None
            
            def is_octal(string):
                octal_values = string.split()

                try:
                    for value in octal_values:
                        int_value = int(value, 8)
                except ValueError:
                    return False

                return True

            if is_base64(string):
                return "Base64"
            elif is_base32(string):
                return "Base32"
            elif is_base58(string):
                return "Base58"
            elif is_base85(string):
                return "Base85"
            elif is_base45(string):
                return "Base45"
            elif is_vigenere(string):
                return "Try these options => {Vigenère/ROT13/ROT47}"
            elif is_octal(string):
                return "Octal"
            else:
                pass

        return f"[{red_bold}X{reset}] The algorithm could not be identified\n"


class Ciphers_Cryptographies:

    green_bold = "\x1b[1;32m"
    red = "\x1b[31m"
    reset = "\x1b[0m"

    acess = Var_results()


    def __init__(self, value, cipher_type):
        self.value = value
        self.cipher_type = cipher_type

    
    def decrypt_with_no_key(self):
        
        if self.cipher_type == "base64":

            try:
                decrypted = b64decode(self.value)
            except Exception as e:
                return f"[{self.red}X{self.reset}] {e}"

            print(self.acess.save_results(self.value, decrypted, self.cipher_type))

            return f"[{self.green_bold}+{self.reset}] Decoded => {decrypted.decode('utf-8', errors='ignore')}\n"
        
        elif self.cipher_type == "base32":

            try:
                decrypted = b32decode(self.value)
            except Exception as e:
                return f"[{self.red}X{self.reset}] {e}"

            print(self.acess.save_results(self.value, decrypted, self.cipher_type))

            return f"[{self.green_bold}+{self.reset}] Decoded => {decrypted.decode('utf-8', errors='ignore')}\n"
        
        elif self.cipher_type == "base45":

            try:
                decrypted = b45decode(self.value)
            except Exception as e:
                return f"[{self.red}X{self.reset}] {e}"

            print(self.acess.save_results(self.value, decrypted, self.cipher_type))

            return f"[{self.green_bold}+{self.reset}] Decoded => {decrypted.decode('utf-8', errors='ignore')}\n"
        
        elif self.cipher_type == "base85":

            try:
                decrypted = b85decode(self.value)
            except Exception as e:
                return f"[{self.red}X{self.reset}] {e}"

            print(self.acess.save_results(self.value, decrypted, self.cipher_type))

            return f"[{self.green_bold}+{self.reset}] Decoded => {decrypted.decode('utf-8', errors='ignore')}\n"
        
        elif self.cipher_type == "base58":
            
            try:
                decrypted = b58decode(self.value)
            except Exception as e:
                return f"[{self.red}X{self.reset}] {e}"

            print(self.acess.save_results(self.value, decrypted, self.cipher_type))

            return f"[{self.green_bold}+{self.reset}] Decoded => {decrypted.decode('utf-8', errors='ignore')}\n"
        
        elif self.cipher_type == "ROT13":
            
            decrypted = ""

            for char in self.value:
                if 'a' <= char <= 'z':
                    decrypted_char = chr(((ord(char) - ord('a') - 13) % 26) + ord('a'))
                elif 'A' <= char <= 'Z':
                    decrypted_char = chr(((ord(char) - ord('A') - 13) % 26) + ord('A'))
                else:
                    decrypted_char = char
                decrypted += decrypted_char

            print(self.acess.save_results(self.value, decrypted, self.cipher_type))
            return f"[{self.green_bold}+{self.reset}] Decoded => {''.join(decrypted)}\n"

        elif self.cipher_type == "ROT47":

            decrypted = ""

            for char in self.value:
                if '!' <= char <= 'O':
                    decrypted_char = chr(ord(char) + 47)
                elif 'P' <= char <= '~':
                    decrypted_char = chr(ord(char) - 47)
                else:
                    decrypted_char = char
                decrypted += decrypted_char

            print(self.acess.save_results(self.value, decrypted, self.cipher_type))
            return f"[{self.green_bold}+{self.reset}] Decoded => {''.join(decrypted)}\n"

        elif self.cipher_type == "octal":
            
            octal_numbers = self.value.split()

            decrypted = "".join(chr(int(octal, 8)) for octal in octal_numbers)
            
            print(self.acess.save_results(self.value, decrypted, self.cipher_type))
            return f"[{self.green_bold}+{self.reset}] Decoded => {decrypted}\n"


    def decrypt_with_key(self, key):

        if self.cipher_type == "vigenere":

            plaintext = ""
            i = 0

            for char in self.value:
                if char.isalpha():
                    key_char = key[i % len(key)]
                    
                    first_alphabet_letter = 'a' if char.islower() else 'A'
                    old_char_position = ord(char) - ord(first_alphabet_letter)
                    key_char_position = ord(key_char.lower()) - ord('a')
                    new_char_position = (old_char_position - key_char_position + 26) % 26
                    decrypted_char = chr(new_char_position + ord(first_alphabet_letter))
                    
                    plaintext += decrypted_char
                    i += 1
                else:
                    plaintext += char

            print(self.acess.save_results(self.value, plaintext, self.cipher_type))
            return f"[{self.green_bold}+{self.reset}] Decoded => {plaintext}\n"


class Hash:

    green_bold = "\x1b[1;32m"
    red_bold = "\x1b[1;31m"
    reset = "\x1b[0m"

    acess = Var_results()

    def __init__(self, value, wordlist, hash_type):
        self.value = value
        self.wordlist = wordlist
        self.hash_type = hash_type


    def crack(self):

        flag = 0

        try: 
            pass_file = open(self.wordlist, "rb")

        except FileNotFoundError:
            return f"{self.red_bold}[X]{self.reset} File path not found!\n"

        print("\n[-] Cracking...")

        for word in pass_file:
            enc_wrd = word.strip()

            if self.hash_type == "MD5":
                digest = md5(enc_wrd).hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode("utf-8"), self.hash_type))
                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"
            
            elif self.hash_type == "MD2":
                h = MD2.new()
                h.update(enc_wrd)
                
                digest = h.hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode("utf-8"), self.hash_type))
                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"
            
            elif self.hash_type == "MD4":
                h = MD4.new()
                h.update(enc_wrd)

                digest = h.hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode('utf-8'), self.hash_type))
                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"
        
            elif self.hash_type == "SHA256":        
                digest = sha256(enc_wrd.strip()).hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode('utf-8'), self.hash_type))

                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"

            elif self.hash_type == "SHA224":
                digest = sha224(enc_wrd.strip()).hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode('utf-8'), self.hash_type))

                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"
            
            elif self.hash_type == "SHA1":
                digest = sha1(enc_wrd.strip()).hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode('utf-8'), self.hash_type))

                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"

            elif self.hash_type == "SHA384":
                digest = sha384(enc_wrd.strip()).hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode('utf-8'), self.hash_type))

                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"

            elif self.hash_type == "SHA512":
                digest = sha512(enc_wrd.strip()).hexdigest()

                if digest == self.value:
                    flag = 1
                    print(self.acess.save_results(self.value, word.decode('utf-8'), self.hash_type))

                    return f"\n[{self.green_bold}+{self.reset}] Hash Found! => {word.decode('utf-8')}"

        if flag == 0:
            return f"{self.red_bold}[X]{self.reset} The Hash is not in your wordlist\n"
