from tkinter import *
import random
import mysql.connector as m1
from tkinter import messagebox  
try:
    con = m1.connect(
        host='localhost',
        database='shop',
        user='root',
        password='aanya123'
    )
    if con.is_connected():
        print("Mubarak ho! Database se connection ho gaya hai.")
        cursor = con.cursor()
except Exception as e:
    print("Database connection mein error hai:", e)
#def billshop():
def genRno():
            a=random.randint(1,9)
            b=random.randint(1,9)
            c=random.randint(1,9)
            d=random.randint(1,9)
            n="hdfc"+str(a)+str(b)+str(c)+str(d)
            return n

def val(x):
    try:
        return int(x.get())
    except:
        return 0

def bill():
    items = []
    if a.get().strip() == "" or b.get().strip() == "":
        messagebox.showerror("Error", "Enter customer details")
        return
    try:

        # COSMETICS
        total_cos_price = (val(s)*1000) + (val(f)*200) + (val(cl)*800) + (val(co)*1200) + (val(hg)*500) + (val(e)*100)
        tot1.set(total_cos_price)
        cos_tax = round(total_cos_price * 0.18, 2)
        taxe.set(cos_tax)

        # GROCERY
        total_groc_price = (val(r)*2000) + (val(w)*1000) + (val(p)*200) + (val(pu)*300) + (val(sa)*100) + (val(sug)*100)
        tot2.set(total_groc_price)
        groc_tax = round(total_groc_price * 0.05, 2)
        zaxe.set(groc_tax)

        # CLOTHES
        total_clot_price = (val(j)*5000) + (val(t)*3000) + (val(ja)*10000) + (val(sh)*2000) + (val(to)*3000) + (val(sar)*10000)
        tot3.set(total_clot_price)
        clot_tax = round(total_clot_price * 0.12, 2)
        axe.set(clot_tax)

        # FINAL
        total = total_cos_price + total_groc_price + total_clot_price
        tax = cos_tax + groc_tax + clot_tax
        final = total + tax

        

        # Cosmetics
        

# Cosmetics
        if val(s) > 0:
                items.append(("Serum", val(s), 1000, val(s)*1000))
        if val(cl) > 0:
                items.append(("Cleanser", val(cl), 800, val(cl)*800))
        if val(f) > 0:
                items.append(("Facemask", val(f), 200, val(f)*200))
        if val(co) > 0:
                items.append(("Compact", val(co), 1200, val(co)*1200))
        if val(hg) > 0:
                items.append(("Hair Gel", val(hg), 500, val(hg)*500))
        if val(e) > 0:
                items.append(("Eyeliner", val(e), 100, val(e)*100))

        # Grocery
        if val(r) > 0:
                items.append(("Rice", val(r), 2000, val(r)*2000))
        if val(w) > 0:
                items.append(("Wheat", val(w), 1000, val(w)*1000))
        if val(p) > 0:
                items.append(("Poha", val(p), 200, val(p)*200))
        if val(pu) > 0:
                items.append(("Pulses", val(pu), 300, val(pu)*300))
        if val(sa) > 0:
                items.append(("Salt", val(sa), 100, val(sa)*100))
        if val(sug) > 0:
                items.append(("Sugar", val(sug), 100, val(sug)*100))

        # Clothes
        if j.get() != "" and int(j.get()) > 0:
                items.append(("Jeans", int(j.get()), 5000, int(j.get())*5000))
        if t.get() != "" and int(t.get()) > 0:
                items.append(("Trouser", int(t.get()), 3000, int(t.get())*3000))
        if ja.get() != "" and int(ja.get()) > 0:
                items.append(("Jacket", int(ja.get()), 10000, int(ja.get())*10000))
        if sh.get() != "" and int(sh.get()) > 0:
                items.append(("Shirt", int(sh.get()), 2000, int(sh.get())*2000))
        if to.get() != "" and int(to.get()) > 0:
                items.append(("Top", int(to.get()), 3000, int(to.get())*3000))
        if sar.get() != "" and int(sar.get()) > 0:
                items.append(("Saree", int(sar.get()), 10000, int(sar.get())*10000))
        e1.delete(0, END)
        e1.insert(0, final)

        g1.delete(0, END)
        g1.insert(0, tax)

        # CUSTOMER
        cust_name = a.get()
        cust_phone = b.get()
        bill_no = str(random.randint(1000,9999))
        c.set(bill_no)

        # DB
        qry = "INSERT INTO account (bill_no, name, phone) VALUES (%s,%s,%s)"
        cursor.execute(qry, (bill_no, cust_name, cust_phone))
        con.commit()

        # BILL AREA
        # BILL AREA
        for widget in f6.winfo_children():
                widget.destroy()

        Label(f6, text=f"Bill No: {bill_no}", font=("Arial", 12, "bold"), bg="snow").pack()
        Label(f6, text=f"Customer: {cust_name}", bg="snow").pack()
        Label(f6, text="-----------------------------------", bg="snow").pack()

        # Header
        Label(f6, text="Item   Qty   Price   Total", font=("Arial", 10, "bold"), bg="snow").pack()

        # Items print
        for item in items:
                name, qty, price, total_item = item
                Label(f6, text=f"{name}   {qty}   {price}   {total_item}", bg="snow").pack()

                Label(f6, text="-----------------------------------", bg="snow").pack()
                Label(f6, text=f"Total: Rs {total}", bg="snow").pack()
                Label(f6, text=f"Tax: Rs {tax}", bg="snow").pack()
                Label(f6, text=f"Pay: Rs {final}", fg="red", font=("Arial", 12, "bold"), bg="snow").pack()
                        
        messagebox.showinfo("Success", "Bill Generated")

    except Exception as err:
        print("Error:", err)
        print(items)




