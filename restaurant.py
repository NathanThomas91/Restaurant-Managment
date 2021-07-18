from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

obj = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'fellowes', database = 'restaurant')
cur = obj.cursor()
        
starting_window = Tk()
width = starting_window.winfo_screenwidth()
height = starting_window.winfo_screenheight()
starting_window.geometry('%dx%d' %(width, height))
img = ImageTk.PhotoImage(Image.open("restaurant_bg.jpg"))
imglabel = Label(starting_window, image=img, width = 1600, height =900)
imglabel.image = img
imglabel.place(x=0, y = 0)
starting_window.title('Restaurant Managment')
l1 = Label(starting_window, text = 'Welcome to XYZ restaurant', font = ('Times',25,'bold')).place(x = 500, y = 30)

class restaurant:
    def __init__(self):
        a = Tk()
        width = a.winfo_screenwidth()
        height = a.winfo_screenheight()
        a.geometry('%dx%d' %(width, height))
        img = ImageTk.PhotoImage(Image.open("main_sc.jpg"))
        imglabel = Label(a, image=img, width = 1360, height = 680)
        imglabel.image = img
        imglabel.place(x=0, y = 0)
        a.title('Restaurant')
        l1 = Label(a, text = 'XYZ restaurant', font = ('Times',30,'bold')).place(x = 500, y = 80)

        MenuBar1 = Menu(a)
        SubMenu1 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Book Order', menu = SubMenu1)
        SubMenu1.add_command(label = 'Book now', command = self.book_now)

        SubMenu2 = Menu(MenuBar1, tearoff = 0)
        MenuBar1.add_cascade(label = 'Menu', menu = SubMenu2)
        SubMenu2.add_command(label = 'Show Menu', command = self.show_menu)

        a.config(menu = MenuBar1)
        global menu_item, menu_prize
        menu_item = {'1':'Burger','2':'Pizza','3':'Fried Chicken'}
        menu_prize = {'1':'100','2':'350','3':'250'}

    def book_now(self):
        global Window
        Window = Tk()
        Window.geometry("600x600")
        l1 = Label(Window, text = 'Book now -', font = ('Times',20,'bold')).place(x = 10, y = 15)

        l2 = Label(Window, text = 'Table Number -', font = ('',15,'')).place(x = 10, y = 90)
        l3 = Label(Window, text = 'Item -', font = ('',15,'')).place(x = 10, y = 130)
        l4 = Label(Window, text = 'Quantity -', font = ('',15,'')).place(x = 10, y = 170)
        l5 = Label(Window, text = 'Do u have a corporate or government ID card -', font = ('',15,'')).place(x = 10, y = 210)

        global quantity
        t_no = Entry(Window)
        quantity = Entry(Window)
        t_no.place(x = 170, y = 95)
        quantity.place(x = 120, y = 175)

        def get_value(event):
            global item1, g_id1
            item1 =  i.get()
            g_id1 = id1.get()
            
        item = StringVar()
        i = ttk.Combobox(Window, width = 20, textvariable =  item)
        i['value'] =  ('---none---', menu_item['1'], menu_item['2'], menu_item['3'])
        i.place(x = 90, y = 135)
        i.current(0)
        i.bind("<<ComboboxSelected>>",get_value)

        g_id = StringVar()
        id1 = ttk.Combobox(Window, width = 20, textvariable =  g_id)
        id1['value'] =  ('---none---', 'No' ,'Yes')
        id1.place(x = 450, y = 215)
        id1.current(0)
        id1.bind("<<ComboboxSelected>>",get_value)

        global b1
        b1 = Button(Window, text = 'Submit', font = ('',13,''), command = self.submit).place(x = 200, y = 300)
        b2 = Button(Window, text = 'Generate Bill', font = ('',13,''), command = self.calculate_bill).place(x = 300, y = 300)

    def submit(self):
        messagebox.showinfo("Submit", "Order Placed " + str(item1))
        
    def calculate_bill(self):
        q = quantity.get()
        if item1 == menu_item['1']:
            xyz = menu_prize['1']
        elif item1 == menu_item['2']:
            xyz = menu_prize['2']
        elif item1 == menu_item['3']:
            xyz = menu_prize['3']

        amnt_no_tax = int(q) * int(xyz)
        adding_tax1 = amnt_no_tax + 2.5
        adding_tax2 = adding_tax1 + 2.5
        tax_added = adding_tax2
        if g_id1 == 'Yes':
            final_amnt = tax_added - 4
        else:
            final_amnt = tax_added

        messagebox.showinfo("Bill", 'Your final amount is ' + str(final_amnt))
        self.close()
        self.feedback_form()

    def close(self):
        Window.destroy()

    def feedback_form(self):
        global Window
        Window = Tk()
        Window.geometry("600x600")
        l1 = Label(Window, text = 'Feed Back Form', font = ('Times',20,'bold')).place(x = 200, y = 25)

        l2 = Label(Window, text = 'Enter Name -', font = ('',15,'')).place(x = 30, y = 100)
        l3 = Label(Window, text = 'Enter Email ID -', font = ('',15,'')).place(x = 30, y = 140)
        l4 = Label(Window, text = 'Enter Date Of Birth -', font = ('',15,'')).place(x = 30, y = 180)
        
        l5 = Label(Window, text = 'Feed Back', font = ('times',18,'bold')).place(x = 230, y = 230)
        l6 = Label(Window, text = 'Service -', font = ('',15,'')).place(x = 30, y = 280)
        l7 = Label(Window, text = 'Food -', font = ('',15,'')).place(x = 30, y = 320)

        global en, eid, edob
        en = Entry(Window)
        eid = Entry(Window)
        edob = Entry(Window)

        en.place(x = 170, y = 105)
        eid.place(x = 190, y = 145)
        edob.place(x = 230, y = 185)

        def get_value(event):
            global f_service, f_food
            f_service =  s.get()
            f_food = f.get()
            
        service = StringVar()
        s = ttk.Combobox(Window, width = 20, textvariable =  service)
        s['value'] =  ('---none---', '1','2','3','4','5')
        s.place(x = 130, y = 285)
        s.current(0)
        s.bind("<<ComboboxSelected>>",get_value)

        food = StringVar()
        f = ttk.Combobox(Window, width = 20, textvariable =  food)
        f['value'] =  ('---none---', '1','2','3','4','5')
        f.place(x = 110, y = 325)
        f.current(0)
        f.bind("<<ComboboxSelected>>",get_value)

        b1 = Button(Window, text = 'Submit', font = ('',13,''), command = self.save_feedback).place(x = 270, y = 380)

    def save_feedback(self):
        name = en.get()
        email = eid.get()
        dob = edob.get()
        
        sql = "Insert into feedback values (%s,%s,%s,%s,%s)"
        rec = (name, email, dob, f_service, f_food)
        try:    #exception error
            cur.execute(sql, rec)
            obj.commit()
            messagebox.showinfo("Feedback", "Feedback Saved!")
        except:
            obj.rollback()
            messagebox.showinfo("Feedback", "Feedback not Saved!!")

        obj.close
        self.close
        
    def show_menu(self):
        global Window
        Window = Tk()
        Window.geometry("500x500")

        l1 = Label(Window, text = 'Menu - ', font = ('Times',20,'bold')).place(x = 10, y = 15)
        l2 = Label(Window, text = 'Item', font = ('Times',17,'bold')).place(x = 100, y = 90)
        l3 = Label(Window, text = 'Prize', font = ('Times',17,'bold')).place(x = 300, y = 90)
        
        menu1 = Label(Window, text = menu_item['1'], font = ('',15,'')).place(x = 100, y = 130)
        menu2 = Label(Window, text = menu_item['2'], font = ('',15,'')).place(x = 100, y = 170)
        menu3 = Label(Window, text = menu_item['3'], font = ('',15,'')).place(x = 100, y = 210)

        prize1 = Label(Window, text = menu_prize['1'], font = ('',15,'')).place(x = 300, y = 130)
        prize2 = Label(Window, text = menu_prize['2'], font = ('',15,'')).place(x = 300, y = 170)
        prize3 = Label(Window, text = menu_prize['3'], font = ('',15,'')).place(x = 300, y = 210)

        b1 = Button(Window, text = 'Close', font = ('',13,''), command = self.close).place(x = 200, y = 300)

def start():
    starting_window.destroy()
    r = restaurant()

starting_window.after(2000,start)
        
