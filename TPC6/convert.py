import json


with open('sparql.json') as json_file:
    data = json.load(json_file)
    data = data["results"]["bindings"]
    listaFilmes = {}
    listaLinguas = set()
    listaPaises = set()
    listaDirectores = set()
    listaCompositores = set()
    listaEscritores = set()
    for i in range(1, len(data)):
        directores = set()
        escritores = set()
        compositores = set()
        linguas = set()
        nomeFilme = data[i]['fname']['value']
        resumo = (data[i]['abs']['value'])
        directores.add((data[i]['dir']['value'].split("/"))[-1])
        listaDirectores.add((data[i]['dir']['value'].split("/"))[-1])
        compositores.add((data[i]['music']['value'].split("/"))[-1])
        listaCompositores.add((data[i]['music']['value'].split("/"))[-1])
        escritores.add((data[i]['writer']['value'].split("/"))[-1])
        listaEscritores.add((data[i]['writer']['value'].split("/"))[-1])
        paisOrigem = (data[i]['country']['value'])
        listaPaises.add(data[i]['country']['value'])
        linguas.add(data[i]['lang']['value'])
        listaLinguas.add(data[i]['lang']['value'])
        if nomeFilme in listaFilmes.keys():
            listaFilmes[nomeFilme]["directores"].update(directores)
            listaFilmes[nomeFilme]["escritores"].update(escritores)
            listaFilmes[nomeFilme]["compositores"].update(compositores)
            listaFilmes[nomeFilme]["linguas"].update(linguas)
        else:
            listaFilmes[nomeFilme] = {"nomeFilme": nomeFilme, "resumo": resumo, "directores": directores, "escritores": escritores,
                                      "compositores": compositores, "paisOrigem": paisOrigem, "linguas": linguas}

file = open("cinema.ttl", "a")

for i in listaFilmes:
    for d in listaFilmes[i]["directores"]:
        file.write("###  http://prc.di.uminho.pt/2020/Cinema#" + d + "\n:" + d +
                   " rdf:type owl:NamedIndividual , \n\t\t\t\t\t\t :Pessoa ; \n\t\t\t\t :realizou :" + listaFilmes[i]["nomeFilme"].replace(" ", "_") + " . \n\n")

    for e in listaFilmes[i]["escritores"]:
        file.write("###  http://prc.di.uminho.pt/2020/Cinema#" + e + "\n:" + e +
                   " rdf:type owl:NamedIndividual , \n\t\t\t\t\t\t :Pessoa ; \n\t\t\t\t :escreveu :" + listaFilmes[i]["nomeFilme"].replace(" ", "_") + " . \n\n")

    for c in listaFilmes[i]["compositores"]:
        file.write("###  http://prc.di.uminho.pt/2020/Cinema#" + c + "\n:" + c +
                   " rdf:type owl:NamedIndividual , \n\t\t\t\t\t\t :Pessoa ; \n\t\t\t\t :compos :" + listaFilmes[i]["nomeFilme"].replace(" ", "_") + " . \n\n")

    file.write(":" + i.replace(" ", "_") + " rdf:type owl:NamedIndividual ,\n")
    file.write("\t\t\t\t :Filme ;\n")
    file.write("\t\t\t:temPaisOrigem :" +
               listaFilmes[i]["paisOrigem"].replace(" ", "_") + ".\n\n")


for i in listaLinguas:
    file.write("###  http://prc.di.uminho.pt/2020/Cinema#"+i+"\n:" +
               i+" rdf:type " + "owl:NamedIndividual ,\n"+"\t\t\t :Lingua .\n\n")

for i in listaPaises:
    file.write("###  http://prc.di.uminho.pt/2020/Cinema#"+i.replace(" ", "_")+"\n:" +
               i.replace(" ", "_")+" rdf:type " + "owl:NamedIndividual ,\n"+"\t\t\t :Pais .\n\n")
