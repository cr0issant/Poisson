import time
import os

TemperatureLast = 0
TemperatureNow = 0
i = 0

while i < 2:
	time.sleep(1)
	tfile = open("/sys/bus/w1/devices/28-031680cfc3ff/w1_slave")
	# Lire tout le texte du dossier.
	text = tfile.read()
	# Fermer le fichier apres qu'il ai ete lu.
	tfile.close()
	# Supprimer la seconde ligne.
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	# Supprimer le "t="
	TemperatureNow = float(temperaturedata[2:])
	# Mettre un chiffre apres la virgule
	TemperatureNow = TemperatureNow / 1000
	print ("Temperature : ")
	print (TemperatureNow)
	
	if TemperatureNow == TemperatureLast :
		i+=1
		print ("TemperatureNow == TemperatureLast")

	TemperatureLast = TemperatureNow

cmd = "raspistill -o " + time.strftime("%Y-%d-%m_%Hh%Mm%Ss") + ".jpg -t 1000 -a 4 -a 'CodeBarreFournisseur | CodeBarreAdminresto | %Y-%m-%d %X | Temperature = " + "{:.3f}".format(TemperatureNow) + " C'"
os.system(cmd)

