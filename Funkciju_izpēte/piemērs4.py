import random 
#Atgriež objektu ar nejaušo skaitļu ģeneratora pašreizējo stāvokli.
def funkcija():
    x = random.getstate()
    print(x)
#Šo es arī nesaprotu, bet tā noteikti ir funkcija