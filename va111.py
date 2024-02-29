import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_466=tk.Label(root)
        ft = tkFont.Font(family='Times',size=54)
        GLabel_466["font"] = ft
        GLabel_466["fg"] = "#333333"
        GLabel_466["justify"] = "center"
        GLabel_466["text"] = "อยู่คนเดียวไปซะไม่มีคนเอามึงหรอก"
        GLabel_466.place(x=0,y=0,width=596,height=495)
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
