import zmq
import time

context = zmq.Context()
print("")
print("CONNESSIONE AL SERVER DI DAVIDE…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("INIZIO CHAT CON BUDINO")
MAGGY = "MAGGY: "
text = input("Maria Chiara: ")
B_t = MAGGY + text
socket.send(B_t.encode())
message = str(socket.recv())
print(message.replace("b", ""))
while True:
    text = input("Maria Chiara: ")
    B_t = MAGGY + text
    socket.send(B_t.encode())      #MANDA
    message = str(socket.recv())   #RICEVI
    print(message.replace("b", ""))
