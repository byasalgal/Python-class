import random
import string

password_length = int(input("how long: \n"))
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits

all_chars = lowercase + uppercase + numbers

password = []
for i in range(password_length):
    password.append(random.choice(all_chars))

random.shuffle(password)

final_password = ''.join(password)

print("your random password is:", final_password)