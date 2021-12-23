from sklearn import linear_model
import pandas
import numpy
import matplotlib
import matplotlib.pyplot as plt
import csv
import time
import json
from Bio.KEGG import REST

human_pathways = REST.kegg_list ("pathway", "hsa").read()

repair_pathways = []

temp = str(input("Input the desired pathway: "))
for line in human_pathways.rstrip().split("\n"):
    entry, description = line.split("\t")
    if temp in description.lower():
        repair_pathways.append(entry)
        print(entry, description)

print (repair_pathways)

repair_genes = []

for pathway in repair_pathways:
    pathway_file = REST.kegg_get(pathway).read()

    current_section = None
    for line in pathway_file.rstrip().split("\n"):
        section = line [:12].strip()
        if not section == "":
            current_section = section

            if current_section == "GENE":
                gene_identifiers , gene_description = line[12:].split("; ")
                gene_id, gene_symbol = gene_identifiers.split()
                if not gene_symbol in repair_genes:
                    repair_genes.append(gene_symbol)

print ("There are %d repair pathways and %d repair genes." %(len(repair_pathways), len(repair_genes)))
print ("The genes are:")
print(", ".join(repair_genes))

