import random

ran_float=random.random()
print(ran_float)
ran_int=random.randint(1,100)
print(ran_int)
my_list=[1,2,3,4,5,6,7,8,9,10,["abc","def"]]
my_tuple=(1,2,3,("a","b","c"))
my_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ran_choice1=random.choice(my_list)
ran_choice2=random.choice(my_tuple)
ran_choice3=random.choice(my_string)
print(ran_choice1)
print(ran_choice2)
print(ran_choice3)

ran_shuffle1=random.shuffle(my_list)
print(ran_shuffle1)