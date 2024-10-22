def puntuacion():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point <= 0 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')
    
def resultado():
        print('Resultados hasta la fecha.')
        read_file = open("data.txt", "r")
        print(read_file.read())
        read_file.close()
        
def menu():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()
        if num == '1':
            puntuacion()
        elif num == '2':
            resultado()
        elif num == '3':
            print('Finalizando')
            break
        else:
            print('Introduzca un número del 1 al 3')
        
if __name__ == "__main__":
    menu()