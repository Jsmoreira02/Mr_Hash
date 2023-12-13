from Utils import Hash, Ciphers_Cryptographies, Identifier
from Session import List, Var_results
from os import system, getcwd
from shlex import split
from sys import exit
from cmd import Cmd

yellow_bold = "\x1b[1;38;5;226m"
red = "\x1b[31m"
green_bold = "\x1b[1;32m"
reset = "\x1b[0m"


def logo():

    banner = "\n          ███    ███ ██████         ██   ██  █████  ███████ ██   ██\n"
    banner += "          ████  ████ ██   ██        ██   ██ ██   ██ ██      ██   ██\n"
    banner += "          ██ ████ ██ ███████        ███████ ███████ ███████ ███████\n"
    banner += "          ██  ██  ██ ██   ██        ██   ██ ██   ██      ██ ██   ██\n"
    banner += "          ██      ██ ██   ██ ██     ██   ██ ██   ██ ███████ ██   ██\n\n"

    banner += "              ██████        ██████████  ██████████        ██████\n"
    banner += "            ████        ██████████████████████████████        ████\n"
    banner += "            ████    ██████████████████████████████████████    ████\n"
    banner += "            ██████████████████████████████████████████████████████\n"
    banner += "              ████████████████████████  ████████████████████████\n"
    banner += "                ██████████████████          ██████████████████\n"
    banner += "                    ████████                      ████████\n\n"


    description = f"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    description += f"\n| {red}Hashes{reset}: {{MD2, MD4, MD5, SHA1, SHA224, SHA256, SHA512, SHA384}}\n"
    description += f"| {red}Cryptographies{reset}: {{base64, base32, base45, base58, base85}}\n"
    description += f"| {red}Ciphers{reset}: {{ROT13, ROT47, octal, vigenere}}\n"
    description += "|\n"

    description += f'| [{yellow_bold}!{reset}]: For ciphertexts with spaces, write between "" => "pvcuregrkg jvgu fcnpr"\n'

    return red + banner + reset + description


