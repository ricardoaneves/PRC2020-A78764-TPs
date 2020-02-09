import csv

with open('PRI2019.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	file = open('alunos.ttl', 'w')
	next(csv_reader)
	for row in csv_reader:
		file.write('###  http://www.semanticweb.org/ricardoneves/ontologies/2020/1/untitled-ontology-2#' + row[0] + '\n')
		file.write(':' + row[0] + ' rdf:type owl:NamedIndividual ,\n')
		file.write('                 :Aluno ;\n')
		file.write('        :frequenta :prc ,\n')
		file.write('                   :spln ;\n')
		file.write('        :ident "' + row[0] + '"^^xsd:string ;\n')
		file.write('        :nome "' + row[1] + '"^^xsd:string ;\n')
		file.write('        :email "' + row[0] + '@alunos.uminho.pt' + '"^^xsd:string ;\n')
		file.write('        :curso "' + 'MIEI' + '"^^xsd:string .\n')
		file.write('\n')
	file.close()
	print('OK!')