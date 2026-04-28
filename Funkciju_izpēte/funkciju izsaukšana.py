# Importē visus piemēru failus, lai varētu izmantot tajos definētās funkcijas
import piemērs1
import piemērs2
import piemērs3
import piemērs4
import piemērs5
import piemērs6
import piemērs7
import piemērs8
import piemērs9
import piemērs10
import piemērs11
import piemērs12
import piemērs13
import piemērs14
import piemērs15

print("===========================================================================================")
print("                                    FUNKCIJU IZVĒLNE")
print("===========================================================================================")
print("1 - Kvadrātsaknes no 1;4;256;49;15.")
print("2 - Cos vērtības no 0;-1;10;360.")
print("3 - Gausa sadalījums ar 100 un 50.")
print("4 - Nejaušo skaitļu ģeneratora pašreizējais stāvoklis.")
print("5 - Atgriež nejaušu veselu skaitli, kas ir 50 bitus garš.")
print("6 - Atgriež veselu skaitli no 1 līdz 20.")
print("7 - Atgriež nejaušu skaitli starp diviem norādītajiem skaitļiem 10 un 60, taču tuvāk 50.")
print("8 - Atgriež nejaušu skaitli(ar decimāldaļām) starp 2 un 222.")
print("9 - Atgriež nejaušu skaitli (ar decimāldaļām) no 0 līdz 1")
print("10 - Atgriež sarakstu ar noteiktu skaitu nejauši atlasītu elementu.")
print("11 - Ņem sarakstu, un pārkārto elementu secību.")
print("12 - Atgriež sarakstu ar nejauši izvēlētiem elementiem.")
print("13 - Atgriež nejauši izvēlētu elementu no norādītā saraksta")
print("14 - Atgriež nejauši izvēlētu elementu no 12 līdz 13567")
print("15 - Pielāgo nejaušo skaitļu ģeneratora sākuma numuru uz 10")
print("===========================================================================================")

while True:
    # Pārbaude, lai pārliecinātos, ka lietotājs ievada skaitli
    try:
        skaitlis = int(input("Ievadi skaitli no 1 līdz 15, lai izvēlētos funkciju: "))
    except ValueError:
        print("Vai tu zini, kas ir skaitlis?!")
        continue
    # Ja skaitlis ir diapazonā, izsauc atbilstošo funkciju
    if skaitlis == 1:
        piemērs1.funkcija()
    elif skaitlis == 2:
        piemērs2.funkcija()
    elif skaitlis == 3:
        piemērs3.funkcija()
    elif skaitlis == 4:
        piemērs4.funkcija()
    elif skaitlis == 5:
        piemērs5.funkcija()
    elif skaitlis == 6:
        piemērs6.funkcija()
    elif skaitlis == 7:
        piemērs7.funkcija()
    elif skaitlis == 8:
        piemērs8.funkcija()
    elif skaitlis == 9:
        piemērs9.funkcija()
    elif skaitlis == 10:
        piemērs10.funkcija()
    elif skaitlis == 11:
        piemērs11.funkcija()
    elif skaitlis == 12:
        piemērs12.funkcija()
    elif skaitlis == 13:
        piemērs13.funkcija()
    elif skaitlis == 14:
        piemērs14.funkcija()
    elif skaitlis == 15:
        piemērs15.funkcija()
     # Ja skaitlis nav diapazonā, izvada kļūdas ziņojumu un atsāk funkciju no sākuma
    else:
        print("Nederīgs skaitlis!")
        continue
    # Piedāvā vai lietotājs vēlas izmēģināt citu funkciju
    atkārtot = input("Vai vēlies izmēģināt citu funkciju? (y/n): ")
    # Ja lietotājs izvēlas "y", funkcija tiek atsākta, ja "n" programma beidzas
    if atkārtot == "y":
        continue
    else:
        print("Nu tad nē :(.")
        break