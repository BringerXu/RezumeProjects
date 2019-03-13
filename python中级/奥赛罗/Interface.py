# Zhengyi Xu 68996560

import tkinter
import rule
import math
import time
import winsound

BLACK_COLOR = '#000000'
WHITE_COLOR = '#FFFFFF'

class SetUpGame(object):
    def __init__(self):
        self._set_window = tkinter.Toplevel() # build up jumping out window
        self._set_window.title('GAME SETTING') # set up jumping out window name

        self._font = ("Helvetica",30,"bold") # set basic font
        self._bg  = '#006000' # set background color
        self._button_bg ='#003399'# set button color
# build up tkinter frame
        self.frame = tkinter.Frame(master = self._set_window, bg = self._bg, width = 320, height = 320)
        self.frame.grid(sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)
# submit submitting button 
        self.submit_text = tkinter.StringVar()
        self.submit_text.set('FINISH SETTING')
        self._set = tkinter.Button(
            master = self.frame, textvariable = self.submit_text,  bg = self._button_bg, fg = '#000000', command = self._SETUP_FINISHED,font = self._font)
        self._set.grid(row = 0, column = 0, padx = 10,pady = 10, ipadx = 15, ipady = 15, columnspan = 3, sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
# build up table size Scale(2, row and column)
        self._table_tablesize_message = tkinter.Label(self.frame, text = 'TABLE SIZE: ',  bg = self._bg,font = self._font)
        self._table_tablesize_message.grid(row = 1, column = 0, sticky = tkinter.W)
# row Scale
        self._table_row = tkinter.Scale(
            self.frame,from_ = 4, to = 16, resolution = 2,orient = tkinter.HORIZONTAL, bg = self._button_bg, width = 20,font = self._font,troughcolor = '#FFFFFF')
        self._table_row.grid(row = 1, column = 1,padx = 10, pady = 10,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
# column Scale
        self._table_column = tkinter.Scale(
            self.frame, from_ = 4, to = 16, resolution = 2,orient = tkinter.HORIZONTAL, bg = self._button_bg,width = 20,font = self._font,troughcolor = '#FFFFFF')
        self._table_column.grid(row= 1, column = 2,padx = 10, pady = 10,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
# build up first turn button
        self.BLACK_message = tkinter.Label(self.frame , text = 'FIRST TURN: ',  bg = self._bg,font = self._font)
        self.BLACK_message.grid(row = 2, column = 0,sticky = tkinter.W)
        self.BLACK = tkinter.Button(self.frame, text = 'BLACK', bg = self._button_bg, command = self._BLACK,font = self._font)
        self.BLACK.grid(row = 2, column = 1, padx = 10, pady = 10,ipadx = 20 , ipady = 20,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
        self.WHITE = tkinter.Button(self.frame, text = 'WHITE', bg = self._button_bg, command = self._WHITE,font = self._font)
        self.WHITE.grid(row = 2, column = 2,padx = 10, pady = 10,ipadx = 20 , ipady = 20,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
# build up left top button
        self.BLACK_LT_message = tkinter.Label(self.frame , text = 'LEFT TOP: ',  bg =self._bg,font = self._font)
        self.BLACK_LT_message.grid(row = 3, column = 0,sticky = tkinter.W)
        self.BLACK_LT =tkinter.Button(self.frame, text = 'BLACK', bg = self._button_bg, command = self._LEFTTOP_BLACK,font = self._font)
        self.BLACK_LT.grid(row = 3, column = 1,padx = 10, pady = 10,ipadx = 20 , ipady = 20,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
        self.WHITE_LT = tkinter.Button(self.frame, text = 'WHITE', bg = self._button_bg, command = self._LEFTTOP_WHITE,font = self._font)
        self.WHITE_LT.grid(row = 3, column = 2,padx = 10, pady = 10,ipadx = 20 , ipady = 20,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
# build up rule(determine winner) button
        self.RULE_message = tkinter.Label(self.frame, text = 'WIN RULE: ', bg = self._bg, font = self._font)
        self.RULE_message.grid(row = 4, column =0,sticky = tkinter.W)
        self.RULE_OVER = tkinter.Button(self.frame, text = '>' ,bg = self._button_bg, command = self._OVER_RULE,font = self._font)
        self.RULE_OVER.grid(row = 4, column = 1,padx = 10, pady = 10,ipadx = 20 , ipady = 20,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
        self.RULE_LESS = tkinter.Button(self.frame, text = '<' ,bg = self._button_bg, command = self._LESS_RULE,font = self._font)
        self.RULE_LESS.grid(row = 4, column = 2,padx = 10, pady = 10,ipadx = 20 , ipady = 20,sticky = tkinter.W+tkinter.E+tkinter.N+tkinter.S)
# set up change size
        self._set_window.rowconfigure(0, weight = 1)
        self._set_window.columnconfigure(0, weight = 1)
        self.frame.rowconfigure(0,weight = 1)
        self.frame.columnconfigure(0,weight = 1)
        self.frame.rowconfigure(1, weight = 1)
        self.frame.columnconfigure(1, weight = 1)
        self.frame.rowconfigure(2, weight = 1)
        self.frame.columnconfigure(2, weight = 1)
# set up variables for transmitting them to main game window
        self.SETUP = False
        self.tablerow = 0
        self.tablecolumn = 0
        self._first_turn = 0
        self._left_top = 0
        self._rule = ''
# Change Clicked Button Color
    def _BLACK(self):
        self._first_turn = rule.BLACK
        self.BLACK['bg'] = '#66FFCC'
        self.WHITE['bg'] = self._button_bg

    def _WHITE(self):
        self._first_turn = rule.WHITE
        self.WHITE['bg'] = '#66FFCC' 
        self.BLACK['bg'] = self._button_bg

    def _LEFTTOP_BLACK(self):
        self._left_top = rule.BLACK
        self.BLACK_LT['bg'] = '#66FFCC'
        self.WHITE_LT['bg'] = self._button_bg

    def _LEFTTOP_WHITE(self):
        self._left_top = rule.WHITE
        self.WHITE_LT['bg'] = '#66FFCC'
        self.BLACK_LT['bg'] = self._button_bg

    def _OVER_RULE(self):
        self._rule = '>'
        self.RULE_OVER['bg'] = '#66FFCC'
        self.RULE_LESS['bg'] = self._button_bg

    def _LESS_RULE(self):
        self._rule = '<'
        self.RULE_LESS['bg'] = '#66FFCC'
        self.RULE_OVER['bg'] = self._button_bg
# show this top level window
    def show(self):
        self._set_window.grab_set()
        self._set_window.wait_window()
# get function
    def _SETUP(self):
        return self.SETUP

    def _SETUP_FINISHED(self):
        if self._first_turn!=rule.NONE and self._left_top!=rule.NONE and self._rule != '':
            self.SETUP = True
            self.tablerow = self._table_row.get()
            self.tablecolumn = self._table_column.get()
            self._set_window.destroy()
        else:
            self.submit_text.set('YOU DO NOT FINISH SOME SETTINGS YET')

    def get_tablerow(self):
        return self.tablerow

    def get_tablecolumn(self):
        return self.tablecolumn

    def get_first_turn(self):
        return self._first_turn

    def get_left_top(self):
        return self._left_top

    def get_rule(self):
        return self._rule




class MainGame:
    def __init__(self):
        
        self.window = tkinter.Tk()
        self.window.title("Othella")


        self._font = ("Helvetica",12,"bold")

        self.frame = tkinter.Frame(master = self.window, bg = '#006000')
        self.frame.grid(row = 0, column = 0, sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)

        self.hint_frame = tkinter.Frame(master = self.window, bg = '#006000')
        self.hint_frame.grid(row = 1, column = 0, sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W, columnspan = 2)

        self.result_frame = tkinter.Frame(master = self.window, bg ='#006000')
        self.result_frame.grid(row = 0, column = 1, sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)
# BLACK number
        self.BLACK_num = tkinter.IntVar()
        self.BLACK_num.set(0)
        self.BLACK_label_prefix =tkinter.Label(master = self.result_frame, bg='#006000', text = 'BLACK: ', font = self._font)
        self.BLACK_label_prefix.grid(row = 0, column = 0,sticky = tkinter.W)
        self.BLACK_label = tkinter.Label(master = self.result_frame, bg='#006000', textvariable = self.BLACK_num, font = self._font)
        self.BLACK_label.grid(row = 0, column = 1,sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)
# WHITE number
        self.WHITE_num = tkinter.IntVar()
        self.WHITE_num.set(0)
        self.WHITE_label_prefix =tkinter.Label(master = self.result_frame, bg='#006000', text = 'WHITE: ', font = self._font)
        self.WHITE_label_prefix.grid(row = 1, column = 0,sticky = tkinter.W)
        self.WHITE_label = tkinter.Label(master = self.result_frame, bg='#006000', textvariable = self.WHITE_num, font = self._font)
        self.WHITE_label.grid(row = 1, column = 1,sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)
# 
        self._turn = tkinter.StringVar()
        self._turn.set('')
        self._turn_message_prefix = tkinter.Label(master = self.result_frame, bg='#006000', text = 'TURN: ', font = self._font)
        self._turn_message_prefix.grid(row = 2, column = 0,sticky = tkinter.W)
        self._turn_message = tkinter.Label(master = self.result_frame, bg='#006000', textvariable = self._turn, font = self._font)
        self._turn_message.grid(row = 2, column = 1,sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)

        self._winner = tkinter.StringVar()
        self._winner.set('')
        self._winner_message_prefix = tkinter.Label(master = self.result_frame, bg='#006000', text = 'WINNER: ', font = self._font)
        self._winner_message_prefix.grid(row = 3, column = 0,sticky = tkinter.W)
        self._winner_message = tkinter.Label(master = self.result_frame, bg='#006000', textvariable = self._winner, font = self._font)
        self._winner_message.grid(row = 3, column = 1, sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)

        self._BLACK_spend_time = tkinter.IntVar()
        self._BLACK_spend_time.set(0)
        self._BLACK_spend_time_message_prefix = tkinter.Label(master = self.result_frame, bg='#006000', text = 'BLACK SPEND: ', font = self._font)
        self._BLACK_spend_time_message_prefix.grid(row = 4, column = 0,sticky = tkinter.W)
        self._BLACK_spend_time_message = tkinter.Label(master = self.result_frame, bg='#006000', textvariable = self._BLACK_spend_time, font = self._font)
        self._BLACK_spend_time_message.grid(row = 4, column = 1, sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)

        self._WHITE_spend_time = tkinter.IntVar()
        self._WHITE_spend_time.set(0)
        self._WHITE_spend_time_message_prefix = tkinter.Label(master = self.result_frame, bg='#006000', text = 'WHITE SPEND: ', font = self._font)
        self._WHITE_spend_time_message_prefix.grid(row = 5, column = 0,sticky = tkinter.W)
        self._WHITE_spend_time_message = tkinter.Label(master = self.result_frame, bg='#006000', textvariable = self._WHITE_spend_time, font = self._font)
        self._WHITE_spend_time_message.grid(row = 5, column = 1, sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)  

        self._currenttime = tkinter.StringVar()
        self._currenttime.set('')
        self._currenttime_message_prefix = tkinter.Label(master = self.result_frame, bg='#006000', text = 'CLOCK: ', font = self._font)
        self._currenttime_message_prefix.grid(row = 6, column = 0,sticky = tkinter.W)
        self._currenttime_message = tkinter.Label(master = self.result_frame, bg='#006000', textvariable = self._currenttime, font = self._font)
        self._currenttime_message.grid(row = 6, column = 1,sticky = tkinter.N + tkinter.S +tkinter.E + tkinter.W)

        self.hint = tkinter.StringVar()
        self.hint.set('DIRECTION: CLICK SET BEFORE START')

        self.hint_message = tkinter.Label(
            master = self.hint_frame, textvariable = self.hint, bg = '#006000', fg = '#FFFFFF')
        self.hint_message.grid(row = 0, column = 0, sticky = tkinter.W)

        self.Menu = tkinter.Menu(master = self.window)
        self.Menu.add_command(label = 'START', command = self.draw_gametable)
        self.Menu.add_command(label = 'SET', command = self.open_dialog)
        self.Menu.add_command(label = 'QUIT', command = self.quit)
        self.window['menu'] = self.Menu

        self._set = False
        self.tablerow = 0
        self.tablecolumn = 0
        self.turn = rule.NONE
        self.lefttop = rule.NONE
        self.table = None
        self.rule = ''
        self._start = False

        self.canvas = tkinter.Canvas(
            master = self.frame, bg = '#006000')

        self.canvas.grid(
            row = 0, column = 0, sticky =  tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.V_line = 50
        self.H_line = 50

        self.GET_time()
        self.GET_spend_time()

        self.window.rowconfigure(0, weight = 1)
        self.window.columnconfigure(0, weight = 1)
        self.hint_frame.rowconfigure(0, weight = 1)
        self.hint_frame.columnconfigure(0, weight = 1)

        self.frame.rowconfigure(0,weight = 1)
        self.frame.columnconfigure(0,weight = 1)
        for item in range(7):
            self.result_frame.rowconfigure(item, weight = 1)
            self.result_frame.columnconfigure(item, weight = 1)

    def quit(self):
        self.window.destroy()

    def start(self):
        self.window.mainloop()

    def open_dialog(self):
        dialog = SetUpGame()
        dialog.show()

        self._set = dialog._SETUP()

        # After the dialog box is dismissed, we'll check if it was the OK
        # or the Cancel button that got clicked.  If OK was clicked, we'll
        # change the greeting label's text by setting its control variable.
        if dialog._SETUP():
            self.tablerow = dialog.get_tablerow()
            self.tablecolumn = dialog.get_tablecolumn()
            self.turn = dialog.get_first_turn()
            self.lefttop = dialog.get_left_top()
            self.rule = dialog.get_rule()
            self.hint.set('DIRECTION: CLICK START AND ENJOY GAME')

    def GET_time(self):
        self._currenttime.set(time.strftime("%H:%M:%S"))
        self.window.after(1000, self.GET_time)

    def GET_spend_time(self):
        if self._start == True:
            if self.turn == rule.BLACK:
                self._BLACK_spend_time.set(self._BLACK_spend_time.get()+1)
                
            elif self.turn == rule.WHITE:
                self._WHITE_spend_time.set(self._WHITE_spend_time.get()+1)
            else:
                pass
        self.window.after(1000, self.GET_spend_time)

    def _redraw(self,event:tkinter.Event):
        self.canvas.delete(tkinter.ALL)
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.V_line = self.canvas.winfo_width()/self.tablecolumn
        self.H_line = self.canvas.winfo_height()/self.tablerow
        self._Map()
        self.Valid_Map()

    def draw_gametable(self):
        if self._set:
            self.canvas.delete(tkinter.ALL)
            self.hint.set('DIRECTION: ENJOY GAME')
            self.BLACK_num.set(2)
            self.WHITE_num.set(2)
            self.table = rule.Table(self.tablerow, self.tablecolumn, self.lefttop).Build()

            self.canvas['width'] = self.V_line * self.tablecolumn
            self.canvas['height'] = self.H_line * self.tablerow

            self.width = self.canvas.winfo_width()
            self.height = self.canvas.winfo_height()

            self.V_line = self.canvas.winfo_width()/self.tablecolumn
            self.H_line = self.canvas.winfo_height()/self.tablerow

            for time in range(self.tablecolumn-1):
                self.canvas.create_line(self.V_line*(time+1),0,self.V_line*(time+1),self.height)
            for time in range(self.tablerow-1):
                self.canvas.create_line(0,self.H_line*(time+1),self.width,self.H_line*(time+1))
            self._Map()
            self.Valid_Map()
            self.Show_Turn()
            self._BLACK_spend_time.set(0)
            self._WHITE_spend_time.set(0)

            self.canvas.bind('<Button-1>',self._drop)
            self.canvas.bind('<Configure>',self._redraw)
            
            self._start = True

        else:
            self.hint.set('DIRECTION: PLEASE CLICK SET BUTTON FOR SETTING GAME')

    def Show_Turn(self):
        if self.turn == rule.BLACK:
            self._turn.set('BLACK')
        elif self.turn == rule.WHITE:
            self._turn.set('WHITE')

    def Show_Chess_NUM(self):
        NUM = rule.SumNum(self.table)
        self.BLACK_num.set(NUM[0])
        self.WHITE_num.set(NUM[1])

    def _Map(self):
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.V_line = self.width/self.tablecolumn
        self.H_line = self.height/self.tablerow
        for time in range(self.tablecolumn-1):
            self.canvas.create_line(self.V_line*(time+1),0,self.V_line*(time+1),self.height)
        for time in range(self.tablerow-1):
            self.canvas.create_line(0,self.H_line*(time+1),self.width,self.H_line*(time+1))


        for row in range(len(self.table)):
            for col in range(len(self.table[0])):
                if self.table[row][col]==rule.NONE:
                    pass
                elif self.table[row][col]==rule.WHITE:
                    self.canvas.create_oval(col*self.V_line,row*self.H_line,col*self.V_line+self.V_line,row*self.H_line+self.H_line,fill = '#FFFFFF',width = 0)
                elif self.table[row][col]==rule.BLACK:
                    self.canvas.create_oval(col*self.V_line,row*self.H_line,col*self.V_line+self.V_line,row*self.H_line+self.H_line,fill = '#000000',width = 0)
        self.Show_Chess_NUM()
        self.Show_Turn()
        self.CheckWIN()


    def Valid_Map(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        V_line = width/self.tablecolumn
        H_line = height/self.tablerow
        MOVES = rule.Check(self.table, self.turn).PureValidMove
        for move in MOVES:
            col = move[1]
            row = move[0]
            self.canvas.create_oval(col*V_line,row*H_line,col*V_line+V_line,row*H_line+H_line, state = tkinter.NORMAL, activefill ='#99FF99', outline = '#006000',tag = 'pre', width = 0)

    def CheckWIN(self):
        if rule.Check(self.table, self.turn).PureValidMove==[]:
            if rule.Check(self.table, rule.BLACK).PureValidMove==[] and rule.Check(self.table, rule.WHITE).PureValidMove==[]:
                self._winner.set(rule.CheckWin(self.rule, self.table))
                self._start = False
            elif rule.Check(self.table, rule.BLACK).Full():
                self._winner.set(rule.CheckWin(self.rule, self.table))
                self._start = False
            else:
                self.turn = rule.ChangeTurn(self.turn)
                self.Show_Chess_NUM()
                self.Show_Turn()
                self.Valid_Map()
        else:
            self.Valid_Map()

    def _drop(self,event:tkinter.Event):
        MOVES = rule.Check(self.table, self.turn).PureValidMove
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.V_line = self.width/self.tablecolumn
        self.H_line = self.height/self.tablerow
        row = math.floor(event.y/self.H_line)
        col = math.floor(event.x/self.V_line)
        if (row, col) in MOVES:
            self.hint.set('DIRECTION: VALID MOVE')
            winsound.Beep(300,100)
            rule.Check(self.table, self.turn).Map(row,col)
            self._Map()
            self.turn = rule.ChangeTurn(self.turn)
            self.canvas.delete('pre')
            self._Map()
        else:
            self.hint.set('DIRECTION: INVALID MOVE')
            self.Wrong_Effect_Sound()
    
    def Wrong_Effect_Sound(self):
        try:
            winsound.PlaySound('wrong_effect_sound.wav', winsound.SND_ALIAS)
        except:
            pass

if __name__ == '__main__':
    Othella = MainGame().start()