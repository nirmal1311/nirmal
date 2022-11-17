import socket
import os
import time

BUFFER_SIZE = 32                

HOST = 'localhost'              
PORT = 12345                    
server_addr = (HOST,PORT)       
print("Enter the corresponding number to download book:")
print("1. Atlas Shrugged by Ayn Rand")
print("2. Don Quixote by Miguel de Cervantes")
file_number = int(input())

if(file_number == 1):
    file_name = "Atlas Shrugged.txt"
elif(file_number == 2):
    file_name = "Don Quixote.txt"

file = file_name.split('.')                 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    start = time.time()                                                                 
    sock.sendto(f"{file_name}".encode(),server_addr)                                    
    file_name = file[0] + "+Protocol=UDP" + "+" + str(os.getpid()) + "." + file[1]      

    with open(file_name, 'wb') as f:                                                    
        print('Receiving Data')
        while True:
            sock.settimeout(2)                                                          

            byte, server = sock.recvfrom(BUFFER_SIZE)                                   
            
            if not byte:
                break

            f.write(byte)                                                               
except:                                                                                 
    print("Timeout Occurred")
    end = time.time()                                                                   
    print(f"Time taken to download: {end - start - 2} sec")                             
    print("Downloaded ",file_name)

    file_stat = os.stat(file_name)                                                       
    file_size = file_stat.st_size

    throughput = round((file_size*0.001)/(end - start), 3)                              
    print("Throughput: ",throughput,"kB/s")
    
    sock.close()                                                                        

finally:
    sock.close()
    