win=Tk()
win.title("retail bill")
# win.maxsize(1500,1500)
# win.minsize(1500,1500)
win.geometry("1920x1080")


a=StringVar()#name
b=StringVar()   # phone
c=StringVar()   # bill no
s = StringVar()
f = StringVar()
cl = StringVar()
co = StringVar()
hg = StringVar()
e = StringVar()

r = StringVar()
w = StringVar()
p = StringVar()
pu = StringVar()
sa = StringVar()
sug = StringVar()

j = StringVar()

t = StringVar()
ja = StringVar()
sh = StringVar()
to = StringVar()
sar = StringVar()

taxe=DoubleVar()
zaxe=DoubleVar()
axe=DoubleVar()

tot1=IntVar()
tot2=IntVar()
tot3=IntVar()


f1=Frame(win,height=100,width=1920,bg="snow",border=6,relief="groove")
f1.pack()

btn=Label(f1,text="Retail   Billing   System",font=("impact",30),fg="purple4",height=2,bg="snow")
btn.pack()

f2=LabelFrame(win,text="coustmer details",font=("arial",15),fg="purple4",height=100,width=1920,bg="snow",border=8,relief="groove")
f2.place(x=10, y=80, width=1890, height=100)

name_lbl = Label(f2, text="Name", font=("Arial",20,"bold"), bg="snow", fg="purple4")
name_lbl.grid(row=0, column=0, padx=2, pady=10,sticky="w")

ent1=Entry(win,bg="snow",font=("book antiqua",15),border=2,textvariable=a)
ent1.place(x=150,y=118)

name_lbl2 = Label(f2, text="Phone number", font=("Arial",20,"bold"), bg="snow", fg="purple4")
name_lbl2.grid(row=0, column=0, padx=400, pady=10,sticky="w")

ent2=Entry(win,bg="snow",font=("book antiqua",15),border=2,textvariable=b)
ent2.place(x=680,y=118)

name_lbl3 = Label(f2, text="Bill number", font=("Arial",20,"bold"), bg="snow", fg="purple4")
name_lbl3.grid(row=0, column=0, padx=950, pady=10,sticky="w")

ent3=Entry(win,bg="snow",font=("book antiqua",15),border=2,textvariable=c)
ent3.place(x=1150,y=118)

btn1=Button(f2,text="Search",font=("Arial",20,"bold"), bg="purple2", fg="snow")
btn1.place(x=1600,y=118)

f3=LabelFrame(win,text="Cosmetics",font=("Arial",20,"bold"), bg="snow", fg="purple4",height=400,width=300,border=8,relief="groove")
f3.place(x=10, y=180, width=350, height=400)

