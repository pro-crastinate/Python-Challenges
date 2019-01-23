import random


def string_to_array(string):
    str_arr = list(string)
    return str_arr


def initiate_counter(str_arr):
    for i in range(len(str_arr)):
        counter[i] = 0


def user_Input(arr,chance):
    chnce = chance
    while chnce != 0:
        print('Chances left =', end=' ')
        print(chnce)
        user_inp = input("Your guess: ")
        guess_stat = check_alpha(arr, user_inp, chance)
        if guess_stat:
            print('\nGood Guess!')
        else:
            chnce -= 1
        wol = win_or_lose(chnce, counter)
        if wol:
            print("Well Done!")
            break


def check_alpha(arr, X, chance):
    guess_good = False
    for i in range(len(arr)):
        if arr[i] == X.lower() or arr[i] == X.upper():
            counter[i] = 1
            guess_good = True
        if arr[i] == ' ':
            counter[i] = 1
        if ord(arr[i]) in range(32,48):
            counter[i] = 1
    if guess_good :
        print_current_stage(arr, counter)
        return guess_good
    else:
        print('Wrong Guess!')
        print_current_stage(arr, counter)
        return guess_good


def print_current_stage(arr,counter):
    for i in range (len(counter)):
        if counter[i] == 1:
            print(arr[i], end=' ')
        else:
            print('_', end=' ')


def check_status(counter):
    win = False
    for i in range(len(counter)):
        counter1all = True
        if counter[i] == 0:
            counter1all = False
            break
        else:
            counter1all = True
    if counter1all:
        win = True
    else:
        win = False
    return win


def win_or_lose(chances, counter):
    wol = check_status(counter)
    if wol:
        print("\nYou Win!!\n")
        return wol
    elif not wol and chances == 0:
        print("\nYou Lose!!\n")
        return wol
    elif not wol and chances != 0:
        print("\nKeep Trying\n")
        return wol


def game_start(string):
    guess_arr = string_to_array(string)
    initiate_counter(guess_arr)
    user_Input(guess_arr,chance)


def read_movie_name():
    file = open('D:\\Ankit\\Github\\Python\\Python-Challenges\\Movie_List.txt')
    movies_list = file.read().splitlines()
    file.close()
    return movies_list


counter = {}
chance = 10
guess_list = read_movie_name()
guess_this = random.choice(guess_list)
#print(guess_list)
#print(guess_this)
game_start(guess_this)
