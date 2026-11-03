if operacion == "División" and b == 0:
        print(f"\n[!] Operación: {operacion}")
        print(f"[!] {a} / {b} = {resultado}")
    else:
        simbolo = {"Suma": "+", "Resta": "-", "Multiplicación": "*", "División": "/"}
        print(f"\n[✓] Operación: {operacion}")
        print(f"[✓] {a} {simbolo[operacion]} {b} = {resultado}")