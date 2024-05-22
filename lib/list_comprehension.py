#!/usr/bin/env python3

def return_evens(num_list):
    even_elements = [n for n in num_list if n % 2 == 0]
    return even_elements

print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
    return [s + "!" for s in sentence_list]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))