serum = Label(f3, text="Serum", font=("candara",20,"bold"), bg="snow", fg="purple1")
serum.grid(row=0, column=0, padx=1, pady=8,sticky="w")
s1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=s)
s1.place(x=130,y=230,width=150)

cleanser = Label(f3, text="Cleanser", font=("candara",20,"bold"), bg="snow", fg="purple1")
cleanser.grid(row=1, column=0, padx=1, pady=18,sticky="w")
s2=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=cl)
s2.place(x=130,y=290,width=150)

mask = Label(f3, text="Facemask", font=("candara",20,"bold"), bg="snow", fg="purple1")
mask.grid(row=2, column=0, padx=1, pady=10,sticky="w")
s3=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=f)
s3.place(x=132,y=350,width=150)

Foundation = Label(f3, text="Compact", font=("candara",20,"bold"), bg="snow", fg="purple1")
Foundation.grid(row=3, column=0, padx=1, pady=10,sticky="w")
s4=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=co)
s4.place(x=132,y=410,width=150)


hairgel = Label(f3, text="Hair gel", font=("candara",20,"bold"), bg="snow", fg="purple1")
hairgel.grid(row=4, column=0, padx=1, pady=10,sticky="w")
s5=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=hg)
s5.place(x=132,y=470,width=150)


Foun = Label(f3, text="Eyeliner", font=("candara",20,"bold"), bg="snow", fg="purple1")
Foun.grid(row=5, column=0, padx=1, pady=10,sticky="w")
s6=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=e)
s6.place(x=132,y=530,width=150)


f4=LabelFrame(win,text="Grocery",font=("Arial",20,"bold"), bg="snow", fg="purple4",height=400,width=300,border=8,relief="groove")
f4.place(x=360, y=180, width=350, height=400)


F1 = Label(f4, text="Rice", font=("candara",20,"bold"), bg="snow", fg="purple1")
F1.grid(row=0, column=0, padx=1, pady=10,sticky="w")
w1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=r)
w1.place(x=460,y=230,width=150)

F2 = Label(f4, text="Wheat", font=("candara",20,"bold"), bg="snow", fg="purple1")
F2.grid(row=1, column=0, padx=1, pady=18,sticky="w")
w2=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=w)
w2.place(x=460,y=290,width=150)

m= Label(f4, text="Poha", font=("candara",20,"bold"), bg="snow", fg="purple1")
m.grid(row=2, column=0, padx=1, pady=10,sticky="w")
w3=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=p)
w3.place(x=460,y=350,width=150)


p1 = Label(f4, text="Pulses", font=("candara",20,"bold"), bg="snow", fg="purple1")
p1.grid(row=3, column=0, padx=1, pady=10,sticky="w")
w4=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=pu)
w4.place(x=460,y=410,width=150)


salt_lbl = Label(f4, text="Salt", font=("candara",20,"bold"), bg="snow", fg="purple1")
salt_lbl.grid(row=4, column=0, padx=1, pady=10,sticky="w")
w5=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=sa)
w5.place(x=460,y=470,width=150)


Fou = Label(f4, text="Sugar", font=("candara",20,"bold"), bg="snow", fg="purple1")
Fou.grid(row=5, column=0, padx=1, pady=10,sticky="w")
w6=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=sug)
w6.place(x=460,y=530,width=150)

f5=LabelFrame(win,text="Clothes",font=("Arial",20,"bold"), bg="snow", fg="purple4",height=400,width=300,border=8,relief="groove")
f5.place(x=710, y=180, width=350, height=400)

F9 = Label(f5, text="Jeans", font=("candara",20,"bold"), bg="snow", fg="purple1")
F9.grid(row=0, column=0, padx=1, pady=10,sticky="w")
z1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=j)
z1.place(x=820,y=230,width=150)

F8 = Label(f5, text="Trousers", font=("candara",20,"bold"), bg="snow", fg="purple1")
F8.grid(row=1, column=0, padx=1, pady=18,sticky="w")
z2=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=t)
z2.place(x=820,y=290,width=150)

