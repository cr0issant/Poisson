import time
i = 0

while i == 0:
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
	temperature = float(temperaturedata[2:])
	# Mettre un chiffre apres la virgule
	temperature = temperature / 1000
	print ("Temperature : ")
	print (temperature)
