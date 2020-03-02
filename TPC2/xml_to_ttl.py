import xml.etree.ElementTree as ET
import sys
import unidecode

sys.stdout = open("arquivoMusical.ttl", "a")

tree = ET.parse('arquivo-musica-digital.xml')
root = tree.getroot()
listaIntrumentos = set()

for obra in root.findall('obra'):
    instrumentos = obra.find('instrumentos')
    for instrumento in instrumentos.findall('instrumento'):
        designacao = instrumento.find('designacao').text
        designacao = designacao.replace(" ", "_")
        listaIntrumentos.add(unidecode.unidecode(designacao))

for ins in listaIntrumentos:
    print("###  http://prc.di.uminho.pt/2020/obrasMusicais#" + ins.lower())
    print(":" + ins.lower() + " rdf:type owl:NamedIndividual ,")
    print("\t \t :Intrumento ;")
    print("\t :nomeIntrumento " + "\"" + ins + "\"" + " .")
    print("\n")


for obra in root.findall('obra'):
    numero = obra.get('id')
    titulo = obra.find('titulo').text
    tipo = obra.find('tipo').text
    compositor = obra.find('compositor').text
    print(":" + numero + " rdf:type owl:NamedIndividual ,")
    print("\t \t :Obra ;")
    print("\t :compositor " + "\"" + compositor + "\"" + " ;")
    print("\t :tipo " + "\"" + tipo + "\"" + " ;")
    print("\t :titulo " + "\"" + titulo + "\"" + " .")
    print("\n")
    i = 1
    for instrumento in instrumentos.findall('instrumento'):
        print(":" + numero + "_" + "partitura" +
              str(i) + " rdf:type owl:NamedIndividual ,")
        print("\t \t :Partitura ;")
        print("\t :estaContidaNa :" + numero + " ;")
        designacao = instrumento.find('designacao').text
        designacao = designacao.replace(" ", "_")
        print(" \t :tem :" + unidecode.unidecode(designacao.lower()) + " .\n")
        i = i+1
