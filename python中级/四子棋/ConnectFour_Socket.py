# 68996560 Zhengyi Xu 19758650 Lukun Han
import socket
NET=[]

def _read_host():
    '''
    receive user input host
    check whether it is valid
    if not request user input again
    in the end, return a valid host
    '''
    while True:
        print('Enter host location which you want to connect')
        host = input('Host: ').strip()

        if host == '':
            print('Please specify a host (either a name or an IP address)')
        else:
            return host

def _read_port():
    '''
    receive user input host
    check whether it is valid
    if not request user input again
    in the end, return a valid port
    '''
    while True:
        try:
            print('Enter port you wanted connect;   Ports must be an integer between 0 and 65535')
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def _read_name():
    '''
    receive user input host
    check whether it is valid
    if not request user input again
    in the end, return a valid name
    '''
    while True:
        print('Enter your server name')
        name=str(input()).strip()
        LIST=name.split()
        if len(LIST)>1:
            print('No blank space')
        else:
            return name

def start_connect():
    '''
    receive host,port
    try connect
    connected
    create send and receive object
    store them in NET list
    '''
    global NET
    while True:
        try:
            GameConnect=socket.socket()
            host=_read_host()
            port=_read_port()
            GameConnect.connect((host,port))
            GameConnect_input=GameConnect.makefile('r')
            GameConnect_output=GameConnect.makefile('w')
        except:
            print('Cannot connect to input host, Please check your input host and port')
            continue
        else:
            break
    NET=[GameConnect_input,GameConnect_output,GameConnect]

def end_connect():
    '''
    close all objects in NET list
    '''
    global NET
    try:
        for x in NET:
            x.close()
    except:
        pass

def send_message(message:str):
    '''
    send message to host
    '''
    global NET
    try:
        NET[1].write(message+'\r\n')
        NET[1].flush()
    except:
        pass

def recv_message():
    '''
    receive message from host
    '''
    try:
        return NET[0].readline()[:-1]
    except:
        pass