#Remember import random function here:
import random 

my_list = [4,5,734,43,45]

#The magic is here:
for i in range(1, 11):
    my_list.append(random.randint(1, 1000))

print(my_list)