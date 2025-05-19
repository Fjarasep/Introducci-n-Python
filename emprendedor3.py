print("Cálculo de utilidades y comparación con el año anterior")

# Entradas
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios normales: "))
GT = float(input("Ingrese el gasto total: "))
Uanterior = float(input("Ingrese las utilidades del año anterior: "))

# Validación
if Uanterior == 0:
    print("Error: Las utilidades del año anterior no pueden ser cero para calcular la razón.")
else:
    # Cálculo
    Uactual = P * U - GT
    Razon = Uactual / Uanterior

    # Resultado
    print(f"Las utilidades actuales son: {Uactual:.2f}")
    print(f"La razón entre utilidades actuales y del año anterior es: {Razon:.2f}")