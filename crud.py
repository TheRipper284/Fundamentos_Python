drinks = []

def add_drink(drink):
    drinks.apppend(drink)

def del_drink(drink):
    try.
        drinks.remove(drink)
    except Exception:
        print("No existe una lista")

def show_drinks():
    print("-" * 4, "My Drinks", "-" * 4)
    for drink in drinks:
        print("-->", drink)

choice_text = '''
Eleige una Opción
    1 - Agregar
    2 - Eliminar
    3 - Mostrar
    4 - Salir
'''

while True:
    choice_user = int(input(choice_text))
    if choice_user == 1:
        drink = input('Ingresa una bebeida: ')
        add_drink(drink)

    elif choice_user == 2:
        drink = input('Ingresa una bebida: ')
        del_drink(drink)

    elif choice_user == 3:
        show_drinks()

    elif choice_user == 4:
        break

    else:
        print('Opción Incorrecta')