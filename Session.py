class Var_results:
    
    variables = {}
    results_list = {}

    green_bold = "\x1b[1;32m"
    reset_ascii_color = "\x1b[0m"
    
    
    def save_results(self, value, result, operation_type):

        if result:
            before = value
            self.results_list[before] = result

            return f"[{self.green_bold}+{self.reset_ascii_color}] The result has been saved!\n"
        else:
            pass


    def save_variable(self, value, name):

        if value:

            variable_name = name
            self.variables[variable_name] = value

            return f"[{self.green_bold}+{self.reset_ascii_color}] {value} has been saved in {variable_name}!\n"
        else:
            pass


class List:

    acess = Var_results()
    green_bold = "\x1b[1;32m"
    reset = "\x1b[0m"

    
    def __init__(self, value):
        self.value = value
    

    def list(self):

        if self.value == "hashes":
            
            info = f"\n| ---------------[{self.green_bold}!All available hashes!{self.reset}]-------------------- |\n"
            info += "| MD2, MD4, MD5, SHA1, SHA224, SHA256, SHA512, SHA384, SHA512 |\n"
            info += "| =========================================================== |\n\n"

            return info

        elif self.value == "ciphers" or self.value == "crypt":

            info = f"\n| -------------------[{self.green_bold}!All available cryptographies!{self.reset}]------------------ |\n"
            info += "| base64, base32, base45, base85, base58, ROT13, ROT47, octal, vigenere |\n"
            info += "| ===================================================================== |\n\n"

            return info

        elif self.value == "variables":

            info = f"\n| ------------------- [{self.green_bold}!Your Variables!{self.reset}] ------------------- |\n"

            print(info, end="")

            for key, value in self.acess.variables.items():
                print(f'| --> ("{key}": {value})')

            return f"| ------------------- [{self.green_bold}!Your Variables!{self.reset}] ------------------- |\n"

        elif self.value == "results":

            info = f"\n| -------------------------- [{self.green_bold}!Your Results!{self.reset}] -------------------------- |\n"

            print(info, end="")
            for key, value in self.acess.results_list.items():
                print(f"| --> {key}: {value}")

            return f"| -------------------------- [{self.green_bold}!Your Results!{self.reset}] -------------------------- |\n"
