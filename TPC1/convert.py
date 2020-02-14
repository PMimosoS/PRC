import json

with open('convertcsv.json') as json_file:
    data = json.load(json_file)
    file = open("salaAulaInf.ttl", "a")
    for i in range(1, len(data)):
        file.write("### http://prc.di.uminho.pt/2020/salaAulaInf#" +
                   (data[i]['A']).lower() + '\n')
        file.write(":" + (data[i]['A']).lower() +
                   " rdf:type owl:NamedIndividual, \n")
        file.write("<http://prc.di.uminho.pt/2020/salaAula#Aluno> ; \n")
        file.write(
            "<http://prc.di.uminho.pt/2020/salaAula#frequenta> <http://prc.di.uminho.pt/2020/salaAula#prc> ; \n")
        file.write("<http://prc.di.uminho.pt/2020/salaAula#ident> " +
                   "\"" + data[i]['A'] + "\"" + " ; \n")
        file.write("<http://prc.di.uminho.pt/2020/salaAula#nome> " +
                   "\"" + data[i]['B'] + "\"" + " .")
        file.write("\n \n")
