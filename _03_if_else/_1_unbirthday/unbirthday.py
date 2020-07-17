'''
Created on Jul 17, 2020

@author: root
'''
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    birthday = simpledialog.askstring(title = 'Greeter', prompt="What is your birthday MM/DD")
    if(birthday == "07/17"):
        messagebox.showinfo(title= 'story', message = "Happy Birthday!!!")
    else:
        messagebox.showinfo(title= 'story', message = "Happy Unbirthday;(")
pass
window.mainloop()