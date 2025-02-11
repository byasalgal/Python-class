import random

# # while True:
# #     print(random.choice("coding"))
# # df= ["a","b","c"]
# # print(random.choice(df))

# # rand= random.randint(1,10)
# # inp = int(input("enter you  guess: "))
# # if rand == inp:
# #     print("You won!")
# # else:
# #     print("womp womp: ",rand)
# print(math.sqrt(int(input())))

cpu = random.randint(1,3)
user =  int(input("1 = paper 2 = rock 3 = scissor: "))
if user > 3:
    print("choose a correct number")
elif cpu == user:
    print("tie cpu choosed: ",cpu)
elif cpu == 1 and user == 2:
    print("cpu won, cpu answer:",cpu)
elif cpu == 2 and user ==  3:
    print("cpu won, cpu answer:",cpu)
elif cpu == 3 and user == 1:
    print("cpu won, cpu answer:",cpu)
elif user == 1 and cpu == 2:
    print("user won, cpu answer:",cpu)
elif user == 2 and cpu ==  3:
    print("user won, cpu answer:",cpu)
elif user == 3 and cpu == 1:
    print("user won, cpu answer:",cpu)