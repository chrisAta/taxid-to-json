import json

fr = open('./taxonomy-all.tab', 'r')
fw = open('./taxonomy-all.json', 'w')

dic = {}

for line in fr:

    line = line.split('\t')

    taxid = line[0]

    species_name = line[2]

    dic[species_name] = taxid


fw.write(json.dumps(dic, indent=2))