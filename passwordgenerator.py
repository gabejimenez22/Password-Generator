import secrets
import string
import json


all_characters = list(string.ascii_letters + string.digits + string.ascii_lowercase +string.ascii_uppercase + string.punctuation)

uppercase = secrets.choice(string.ascii_uppercase)
lowercase = secrets.choice(string.ascii_lowercase)
digit = secrets.choice(string.digits)
special = secrets.choice(string.punctuation)


password_length = int(input("how long would you like your pasword to be(enter an integer):"))
password_name = str(input("what would you like to name this password:"))


characters_each =[uppercase , lowercase , digit , special]
remaining_chars = [secrets.choice(all_characters) for i in range(password_length - 4)]

            
password_list = characters_each + remaining_chars

secrets.SystemRandom().shuffle(password_list)
password = "".join(password_list)
password_generated = {password_name: "".join(password_list)}
print( password_generated)


with open("generated_passwords.txt", "a") as file:
    json.dump(password_generated, file)
    file.write("\n") 