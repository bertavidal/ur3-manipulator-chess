import random
import socket
import time

# Dirección IP del robot UR
HOST = "10.10.73.239"

# Puerto del servidor en el robot
PORT = 30002

# Conexión via socket a la controladora del robot
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Scripts para abrir y cerrar la pinza
Abrir_pinza = 'pinza40UR3.py'
Cerrar_pinza = 'pinza10UR3.py'

# Función para enviar una trayectoria en espacio de configuraciones a la controladora del robot
def send_joint_path(path, sock):
    for joint_config in path:
        print(joint_config)
        sock.send(f"movej({joint_config}, a=0.5, v=0.5)".encode() + "\n".encode())
        time.sleep(1.1)

# Trayectoria -- configuraciones (variables articulares, en radianes)
posicion_inicial = [[0.0344,-3.0629,1.4657,-1.4601,1.5753,0.0024]]

posicion_intermedia = [[0.1952, -2.7273, 1.4251, -1.8327, 1.2942, 0.0030]]

pieza1 = [[-0.4182, -2.0235, -2.1696, 0.2194, 1.8185, -0.3072]]
pieza1_elevada = [[-0.4198, -1.8776, -2.1238, 0.0268, 1.8211, -0.3093]]

pieza2 = [[-0.1172, -1.8904, -2.4666, 0.4158, 1.6137, -0.0867]]
pieza2_elevada = [[-0.1162, -1.6812, -2.4116, 0.1511, 1.6123, -0.0860]]

pieza3 = [[0.2627, -1.8261, -2.6847, 0.5445, 1.3510, 0.1896]]
pieza3_elevada = [[0.2643, -1.4859, -2.6015, 0.1205, 1.3491, 0.1906]]

linia_recta = [
    [0.0535, -2.7410, 1.3708, -1.7655, 1.4352, 0.0041],
    [-0.0779, -2.7527, 1.3045, -1.6875, 1.5663, 0.0049],
    [-0.1967, -2.7592, 1.2241, -1.6008, 1.6851, 0.0056],
    [-0.3031, -2.7581, 1.1281, -1.5057, 1.7915, 0.0062],
    [-0.3976, -2.7472, 1.0133, -1.4016, 1.8860, 0.0068],
    [-0.4815, -2.7232, 0.8740, -1.2861, 1.9699, 0.0073]
]

# Bucle principal
with open(Abrir_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)
final = False

# Se mueve a la posición inicial
send_joint_path(posicion_inicial, sock)
time.sleep(3.5)

while not final:

    # Escoje una de las tres piezas y se mueve hasta ella
    pieza = random.randint(1,3)
    if pieza == 1:
        pieza = pieza1
        pieza_elevada = pieza1_elevada
    elif pieza == 2:
        pieza = pieza2
        pieza_elevada = pieza2_elevada
    else:
        pieza = pieza3
        pieza_elevada = pieza3_elevada

    send_joint_path(pieza_elevada, sock)
    time.sleep(8)
    send_joint_path(pieza, sock)
    time.sleep(1.5)

    # Coje la pieza
    with open(Cerrar_pinza, 'rb') as f: sock.sendall(f.read())
    time.sleep(1)

    send_joint_path(pieza_elevada, sock)
    time.sleep(1.5)

    # Se mueve a la posición intermedia (enseña la pieza)
    send_joint_path(posicion_intermedia, sock)
    time.sleep(8)

    respuesta = input("¿Es el rey? (Si/No)")
    if respuesta == 'Si': # Se mueve a la posición final y termina
        send_joint_path(linia_recta, sock)
        time.sleep(6)
        final = True

    else: # Devuelve la pieza
        send_joint_path(pieza_elevada, sock)
        time.sleep(8)
        send_joint_path(pieza, sock)
        time.sleep(1.5)

        with open(Abrir_pinza, 'rb') as f: sock.sendall(f.read()) #abrir pinza
        time.sleep(1)

        # Vuelve a la posición inicial
        send_joint_path(posicion_inicial, sock)
        time.sleep(9)

# Mensaje que se imprime cuando se finaliza la ejecución de la trayectoria
print("Trayectoria finalizada")
data = sock.recv(1024)

# Se cierra la conexión
sock.close()