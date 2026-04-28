import random 
#atgriež sarakstu ar nejauši izvēlētiem elementiem no norādītā saraksta
sarakstiņš = ["kaķis", "zaķis", "skapis"]

print(random.choices(sarakstiņš, k = 10))