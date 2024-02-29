import tkinter as tk
import tkinter.font as tkFont
def lui1():
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
    GLabel_466["text"] = "ไม่มีคนเอามึงหรอก"
    GLabel_466.place(x=0,y=0,width=600,height=500)
def lui2():
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
    GLabel_466["text"] = "มีคนเอาด้วยหรอ"
    GLabel_466.place(x=0,y=0,width=600,height=500)

root = tk.Tk()
root.geometry("400x400")
root.title('valentine')
tk.Button(root,text='โสด', bg = "pink", command = lui1).pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
tk.Button(root,text='ไม่โสด', bg = "purple", command = lui2).pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)

root.mainloop()