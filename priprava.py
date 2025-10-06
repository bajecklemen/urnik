# predelava podatkov iz csv v javascript za urnik
# podatke zapiše v datoteko data.js

from tkinter import filedialog
datoteka_v = filedialog.askopenfilename(title="Izberi datoteko s podatki")
datoteka_i = filedialog.asksaveasfilename(title="Kam shranim")

with open(datoteka_v, 'r', encoding='utf-8') as vhod, open(datoteka_i, 'w', encoding='utf-8') as izhod:
    vrstice = vhod.readlines()
    izhod.write("podatki = new Array("+str(len(vrstice))+");\n")
    razredi = []
    ucitelji = []
    ucilnice = []
        
    for i in range(len(vrstice)):
        izhod.write("podatki["+str(i)+"] = new Array(7);\n")
        v = vrstice[i].split(",")
        razredi.append(v[1])
        ucitelji.append(v[2])
        ucilnice.append(v[4])               
        for j in range(7):
            izhod.write("podatki["+str(i)+"]["+str(j)+"] = "+ ("\"\"" if v[j]== '' else v[j])+"\n")
    y = set(razredi) - set([''])
    izhod.write("razredi = new Array("+str(len(y))+");\n")
    i = 0
    for x  in y:
        izhod.write("razredi["+str(i)+"] = "+x+";\n")
        i += 1

    y = set(ucitelji) - set([''])
    izhod.write("ucitelji = new Array("+str(len(y))+");\n")
    i = 0
    for x  in y:
        izhod.write("ucitelji["+str(i)+"] = "+x+";\n")
        i += 1

    y = set(ucilnice) - set([''])
    izhod.write("ucilnice = new Array("+str(len(y))+");\n")
    i = 0
    for x  in y:
        izhod.write("ucilnice["+str(i)+"] = "+x+";\n")
        i += 1

print("OK")

        
    
    
