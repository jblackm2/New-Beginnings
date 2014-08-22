from tkinter import *
class Application(Frame):
    
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.widgets()
        time = 10
    def widgets():
        Label(self,
              text = time,
              ).grid( row = 1, column = 1)
    def tick():
        
        time -= 1
        if time == 0:
            print("HI")
        else:
            self.after(1000,tick)









def main_loop():
    
    root = Tk()
    root.title("Automated Brewer's Assistant")
    root.geometry("900x450")
    app = Application(root)
    root.mainloop()

main_loop()
