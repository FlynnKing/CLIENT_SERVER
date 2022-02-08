import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("")
print("SERVER AVVIATO")
print("INIZIO CHAT CON MAGGY")
BUDINO = "BUDINO: "
try:
    text = input("Davide: ")
    B_t = BUDINO + text
    socket.send(B_t.encode())  # MANDAsd
except:
    pass
while True:
    message = str(socket.recv())  #RICEVI
    print(message.replace("b", ""))
    text = input("Davide: ")
    B_t = BUDINO + text
    socket.send(B_t.encode())     #MANDA


