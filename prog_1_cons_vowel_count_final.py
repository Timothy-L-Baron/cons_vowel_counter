"""Program 1 for my portfolio - I want to write a program that will take as
input somebody's name and output the number of vowels and consonants. It will also output a magic word
created by randomly shuffling the letters of the person's name"""
import random

#Need lists of vowels and consonants
vows = ['a', 'e', 'i', 'o', 'u']
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

#prompt user for input
user_input = input("please input your name:")

# function that counts the numer of vowels and consonants
def cons_vow_counter(str):
    count_c = 0
    count_v = 0
    magic_letters_lst = []
    for letter in str:
        if letter in vows:
            count_v = count_v + 1
            magic_letters_lst.append(letter)
        if letter in cons:
            count_c = count_c + 1
            magic_letters_lst.append(letter)
    random.shuffle(magic_letters_lst)
    magic_letters = ""
    for letter in magic_letters_lst:
        magic_letters = magic_letters + letter
    return print('Your name has {} consonant(s) and {} vowel(s). \nYour name forms the magic word: {}'.format(count_c, count_v, magic_letters.upper()))


cons_vow_counter(user_input)
