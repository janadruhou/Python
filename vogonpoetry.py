#!/usr/bin/env python3
import random
zajmena = ["můj", "tvůj", "její", "jeho"]
podstatna = ["kočka", "králík", "prkodrťák", "vogon"]
slovesa = ["rozseká", "utíká", "zpívá", "ničí"]
příslovce = ["hlasitě", "smrdutě", "hrozně", "provokativně"]

for _ in [1, 2, 3, 4, 5]:
    zajmeno = random.choice(zajmena)
    podstatne = random.choice(podstatna)
    sloveso = random.choice(slovesa)
    if random.randint(0, 1) == 0:
        print(zajmeno, podstatne, sloveso)
    else:
        adverb = random.choice(příslovce)
        print(zajmeno, podstatne, adverb, sloveso)



