from textblob import TextBlob
import tkinter as tk
import tkinter.font as tkFont

def Check_Spell():
    userdata = GLineEdit_522.get()
    corrected= TextBlob(userdata).correct()
    GLineEdit_499.delete(0,tk.END)
    GLineEdit_499.insert(0,corrected)


class App:
    def __init__(self, root):
        #setting title
        root.title("Spelling Check")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.config(bg="darkorchid2")

        global GLineEdit_499,GLineEdit_522

        GLabel_572=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=13,weight="bold")
        GLabel_572["font"] = ft
        GLabel_572["bg"] = "darkorchid2"
        GLabel_572["fg"] = "#FFFAFA"
        GLabel_572["justify"] = "center"
        GLabel_572["text"] = "Enter the word to be check :"
        GLabel_572.place(x=10,y=90,width=225,height=42)

        GLineEdit_522=tk.Entry(root)
        GLineEdit_522["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=13)
        GLineEdit_522["font"] = ft
        GLineEdit_522["bg"] = "darkorchid1"
        GLineEdit_522["fg"] = "#FFFAFA"
        GLineEdit_522["justify"] = "center"
        GLineEdit_522["text"] = ""
        GLineEdit_522.place(x=230,y=90,width=352,height=41)

        GLabel_947=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=13,weight="bold")
        GLabel_947["font"] = ft
        GLabel_947["fg"] = "#FFFAFA"
        GLabel_947["bg"] = "darkorchid2"
        GLabel_947["justify"] = "center"
        GLabel_947["text"] = "Corrected Word :"
        GLabel_947.place(x=0,y=330,width=194,height=38)

        GLineEdit_499=tk.Entry(root)
        GLineEdit_499["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        GLineEdit_499["font"] = ft
        GLineEdit_499["bg"] = "darkorchid1"
        GLineEdit_499["fg"] = "#FFFAFA"
        GLineEdit_499["justify"] = "center"
        GLineEdit_499["text"] = ""
        GLineEdit_499.place(x=200,y=330,width=381,height=41)

        GButton_988=tk.Button(root)
        ft = tkFont.Font(family='Helvetica',size=10,weight="bold")
        GButton_988["bg"] = "darkorchid2"
        GButton_988["font"] = ft
        GButton_988["fg"] = "#FFFAFA"
        GButton_988["activebackground"]="darkorchid1"
        GButton_988["justify"] = "center"
        GButton_988["borderwidth"] = "1px"
        GButton_988["text"] = "Check"
        GButton_988.place(x=330,y=160,width=249,height=39)
        GButton_988["command"] = Check_Spell

    def GButton_988_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
