import random
import string

class RandPasswordGenerator():
    def generate_password(self, lenght, wantNums, wantUppers):
        password = ""
        chars = string.ascii_letters

        # Checking if the user want to include numbers to his password
        if wantNums.lower() == "yes":
            chars = chars + "1234567890"
        elif wantNums.lower() == "no":
            pass
        else:
            return "Invalid input at 'wantNums' input, please enter 'yes' or 'no'! "

        # Generating Random password uging random function 
        for i in range(lenght):
            password = password + random.choice(chars)

        # Checking if the user want to include upercase chars to his password  
        if wantUppers.lower() == "yes":
            return "Password: " + password
        elif wantUppers.lower() == "no":
            return "Password: " + password.lower()
        else:
            return "Invalid input at 'wantUppers' input, please enter 'yes' or 'no'! "
        

    def rigenerate_password(self):
        working = True
        while working == True:
            # inputing params
            lenght = int(input("How long do you want the password to be? [in numbers] "))
            wantNums = input("Do you want numbers in the password? [yes/no] ")
            wantUppers = input("Do you want uppercase letters? [yes/no] ")

            gen_pass = self.generate_password(lenght, wantNums, wantUppers)
            print(gen_pass)

            restart = input("Do you want another password? [yes/no] ")
            if restart.lower() == "yes":
                working = True
            else:
                print("Password Generator is shuting down!")
                working = False


if __name__ == "__main__":
    RandPasswordGenerator().rigenerate_password()
