#!/usr/bin/python3

import csv

f = open("filmes.ttl", "w")

with open('filmes.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:

        if line_count == 0:

            line_count+=1

        else:

            titulo = row[0]
            id = titulo.replace(' ', '')

            diretores = row[1]
            arrayDiretores = diretores.split(';')

            paises = row[3]
            arrayPaises = paises.split(';')

            f.write(f'###  http://www.semanticweb.org/ricardo/ontologies/2020/2/cinema#{id}\n')
            f.write(f':{id} rdf:type owl:NamedIndividual ,\n')
            f.write('        :Filme ;\n')
            for i in range(len(arrayDiretores)):
                diretor = arrayDiretores[i].replace(' ', '')
                f.write(f'    :temRealizador :{diretor} ;\n')
            pais = arrayPaises[0].replace(' ', '')
            f.write(f'    :temPaisOrigem :{pais} .\n')
            f.write('\n')

            line_count+=1

    print(f'Processed {line_count} lines!')