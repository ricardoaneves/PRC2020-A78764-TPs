#!/usr/bin/python3

import xml.etree.ElementTree as ET

tree = ET.parse('arquivo-musica-digital.xml')
root = tree.getroot()

file = open('arquivo-musica-digital.ttl', 'w')

for obra in root.findall('obra'):
    file.write('###  http://www.semanticweb.org/ricardo/ontologies/2020/1/arquivo-musica-digital#' + obra.get('id') + '\n')
    file.write(':' + obra.get('id') + ' rdf:type owl:NamedIndividual ;\n')
    if obra.find('titulo') is not None:    
        file.write('    :titulo "' + obra.find('titulo').text + '"^^xsd:string ;\n')
    if obra.find('tipo') is not None:
        file.write('    :tipo "' + obra.find('tipo').text + '"^^xsd:string ;\n')
    if obra.find('compositor') is not None:
        file.write('    :compositor "' + obra.find('compositor').text + '"^^xsd:string ;\n')
    if obra.find('inf-relacionada/video') is not None:
        file.write('    :video "' + obra.find('inf-relacionada/video').get('href') + '"^^xsd:string ;\n')
    for instrumento in obra.findall('instrumentos/instrumento'):
        file.write('    :éTocadaPor :' + obra.get('id') + '-' + instrumento.find('designacao').text.replace(" ", "") + ' ;\n')
    file.write('.\n\n')

    for instrumento in obra.findall('instrumentos/instrumento'):
        file.write('###  http://www.semanticweb.org/ricardo/ontologies/2020/1/arquivo-musica-digital#' + obra.get('id') + '-' + instrumento.find('designacao').text.replace(" ", "") +  '\n')
        file.write(':' + obra.get('id') + '-' + instrumento.find('designacao').text.replace(" ", "") + ' rdf:type owl:NamedIndividual ;\n')
        file.write('    :designacao "' + instrumento.find('designacao').text + '"^^xsd:string ;\n')
        file.write('.\n\n')

        file.write('###  http://www.semanticweb.org/ricardo/ontologies/2020/1/arquivo-musica-digital#' + instrumento.find('partitura').get('path') + '\n')
        file.write(':' + instrumento.find('partitura').get('path') + ' rdf:type owl:NamedIndividual ;\n')
        file.write(':define :' + obra.get('id') + '-' + instrumento.find('designacao').text.replace(" ", "") + ' ;\n')
        if instrumento.find('partitura').get('voz') is not None: 
            file.write('    :voz "' + instrumento.find('partitura').get('voz') + '"^^xsd:string ;\n')
        if instrumento.find('partitura').get('type') is not None: 
            file.write('    :tipo "' + instrumento.find('partitura').get('type') + '"^^xsd:string ;\n')
        file.write('.\n\n')

file.close()
print('OK!')