# 68996560 Zhengyi Xu 19758650 Lukun Han
import ConnectFour_Socket
import GameLogic
import ConnectFour_Console

'''
Most people use receive message from Host to control whole structure, like if recv_message=="READY"
I think it is not so secure and I find our protocal show us 
after login procedure
READY
user send 1
host response 3
so we can use number to control them
'''

        
def ConnectFour_Online():
    '''
    Entire structure of ConnectFour_Online version game
    '''
    while True:
        ConnectFour_Socket.start_connect() # Receive user input host and port, start connect
        name=ConnectFour_Socket._read_name() # Store user input login name
        login='I32CFSP_HELLO '+name # Convert name form basing on protocal
        ConnectFour_Socket.send_message(login) # Send name, start login

        Confirmation=ConnectFour_Socket.recv_message() # I add this confirmation procedure because when we can connect to a wrong but leagal port
        if Confirmation!='WELCOME '+name:
            command=input('Wrong Connect!!!\nEnsure you give right host and port\nDo you want to play a console game, or try to connect again.\nInput Y(es) or N(ot): ')
            if command=='Y': # give user a selection to play a console game(LOL)
                ConnectFour_Console.connectfour_console()
            elif command=='N':
                continue
        else:
            break

    print(Confirmation) # Receive confirmation, print "Welcome name"
    ConnectFour_Socket.send_message('AI_GAME') # Request ConnectFour game with AI
    a=-1 # I use number to control whole structure because I think It will be more secure
    ConnectFour_Console.ShowChessTable() # Print simple interface help user detect chess table
    while True: # In Concole module if there are no winner I set Winner value=10
        a+=1 # Initialize turn number
        try: # Use try in case of some unexpected error
            if a%4==1: # receive "READY" means user should move
                GameLogic.select_method() # request method from user input
                GameLogic.select_column() # request column from user input
                ConnectFour_Console.ResponseACT() # map chesspiece to chess table store in Console
                ConnectFour_Console.ShowChessTable() # print refreshed chess table
                move=GameLogic.METHOD+' '+str(int(GameLogic.COLUMN)+1) # convert user input into legal move basing on protocal
                ConnectFour_Socket.send_message(move) # send user move
            elif a%4==3: # receive will be "OKAY" means the next recv will be AI move
                chess=ConnectFour_Socket.recv_message() # receive AI move
                GameLogic.METHOD=chess.split()[0] # receive METHOD
                GameLogic.COLUMN=int(chess.split()[1])-1 # receive COLUMN
                ConnectFour_Console.ResponseACT() # map chesspiece to chess table store in console version game
                ConnectFour_Console.ShowChessTable() # print refreshed chess table
            else:
                ConnectFour_Socket.recv_message() # receive those unnecessary information, even more we can create some check machine for checking these information in case of there are some virus(LOL)
                if ConnectFour_Console.ShowWinner()==None:
                    break
        except: # when unexpectable error emerge, end whole connection
            ConnectFour_Socket.end_connect()
            print('Lose Connection, Please run program again')

if __name__ == '__main__':
    ConnectFour_Online()
