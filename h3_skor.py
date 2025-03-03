#!/bin/bash
import random

takımlar = ['FB', 'GS']

fbskor = random.randint(1,10) 
gsskor = random.randint(1,10)  


if fbskor > gsskor:
    kazanan = 'Fenerbahçe '
elif gsskor > fbskor:
    kazanan = 'Galatasaray '
else:
    kazanan = 'Beraberlik'

print(f"Fenerbahçe'nin attığı gol: {fbskor}")
print(f"Galatasaray'ın attığı gol: {gsskor}")
