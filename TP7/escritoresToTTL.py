#!/usr/bin/python3

import csv

f = open("escritores.ttl", "w")

with open('escritores.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:

        if line_count == 0:

            line_count+=1

        else:

            nome = row[0]
            id = nome.replace(' ', '')

            f.write(f'###  http://www.semanticweb.org/ricardo/ontologies/2020/2/cinema#{id}\n')
            f.write(f':{id} rdf:type owl:NamedIndividual ,\n')
            f.write('        :Pessoa .\n')
            f.write('\n')

            line_count+=1

    print(f'Processed {line_count} lines!')