
nom = basestring(input("Entrer un nom"))
noml = len(nom)

if noml < 5:
    print("mot de passe solide")
elif noml == 2:
    print("pas solide")
else:
    print ("nul a chier")
