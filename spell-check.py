from pickle import load
from bitstring import BitArray
import mmh3

with open('spell-dict.pkl', 'rb') as file: array = load(file)
    
def check(word):
    for seed in range(7):
        slot = mmh3.hash(word, seed, signed=False) % 2593583
        if array[slot] is False: return False
    return True  # Maybe
  
