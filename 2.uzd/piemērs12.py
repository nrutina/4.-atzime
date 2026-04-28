import random 
#Atgriež sarakstu ar nejauši izvēlētiem elementiem no norādītā saraksta

def funkcija():
    saraksts = ["helihopters", "izglābj", "īstu","jaguāru"]
    print(random.choices(saraksts, k = 10))