#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tupla = (0, None)
    else:
            tupla = (len(sentence), sentence[0])
    return tupla

     
