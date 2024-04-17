# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 10
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
    print(f"Numarul {number} este pozitiv!")
else:
    print(f"Numarul {number} este negativ!")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0 and number % 2 == 0: 
    print(f"Numarul {number} este par!")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
num = 3
if num > 0 and num % 2 == 0: 
    print(f"Numarul {num} este par!")
else:
    print(f"Numarul {num} este impar!")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = "Coding in Phyton"
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Phyton" in text:
    print("Variabila text contine acest cuvant! -> Phyton")
else:
    print("Variabila text nu contine acest cuvant! -> Phyton")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Java" in text:
    print("Variabila text contine acest cuvant! -> Java")
else:
    print("Variabila text nu contine acest cuvant! -> Java")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Phyton" in text:
    print("Variabila text contine cuvantul Phyton!")
elif "Java" in text:
    print("Variabila text contine cuvantul Java!")
else:
    print("Variabila text nu contine nici Phyton, nici Java!")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Phyton" and "Java" in text:
    print("Variabila text contine atat cuvantul Phyton cat si Java!")
elif "Phyton" or "Java" in text:
    print("Variabila text contine doar un cuvant comun!")
else:
    print("Variabila text nu contine nici Phyton, nici Java!")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = int(input("Selectati un numar: "))
print("Tipul numarului introdus este:", type(number))

if number == 1:
    print(f"Numarul introdus este: Unu -> ({number})")
elif number == 2:
    print(f"Numarul introdus este: Doi -> ({number})")
elif number == 3:
    print(f"Numarul introdus este: Trei -> ({number})")
elif number == 4:
    print(f"Numarul introdus este: Patru -> ({number})")
elif number == 5:
    print(f"Numarul introdus este: Cinci -> ({number})")  
else:
    print("Eroare! Introdu un numar de la 1 la 5")          

# CODUL TĂU VINE MAI SUS:


