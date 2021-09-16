#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:52:22 2021

@author: alina

Create data points to fill the database
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

supplies = ['dNTPs 200mM', 'dNTPs 200mM', 'dNTPs 200mM', 'dNTPs 200mM', 'dNTPs 200mM', 'dNTPs 200mM', 'dNTPs 200mM',
            'dNTPs 200mM', 'Zero Blunt TOPO PCR Cloning Kit', 'QIAGEN Multiplex PCR/PCR plus Kits', 'HotStarTaq Master mix Kit',
            'QuantiNova Multiplex PCR Kit', 'QuantiNova Multiplex RT-PCR Kit', 'QIAGEN Multiplex PCR/PCR plus Kits', 'HotStarTaq Master mix Kit',
            'QuantiNova Multiplex PCR Kit', 'QuantiNova Multiplex RT-PCR Kit', 'T4 DNA Ligase', 'BamHI Endonuclease', 'Bglll Endonuclease',
            'Dpnl Endonuclease', 'EcoRI Endonuclease', 'EcoRV Endonuclease', 'Exonuclease I', 'Lambda Exonuclease', 'Platinum SuperFi DNA DNA Polymerase',
            'Platinum II Taq Hot-Start DNA Polymerase', 'Platinum Taq DNA Polymerase', 'Platinum SuperFi DNA DNA Polymerase', 'Platinum II Taq Hot-Start DNA Polymerase',
            'Platinum Taq DNA Polymerase',]

# freezer options
stored_freezer_80 = ['-80/1', '-80/2', '-80/3', '-80/4']
stored_freezer_20 = ['-20/1', '-20/2', '-20/3', '-20/4']

# storage boxes
stored_box = [(x + 1) for x in range(10)]

# to create primers
seqs = ['5-ATGCAGGGGAAACATGATTCAGGAC-3', '5-GTCCTGAATCATGTTTCCCCTGCAC-3', '5-TGCCCTGCTACTGATACTACTCTT-3',
        '5-TGTCATCATTAAACAGAAATACAAA-3', '5-TCAGGTTTCCTCCCTCCGAAGGCGG-3', '5-TAGCTAACTTGGCCTGAAGCCTC-3',
        '5-GTCCAGGCGGTGGTGATGGAGTATA-3', '5-ATGGAGTATAAATGGAGAGGAGCTCT-3', '5-AAAGCGTCTCTGTGTGTTCAGATG-3',
        '5-GCTGCCACAAGCCCTGCAACATCCC-3',]
organism = ['Sl', 'Ha', 'Zm', 'St', 'Os', 'Ta']
primer_num = [(x + 1) for x in range(42)]
strand = ['F', 'R']

def get_box_position(stored_box):
    """Return a str that represents a position in a 10x10 storage box,
    with the format: 'A / 10' .
    """
    col = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    row = random.choice(stored_box)
    return col + ' / ' + str(row)


def create_primer_name(organism, primer_num, strand):
    first = random.choice(organism)
    second = random.choice(primer_num)
    third = random.choice(strand)
    return first + '-' + str(second) + '-' + third


def create_tissue_data_points():
    tissues_data_points = []
    data_point = {}
    for i in range(100):
        data_point['tissue_info'] = random.choice(tissue_info)
        d1 = datetime.date(random.randint(2000,2020), random.randint(1,12), random.randint(1,28))
        d2 = d1 + datetime.timedelta(weeks=78)
        data_point['date_received'] = str(d1)
        data_point['date_discarded'] = str(d2)
        data_point['stored_freezer'] = random.choice(stored_freezer_80)
        data_point['stored_box'] = random.choice(stored_box)
        tissues_data_points.append(data_point)
        data_point = {}   
    return tissues_data_points


def create_dna_data_points():
    dna_data_points = []
    data_point = {}
    for i in range(100):
        data_point['tissue_info'] = random.choice(tissue_info)
        d1 = datetime.date(random.randint(2000,2020), random.randint(1,12), random.randint(1,28))
        d2 = d1 + datetime.timedelta(weeks=104)
        data_point['extraction_date'] = str(d1)
        data_point['date_discarded'] = str(d2)
        data_point['stored_freezer'] = random.choice(stored_freezer_20)
        data_point['stored_box'] = get_box_position(stored_box)
        dna_data_points.append(data_point)
        data_point = {}   
    return dna_data_points


def create_supplies_data_points():
    supplies_data_points = []
    data_point = {}
    for i in range(50):
        data_point['product_name'] = random.choice(supplies)
        data_point['purchase_order'] = i + 100
        d1 = datetime.date(random.randint(2000,2020), random.randint(1,12), random.randint(1,28))
        d2 = d1 + datetime.timedelta(weeks=4)
        d3 = d2 + datetime.timedelta(weeks=104)
        data_point['date_received'] = str(d1)
        data_point['date_opened'] = str(d2)
        data_point['date_discarded'] = str(d3)
        data_point['stored_freezer'] = random.choice(stored_freezer_20)
        supplies_data_points.append(data_point)
        data_point = {}   
    return supplies_data_points


def create_primers_data_points():
    primers_data_points = []
    data_point = {}
    for i in range(300):
        data_point['primer_name'] = create_primer_name(organism, primer_num, strand)
        data_point['primer_seq'] = random.choice(seqs)
        data_point['purchase_order'] = i + 200
        d1 = datetime.date(random.randint(2000,2020), random.randint(1,12), random.randint(1,28))
        d2 = d1 + datetime.timedelta(weeks=2)
        d3 = d2 + datetime.timedelta(weeks=4)
        data_point['date_received'] = str(d1)
        data_point['date_opened'] = str(d2)
        data_point['date_discarded'] = str(d3)
        data_point['stored_freezer'] = random.choice(stored_freezer_20)
        data_point['stored_box'] = get_box_position(stored_box)
        primers_data_points.append(data_point)
        data_point = {}   
    return primers_data_points

# create all data points
tissues_data_points = create_tissue_data_points()
dna_data_points = create_dna_data_points()
supplies_data_points = create_supplies_data_points()
primers_data_points = create_primers_data_points()

# create json files
with open('/home/alina/Learning_to_Code/WebDev/Inventory/lab_inventory/tissues_data_points.json', 'w') as f:
    json.dump(tissues_data_points, f)

with open('/home/alina/Learning_to_Code/WebDev/Inventory/lab_inventory/dna_data_points.json', 'w') as f:
    json.dump(dna_data_points, f)

with open('/home/alina/Learning_to_Code/WebDev/Inventory/lab_inventory/supplies_data_points.json', 'w') as f:
    json.dump(supplies_data_points, f)

with open('/home/alina/Learning_to_Code/WebDev/Inventory/lab_inventory/primers_data_points.json', 'w') as f:
    json.dump(primers_data_points, f)












