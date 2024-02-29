#!/usr/bin/env python3

num_list=[3,5,7,9,7,3]

def return_evens(num_list):
        new_list=[n for n in num_list if n % 2 == 0]
        print(new_list)
        
return_evens(num_list)


sentence_list=[]

def make_exclamation(sentence_list):
        new_sentence=[x + "!" for x in sentence_list]
        print(new_sentence)
    
make_exclamation(sentence_list)

