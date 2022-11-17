import socket
choice = int(input("Enter  1.Ip address 2.Website name:"))
if(choice == 1):
    ip_address = input("Enter the ip address : ")
    host = socket.gethostbyaddr(ip_address)
    print(f'The Host name of the {socket.gethostbyname(ip_address)} is : {host[0]}')

elif(choice == 2):
    host_name = input("Enter the Host name to find ip address :")
    print(
        f'The Ip address of the {host_name} is : {socket.gethostbyname(host_name)}')
