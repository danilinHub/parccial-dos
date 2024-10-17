def salario_base():


        salario_base = float(input("Salario base mensual $: "))
        cargo = input("Cargo del empleado: ").lower()
        desempeño = input("Nivel de desempeño: ").lower()

        bonificacion = 0

        if cargo == 'directivo':
            if desempeño == 'alto':
                bonificacion = 0.20 * salario_base
            elif desempeño == 'medio':
                bonificacion = 0.10 * salario_base

        elif cargo == 'operativo':
            if desempeño == 'alto':
                bonificacion = 0.15 * salario_base
            elif desempeño == 'medio':
                bonificacion = 0.05 * salario_base

        total_recibir = salario_base + bonificacion


        print("\n-----Resumen del Pago-----")
        print(f"Cargo: {cargo.capitalize()}")
        print(f"Nivel de Desempeño: {desempeño.capitalize()}")
        print(f"Salario Base: ${int(salario_base)}")
        print(f"Bonificación: ${int(bonificacion)}")
        print(f"Total a Recibir: ${int(total_recibir)}")
        print("------------------------------------")


salario_base()