m1= Label(f5, text="Jacket", font=("candara",20,"bold"), bg="snow", fg="purple1")
m1.grid(row=2, column=0, padx=1, pady=10,sticky="w")
z3=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=ja)
z3.place(x=820,y=350,width=150)


p9 = Label(f5, text="Shirt", font=("candara",20,"bold"), bg="snow", fg="purple1")
p9.grid(row=3, column=0, padx=1, pady=10,sticky="w")
z4=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=sh)
z4.place(x=820,y=410,width=150)


h1 = Label(f5, text="Tops", font=("candara",20,"bold"), bg="snow", fg="purple1")
h1.grid(row=4, column=0, padx=1, pady=10,sticky="w")
z5=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=to)
z5.place(x=820,y=470,width=150)


Foud = Label(f5, text="Saree", font=("candara",20,"bold"), bg="snow", fg="purple1")
Foud.grid(row=5, column=0, padx=1, pady=10,sticky="w")
z6=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=sar)
z6.place(x=820,y=530,width=150)


f6=LabelFrame(win,text="Bill Area",font=("Arial",20,"bold"), bg="snow", fg="purple4",height=400,width=300,border=8,relief="groove")
f6.place(x=1060, y=180, width=460, height=400)

f7=Frame(win,height=120,width=250,bg="snow",border=8,relief="groove")
f7.place(x=10,y=600,width=350,height=120)
btn4=Label(f7,text="Total Cosmetics Bill",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn4.grid(row=0, column=0, padx=1, pady=10,sticky="w")
a1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=tot1)
a1.place(x=200,y=610,width=130)

btn8=Label(f7,text="             Tax",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn8.grid(row=1, column=0, padx=1, pady=10,sticky="w")
a1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=taxe)
a1.place(x=200,y=660,width=130)


f8=Frame(win,height=120,width=250,bg="snow",border=8,relief="groove")
f8.place(x=362,y=600,width=350,height=120)
btn5=Label(f8,text="Total Grocercy Bill",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn5.grid(row=0, column=0, padx=1, pady=10,sticky="w")
b1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=tot2)
b1.place(x=560,y=610,width=130)

btn8=Label(f8,text="             Tax",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn8.grid(row=1, column=0, padx=1, pady=10,sticky="w")
a1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=zaxe)
a1.place(x=560,y=660,width=130)

f9=Frame(win,height=120,width=250,bg="snow",border=8,relief="groove")
f9.place(x=714,y=600,width=350,height=120)
btn7=Label(f9,text="Total Clothes Bill",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn7.grid(row=0, column=0, padx=1, pady=10,sticky="w")
c1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=tot3)
c1.place(x=900,y=610,width=130)

btn11=Label(f9,text="             Tax",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn11.grid(row=1, column=0, padx=1, pady=10,sticky="w")
d1=Entry(win,bg="snow",font=("book antiqua",18),border=2,textvariable=axe)
d1.place(x=900,y=660,width=130)

f10=Frame(win,height=120,width=250,bg="snow",border=8,relief="groove")
f10.place(x=1066,y=600,width=450,height=120)
btn88=Label(f10,text="Total Bill",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn88.grid(row=0,column=4)
e1=Entry(win,bg="snow",font=("book antiqua",18),border=2)
e1.place(x=1210,y=640,width=100)

z12=Button(f10,text="BILL",font=("impact",17),fg="snow",height=3,bg="purple4",width=4,command=bill)
z12.grid(row=0,column=1)

btn8=Label(f10,text="Total Tax",font=("Arial",15),fg="purple4",height=1,bg="snow")
btn8.grid(row=0, column=10, padx=1, pady=10,sticky="w")
g1=Entry(win,bg="snow",font=("book antiqua",18),border=2)
g1.place(x=1408,y=640,width=100)
#aa=Button(f10,text="Bill",font=("arial",12),bg="purple1",fg="white",height=2,width=3)
#aa.grid(row=1,column=9)

f11=Frame(win,height=120,width=250,bg="snow",border=4,relief="groove")
f11.place(x=10,y=730,width=1510,height=70)


bt=Label(f11,text="Your order made our day🥰-Thankyou for Shopping",font=("impact",30),fg="purple4",height=4,bg="snow")
bt.pack()





win.mainloop()