class Console(Cmd):

    session = Var_results()

    def __init__(self):

        super().__init__()
        self.intro = f"\n[{green_bold}+{reset}] Welcome to the Mr.Hash's Console. Type 'help' for a list of commands."
        self.prompt = yellow_bold + "\nmrhash~# " + reset


    def do_help(self, args):

        args = args.split()
        
        if not args:
            info = "\n---------------------\n"
            info += "     - Options -     \n"
            info += "---------------------\n"
            info += "|  - crack          |\n"
            info += "|  - decrypt        |\n"
            info += "| ----------------- |\n"
            info += "|    - Utils -      |\n"
            info += "| ----------------- |\n"
            info += "|  - reverse        |\n"
            info += "|  - variable       |\n"
            info += "|  - uppercase      |\n"
            info += "|  - lowercase      |\n"
            info += "|  - savetofile     |\n"
            info += "|  - identify       |\n" 
            info += "|  - list           |\n"
            info += "| ----------------- |\n"
            info += "|    - Console -    |\n"
            info += "| ----------------- |\n"
            info += "|  - pwd            |\n"
            info += "|  - cat            |\n"
            info += "|  - ls             |\n"
            info += "|  - clear          |\n"
            info += "|  - exit           |\n"
            info += "---------------------\n\n"

            info += "- crack [hash or variable_name] [wordlist file path] [type]\n\n"
            info += "- decrypt [encrypted text or Ciphertext] [key] [type]\n\n"
            info += "- reverse [hash or encrypted text/variable_name]\n\n"
            info += "- variable [file path/hash_text} [name]\n\n"
            info += "- uppercase [hash or encrypted text/variable_name]\n\n"
            info += "- lowercase [hash or encrypted text/variable_name]\n\n"
            info += "- savetofile [filename]\n\n"
            info += "- identify [hash or encrypted text/variable_name]\n\n"
            info += "- list [options: hashes, crypt, results, variables]\n\n"
            info += "- clear\n\n"
            info += "- exit\n\n"

            info += "Type: help [options] for more info\n"
            
            print(info)

        elif args[0] == "crack":
            system("clear")
            
            info = "\n|-------------------------------------------------------------------------------------------|\n"
            info += "| Start Cracking by parsing the encrypted or hashed value, wordlist file path and hash type |\n"
            info += "| Example: crack 0a52730597fb4ffa01fc117d9e71e3a9 /home/user/file/rockyou.txt MD5           |\n"
            info += "| You can also pass a variable as data, to shorten the size of the command input            |\n"
            info += "| Example: crack hash wordlist hash_type                                                    |\n"
            info += "|-------------------------------------------------------------------------------------------|\n"

            print(info)

        elif args[0] == "decrypt":
            system("clear")
            
            info = "\n|------------------------------------------------------------------------------------------------|\n"
            info += "| Start decrypting by parsing the encrypted text or Ciphertext, optional key and encryption type |\n"
            info += "| Example: decrypt LT4gcHdkZG91c2VyY3RmZG9ocyA8LQ== base64                                       |\n"
            info += "| Example: decrypt Rjm* A OOK                                                                    |\n"
            info += "| You can also pass a variable as data, to shorten the size of the command input                 |\n"
            info += "| Example: decrypt ciphertext type                                                               |\n"
            info += "| Example: decrypt ciphertext key type                                                           |\n"
            info += "|------------------------------------------------------------------------------------------------|\n"

            print(info)

        elif args[0] == "reverse":
            system("clear")

            info = "\n|--------------------------------------------------------------------------------|\n"
            info += "| Reverse hashed or encrypted value                                              |\n"
            info += "| Example: reverse ==QL8Ayco9GZmR3YyV2c19GZkdHcg4TL                              |\n"
            info += "| You can also pass a variable as data, to shorten the size of the command input |\n"
            info += "| Example: reverse hash                                                          |\n"
            info += "|--------------------------------------------------------------------------------|\n"
        
            print(info)

        elif args[0] == "list":
            system("clear")

            info = "\n|-------------------------------------------------------|\n"
            info += "| List your decrypted or cracked values and variables   |\n"
            info += "| Example: list hashes                                  |\n"
            info += "| Example: list variables                               |\n"
            info += "| Example: list results                                 |\n"
            info += "| Example: list crypt                                   |\n"
            info += "|-------------------------------------------------------|\n"

            print(info)

        elif args[0] == "variable":
            system("clear")

            info = "\n|--------------------------------------------------------------------------------|\n"
            info += "| (Optional use) Inserts a value into a variable to shorten the command          |\n"
            info += "| Example: variable f961d3063fb669c263449563c8e2852b0228f68e hash                |\n"
            info += "| Example: variable /home/user/files/password.txt file                           |\n"
            info += "|--------------------------------------------------------------------------------|\n"

            print(info)

        elif args[0] == "uppercase":
            system("clear")

            info = "\n|--------------------------------------------------------------------------------|\n"
            info += "| Converts every character in the input to upper case                            |\n"
            info += "| Example: uppercase ==QL8Ayco9GZmR3YyV2c19GZkdHcg4TL                            |\n"
            info += "| You can also pass a variable as data, to shorten the size of the command input |\n"
            info += "| Example: uppercase hash                                                        |\n"
            info += "|--------------------------------------------------------------------------------|\n"

            print(info)

        elif args[0] == "lowercase":
            system("clear")

            info = "\n|--------------------------------------------------------------------------------|\n"
            info += "| Converts every character in the input to lower case                            |\n"
            info += "| Example: lowercase ==QL8Ayco9GZmR3YyV2c19GZkdHcg4TL                            |\n"
            info += "| You can also pass a variable as data, to shorten the size of the command input |\n"
            info += "| Example: lowercase hash                                                        |\n"
            info += "|--------------------------------------------------------------------------------|\n"

            print(info)
        
        elif args[0] == "identify":
            system("clear")

            info = "\n|--------------------------------------------------------------------------------|\n"
            info += "| Analyzes and identifies the type of hash, cipher or encryption                 |\n"
            info += "| Example: identify f961d3063fb669c263449563c8e2852b0228f68e                     |\n"
            info += "| You can also pass a variable as data, to shorten the size of the command input |\n"
            info += "| Example: identify hash                                                         |\n"
            info += "|--------------------------------------------------------------------------------|\n"

            print(info)
        
        elif args[0] == "savetofile":
            system("clear")

            info = "\n|--------------------------------------------------|\n"
            info += "| Save every cracked ou decrypted value to a file  |\n"
            info += "| Example: savetofile results.txt                  |\n"
            info += "|--------------------------------------------------|\n"

            print(info)                  

        elif args[0] == "quit" or args[0] == "exit":
            system("clear")

            info = "\n|------ Close Program ------|"
            print(info)

        elif args[0] == "clear":    
            system("clear")

            info = "\n|------ Clear terminal ------|"
            print(info)
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")


    def do_crack(self, args):

        args = split(args)

        if len(args) == 3:

            value, wordlist, hash_type = args

            if value in self.session.variables.keys() and wordlist in self.session.variables.keys():
                run = Hash(self.session.variables.get(value), self.session.variables.get(wordlist), hash_type)

            elif value in self.session.variables.keys():
                run = Hash(self.session.variables.get(value), wordlist, hash_type)

            elif wordlist in self.session.variables.keys():
                run = Hash(value, self.session.variables.get(wordlist), hash_type)
            else:
                run = Hash(value, wordlist, hash_type)

            print(run.crack())
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")

    
    def do_decrypt(self, args):

        args = split(args)

        if len(args) == 2:
            value, cipher_type = args

            if value in self.session.variables.keys():
                run = Ciphers_Cryptographies(self.session.variables.get(value), cipher_type)
            else:
                run = Ciphers_Cryptographies(value, cipher_type)

            print(run.decrypt_with_no_key())

        elif len(args) == 3:
            value, key, cipher_type = args

            if value in self.session.variables.keys() and key in self.session.variables.keys():
                run = Ciphers_Cryptographies(self.session.variables.get(value), cipher_type)

                print(run.decrypt_with_key(self.session.variables.get(key)))

            elif value in self.session.variables.keys():
                run = Ciphers_Cryptographies(self.session.variables.get(value), cipher_type)

                print(run.decrypt_with_key(key))

            elif key in self.session.variables.keys():
                run = Ciphers_Cryptographies(value, cipher_type) 

                print(run.decrypt_with_key(self.session.variables.get(key)))
            else:
                run = Ciphers_Cryptographies(value, cipher_type)           

                print(run.decrypt_with_key(key))
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")


    def do_reverse(self, args):

        args = split(args)
        
        if len(args) == 1:
            value = args[0]

            if value in self.session.variables.keys():
                new_value = self.session.variables.get(value)[::-1]
                print(f"{green_bold}[+]{reset} reversed => {new_value}")
            else:
                new_value = value[::-1]
                print(f"{green_bold}[+]{reset} reversed => {new_value}")
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")


    def do_variable(self, args):

        args = split(args)
    
        if len(args) == 2:
            value, name = args

            print(self.session.save_variable(value, name))
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")


    def do_uppercase(self, args):

        args = split(args)
        
        if len(args) == 1:
            value = args[0]
            
            if value in self.session.variables.keys():
                new_value = self.session.variables.get(value).upper()
                print(f"{green_bold}[+]{reset} to uppercase => {new_value}")
            else:
                new_value = value.upper()
                print(f"{green_bold}[+]{reset} to uppercase => {new_value}")
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")


    def do_lowercase(self, args):

        args = split(args)
        
        if len(args) == 1:
            value = args[0]

            if value in self.session.variables.keys():
                new_value = self.session.variables.get(value).lower()
                print(f"{green_bold}[+]{reset} to lowercase => {new_value}")
            else:
                new_value = value[::-1]
                print(f"{green_bold}[+]{reset} to lowercase => {new_value}")
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")


    def do_savetofile(self, args):

        args = split(args)

        if len(args) == 1:
            filename = args[0]
            with open(filename, "w") as file:

                result = f"\n| -------------------------- [{green_bold}!Your Results!{reset}] -------------------------- |\n"
                for key, value in self.session.results_list.items():
                    result += f"| --> {key}: {value}"

                result += f"| -------------------------- [{green_bold}!Your Results!{reset}] -------------------------- |\n\n"

                file.write(result)
                file.close()
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")

        
    def do_identify(self, args):

        args = split(args)

        if len(args) == 1:
            
            unknown = args[0]
            if unknown in self.session.variables.keys():
                unknown = self.session.variables.get(unknown)
            else:
                pass

            type = Identifier.identify_value(unknown)
            print(f"[{green_bold}+{reset}] Type: {type}")
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")


    def do_list(self, args):

        args = split(args)

        if len(args) == 1:
            options = args[0]
            run = List(options)

            print(run.list())
        else:
            print("-> Command syntax not recognized, try again or type [help {options}] for more information\n")

        
    def do_ls(self, args):
        
        args = args.split()
        
        if not args:
            system("ls")
        else:
            suffix = args[0]
        
            if suffix in self.session.variables.keys():
                suffix = self.session.variables.get(suffix)
            else:
                pass
        
            try:
                if len(args) == 2:
                    suffix2 = args[1]
                    
                    if suffix2 in self.session.variables.keys():
                        suffix2 = self.session.variables.get(suffix2)
                    else:
                        pass

                    system("ls " + suffix + f" {suffix2}")
                else:
                    system("ls " + suffix)
            
            except Exception as e:
                return f"[{red}X{reset}] {e}"
            
    
    def do_cat(self, args):

        args = args.split()

        if not args:
            print("-> Command syntax not recognized. File path not found!\n")
        else:
            suffix = args[0]

            if suffix in self.session.variables.keys():
                suffix = self.session.variables.get(suffix)
            else:
                pass
            
            try:
                system("cat " + suffix)

            except Exception as e:
                return f"[{red}X{reset}] {e}"
    
    
    def do_clear(self, args):
        system("clear")
        print(logo())
        
    
    def do_pwd(self, args):
        print(getcwd())

    
    def emptyline(self):
        pass
        
    
    def do_exit(self, args):
        exit()
    
    
if __name__ == "__main__":
    
    console = Console()

    try:
        print(logo())
        console.cmdloop()

    except KeyboardInterrupt:
        print("\nCtrl+C detected! Finished!")
        exit()
