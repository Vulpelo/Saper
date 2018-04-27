from tkinter import *


class MButton:
    def __init__(self, win, i, j, commandLMBFun, commandRMBFun, posX, posY):
        self.window = win
        self.posX = posX
        self.posY = posY
        self.questionMark_image = PhotoImage(file='images/t_questionMark20px.png')
        self.mine_image = PhotoImage(file='images/t_mine20px.png')
        self.mineRed_image = PhotoImage(file='images/t_mineRed20px.gif')
        self.flag_image = PhotoImage(file='images/t_flag20px.png')
        self.number_images = {0: PhotoImage(file='images/t_tile20px.png'),
                              1: PhotoImage(file='images/t_1_20px.png'), 2: PhotoImage(file='images/t_2_20px.png'),
                              3: PhotoImage(file='images/t_3_20px.png'), 4: PhotoImage(file='images/t_4_20px.png'),
                              5: PhotoImage(file='images/t_5_20px.png'), 6: PhotoImage(file='images/t_6_20px.png'),
                              7: PhotoImage(file='images/t_7_20px.png'), 8: PhotoImage(file='images/t_8_20px.png')}
        self.empty_image = PhotoImage(file='images/t_empty20px.png')

        self.thisButton = Button(self.window, bg='grey85', disabledforeground="black", relief=RAISED, overrelief=GROOVE,
                                 width=20, image=self.empty_image, command=(lambda a=i, b=j: commandLMBFun(a, b)))
        self.thisButton.bind("<Button-3>", lambda event, a=i, b=j: commandRMBFun(a, b))
        self.thisButton.grid(row=posY, column=posX, sticky="news", padx=0, pady=0)

    def uncover(self, number=0):
        self.thisButton.destroy()
        self.thisButton = Label(image=self.number_images[number], bg="grey85", width=22, height=22)
        self.thisButton.grid(row=self.posY, column=self.posX, sticky="news")

    def mark(self, marked="empty"):
        if marked == "minered":
            self.thisButton.destroy()
            self.thisButton = Label(image=self.mineRed_image, width=22, height=22)
        elif marked == "mine":
            self.thisButton.destroy()
            self.thisButton = Label(image=self.mine_image, width=22, height=22)
        elif marked == "highlight":
            self.thisButton.config(bg="grey65")
        elif marked == "flag":
            self.thisButton.config(image=self.flag_image)
        elif marked == "questionmark":
            self.thisButton.config(image=self.questionMark_image)
        elif marked == "empty":
            self.thisButton.config(image=self.empty_image)
        self.thisButton.grid(row=self.posY, column=self.posX, sticky="news")

    def disable(self):
        self.thisButton.config(stat=DISABLED)

    def active(self):
        self.thisButton.config(stat=ACTIVE)

    def destroy(self):
        self.thisButton.destroy()
