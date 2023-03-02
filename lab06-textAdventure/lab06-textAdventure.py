class Room:
    def __init__(self, description = "", north=0, south=0, east=0, west=0):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():

    room_list = []
    room = Room("Estas en la sala inicial. Miras a tu alrededor y tienes dos caminos: \nAl sur, hacia un camino oscuro cubierto por las copas de los árboles. \nO al este, hacia un río que discurre pendiente abajo.", None, 1, 2, None)
    room_list.append(room)
    room = Room("Llegas al bosque oscuro cubierto por los árboles, en completa oscuridad solo ves dos salidas del bosque: \nAl este \nAl norte", 0, None, 3, None)
    room_list.append(room)
    room = Room("Llegas a un camino por donde discurre un río cuesta abajo. \nPuedes cruzarlo e ir al este \nCruzarlo para ir al oeste \nO seguir la corriente para ir al sur", None, 3, 4, 0)
    room_list.append(room)
    room = Room("Has entrado en un bosque mágico que cambia su posición cada poco. Escapa rápidamente: \nAl norte \nAl este \nAl oeste", 2, None, 5, 1)
    room_list.append(room)
    room = Room("Continuas caminando y llegas a un barranco. No tienes más salidas que ir: \nAl sur \nAl oeste", None, 5, None, 2)
    room_list.append(room)
    room = Room("Has entrado en un claro donde se encuentra una cabaña completamente cerrada. A donde vas: \nAl norte \nAl sur", 4, 3, None, None)
    room_list.append(room)

    current_room = 0

    #print(room_list[0])
    #print(room_list[current_room].description)

    done = False
    while(done!=True):
        print("\n")
        print(room_list[current_room].description)
        accion = input("¿Qué quieres hacer? (n,s,e,w o Salir): ")
        if(accion == ("n" or "N" or "North" or "NoRtH")):
            if(room_list[current_room].north == None):
                print("No hay habitaciones por ahí")
            else:
                next_room = room_list[current_room].north
                current_room = next_room
                print("Has ido al norte")
        elif (accion == ("s" or "S" or "South" or "SoUtH")):
            if (room_list[current_room].south == None):
                print("No hay habitaciones por ahí")
            else:
                next_room = room_list[current_room].south
                current_room = next_room
                print("Has ido al sur")
        elif (accion == ("e" or "E" or "East" or "EaSt")):
            if (room_list[current_room].east == None):
                print("No hay habitaciones por ahí")
            else:
                next_room = room_list[current_room].east
                current_room = next_room
                print("Has ido al este")
        elif (accion == ("w" or "W" or "West" or "WeSt")):
            if (room_list[current_room].west == None):
                print("No hay habitaciones por ahí")
            else:
                next_room = room_list[current_room].west
                current_room = next_room
                print("Has ido al oeste")
        elif(accion=="Salir"):
            done = True
        else: print("No se que significa eso")

main()
