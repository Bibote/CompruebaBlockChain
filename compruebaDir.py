
from os import listdir
from os.path import isfile, join
import comprobador
print("Nombre del fichero:")
fichero=input()
print("Nombre del directorío:")
directorio=input()
mypath="SGSSI-22.Lab06.CB.02.Candidatos/"
onlyfiles = [f for f in listdir(directorio) if isfile(join(directorio, f))]
maxcero=""
maxnum=0
for file in onlyfiles:
    num=comprobador.comprobar(fichero,directorio+file)
    if(num>maxnum):
        maxnum=num
        maxcero=file
print(maxcero)
print(maxnum)
