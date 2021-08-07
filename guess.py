my_list=[' ','O',' ']
from random import shuffle
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def guess_pos():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('enter the number 0,1 or 2:')
    return int(guess)

def check_guess(my_list,guess):
    if my_list[guess]=='O':
        print('CORRECT GUESS!')
    else:
        print('INCORRECT GUESS!')
        print(my_list)

# mylist
my_list=[' ','O',' ']

#shuffle
mixed_list=shuffle_list(my_list)

#guess
check=guess_pos()

#check
check_guess(mixed_list,check)
