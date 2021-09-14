#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:52:22 2021

@author: alina
"""

import random
import datetime
import json

tissue_info = ['Solanum lycopersicum / fruit',
               'Solanum lycopersicum / leaf',
               'Helianthus annuus / seed',
               'Helianthus annuus / leaf',
               'Zea mays / seed',
               'Zea mays / leaf',
               'Solanum tuberosum / tuber',
               'Solanum tuberosum / leaf',
               'Oryza sativa / seed',
               'Oryza sativa / leaf',
               'Triticum aestivum / seed',
               'Triticum aestivum / leaf',
               ]

stored_freezer = ['-80 / 1', '-80 / 2', '-80 / 3', '-80 / 4']
stored_box = [(x + 1) for x in range(10)]

tissues_data_points = []
data_point = {}

for i in range(100):
    data_point['tissue_info'] = random.choice(tissue_info)
    data_point['date_received'] = str(datetime.date(random.randint(2000,2020), random.randint(1,12), random.randint(1,28)))
    data_point['date_discarded'] = "None"
    data_point['stored_freezer'] = random.choice(stored_freezer)
    data_point['stored_box'] = random.choice(stored_box)
    tissues_data_points.append(data_point)
    

with open('/home/alina/Learning_to_Code/WebDev/Inventory/lab_inventory/tissues_data_points.json', 'w') as f:
    json.dump(tissues_data_points, f)


