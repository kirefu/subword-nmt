#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:53:31 2020

@author: fkirefu
"""

from collections import Counter, defaultdict
import matplotlib.pyplot as plt

file = '/home/fkirefu/csd3/ip/data/ar-en/ar-en.train.tc.en'

with open(file, 'r') as f:
    
    data = []
    main_counter_dict = defaultdict(int)

    for i, ff in enumerate(f):
        data.extend(ff.strip().split())
        
    
        if not i % 1000000:
            counter_dict = Counter(data)
            
            for k,v in counter_dict.items():
                
                main_counter_dict[k] += v
                
            del counter_dict
            data = []
            
            
counter_dict = Counter(data)

for k,v in counter_dict.items():
    
    main_counter_dict[k] += v
    
del counter_dict

TOTAL = sum(list(main_counter_dict.values()))

main_counter_dict = {k: v for k, v in sorted(main_counter_dict.items(), key=lambda item: item[1], reverse=True)}


main_counter_dict_dec = {k: v/TOTAL for k, v in main_counter_dict.items()}

main_counter_dict_cum = {}
subtotal = 0
for k, v in main_counter_dict_dec.items():
    
    subtotal += v
    main_counter_dict_cum[k] = subtotal
    

    