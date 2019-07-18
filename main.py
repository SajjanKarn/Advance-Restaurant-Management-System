from tkinter import *
import random
import time
import datetime
import tkinter.messagebox

#=========================== module imported ==============================#

root = Tk() # ======= Creating GUI Windows ========== #

#============================= FRAMES =====================================#
Tops = Frame(root, bg='Cadet Blue', bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)


Menu_Frame = Frame(root, bg='Cadet Blue', bd=10,relief=RIDGE)
Menu_Frame.pack(side=LEFT)

Receipt_Frame = Frame(root, bg='Cadet Blue', bd=10,relief=RIDGE)
Receipt_Frame.pack(side=RIGHT)





# ========================== INSIDE RECEIPT FRAME ========================#
Button_Frame = Frame(Receipt_Frame, bd=4, bg='powder blue', relief=RIDGE)
Button_Frame.pack(side=BOTTOM) # ===== For Buttons ========#

receipt_Frame = Frame(Receipt_Frame, bd=4, bg='powder blue', relief=RIDGE)
receipt_Frame.pack(side=BOTTOM) # ====== For Printing Bills ========#

Calc_Frame = Frame(Receipt_Frame, bd=4, bg='powder blue', relief=RIDGE)
Calc_Frame.pack(side=TOP) # ======== For Calculator ======== #


# ====================== INSIDE MENU FRAME ===============================#

Cost_Frame = Frame(Menu_Frame, bd=4, bg='powder blue')
Cost_Frame.pack(side=BOTTOM) # =========== For Displaying Cost ====== #


Drinks_Frame = Frame(Menu_Frame, bd=10, bg='powder blue',relief=RIDGE)
Drinks_Frame.pack(side=LEFT) # ===== For Drink Items ========#

Cakes_Frame = Frame(Menu_Frame, bd=10, bg='powder blue',relief=RIDGE)
Cakes_Frame.pack(side=RIGHT) # =========== For Cake Items ====== #






# ========================== TITLE ==========================================#
title_Label = Label(Tops, bd=21, bg='Cadet Blue'
                    ,fg="Cornsilk", font=('arial',70,'bold'),justify=CENTER, 
                    text="Restauurant Management System")
title_Label.pack()


# ==================== DISABLE ENABLE FUNCTION =================================#
def func_Beer():
    if beer.get() == 1:
        txtBeer.configure(state = NORMAL)
        txtBeer.focus()
        txtBeer.delete('0', END)
        E_Beer.set('')
    elif beer.get() == 0:
        txtBeer.configure(state = DISABLED)
        E_Beer.set('0')

def func_hard_soda():
    if hard_soda.get() == 1:
        txtHard_Soda.configure(state = NORMAL)
        txtHard_Soda.focus()
        txtHard_Soda.delete('0', END)
        E_hardSoda.set('')
    elif hard_soda.get() == 0:
        txtHard_Soda.configure(state = DISABLED)
        E_hardSoda.set('0')

def func_expressor():
    if expresso.get() == 1:
        txtExpresso.configure(state = NORMAL)
        txtExpresso.focus()
        txtExpresso.delete('0', END)
        E_Expresso.set('')
    elif expresso.get() == 0:
        txtExpresso.configure(state = DISABLED)
        E_Expresso.set('0')

def func_tea():
    if tea.get() == 1:
        txtTea.configure(state = NORMAL)
        txtTea.focus()
        txtTea.delete('0', END)
        E_Tea.set('')
    elif tea.get() == 0:
        txtTea.configure(state = DISABLED)
        E_Tea.set('0')

def func_soda():
    if soda.get() == 1:
        txtSoda.configure(state = NORMAL)
        txtSoda.focus()
        txtSoda.delete('0', END)
        E_Soda.set('')
    elif soda.get() == 0:
        txtSoda.configure(state = DISABLED)
        E_Soda.set('0')

def func_smoothie():
    if smoothie.get() == 1:
        txtSmoothie.configure(state = NORMAL)
        txtSmoothie.focus()
        txtSmoothie.delete('0', END)
        E_Smoothie.set('')
    elif smoothie.get() == 0:
        txtSmoothie.configure(state = DISABLED)
        E_Smoothie.set('0')

def func_milkshake():
    if milkshake.get() == 1:
        txtMilkShake.configure(state = NORMAL)
        txtMilkShake.focus()
        txtMilkShake.delete('0', END)
        E_MilkShake.set('')
    elif milkshake.get() == 0:
        txtMilkShake.configure(state = DISABLED)
        E_MilkShake.set('0')

def func_juice():
    if juice.get() == 1:
        txtJuice.configure(state = NORMAL)
        txtJuice.focus()
        txtJuice.delete('0', END)
        E_Juice.set('')
    elif beer.get() == 0:
        txtJuice.configure(state = DISABLED)
        E_Juice.set('0')
# ======================== cakes ==============================#


# ============================ Setting Up Drink Items ==========================#
#==== their variables ======#
beer = IntVar()
hard_soda = IntVar()
expresso = IntVar()
tea = IntVar()
soda = IntVar()
smoothie = IntVar()
milkshake = IntVar()
juice = IntVar()


Beer = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Beer", variable=beer,command=func_Beer).grid(row=0,column=0,sticky=W)


Hard_soda = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Hard soda", variable=hard_soda, command=func_hard_soda).grid(row=1,column=0,sticky=W)

Expresso = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Expresso", variable=expresso,command=func_expressor).grid(row=2,column=0,sticky=W)


Tea = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Tea", variable=tea,command=func_tea).grid(row=3,column=0,sticky=W)


Soda = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Soda", variable=soda,command=func_soda).grid(row=4,column=0,sticky=W)



Smoothie = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Smoothie", variable=smoothie,command=func_smoothie).grid(row=5,column=0,sticky=W)


Milkshake = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Milkshake", variable=milkshake, command=func_milkshake).grid(row=6,column=0,sticky=W)


Juice = Checkbutton(Drinks_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Juice", variable=juice, command=func_juice).grid(row=7,column=0,sticky=W)

# =========================== Drinks entries ================================== #
E_Beer = StringVar()
E_hardSoda = StringVar()
E_Expresso = StringVar()
E_Tea = StringVar()
E_Soda = StringVar()
E_Smoothie = StringVar()
E_MilkShake = StringVar()
E_Juice = StringVar()

E_Beer.set('0')
E_hardSoda.set('0')
E_Expresso.set('0')
E_Tea.set('0')
E_Soda.set('0')
E_Smoothie.set('0')
E_MilkShake.set('0')
E_Juice.set('0')

txtBeer = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'),textvariable=E_Beer, width=12, state = DISABLED)
txtBeer.grid(row=0, column=1)

txtHard_Soda = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'),textvariable=E_hardSoda, width=12, state = DISABLED)
txtHard_Soda.grid(row=1, column=1)

txtExpresso = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_Expresso,width=12, state = DISABLED)
txtExpresso.grid(row=2, column=1)


txtTea = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_Tea,width=12, state = DISABLED)
txtTea.grid(row=3, column=1)


txtSoda = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_Soda,width=12, state = DISABLED)
txtSoda.grid(row=4, column=1)

txtSmoothie = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'),textvariable=E_Smoothie, width=12, state = DISABLED)
txtSmoothie.grid(row=5, column=1)

txtMilkShake = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'),textvariable=E_MilkShake, width=12, state = DISABLED)
txtMilkShake.grid(row=6, column=1)

txtJuice = Entry(Drinks_Frame, bd=6, font=('arial',16,'bold'),textvariable=E_Juice ,width=12, state = DISABLED)
txtJuice.grid(row=7, column=1)








# ============================ Setting Up Cake Items ==========================#

def func_poundCake():
    if poundCake.get() == 1:
        txtpoundCake.configure(state = NORMAL)
        txtpoundCake.focus()
        txtpoundCake.delete('0', END)
        E_PoundCake.set('')
    elif poundCake.get() == 0:
        txtpoundCake.configure(state = DISABLED)
        E_PoundCake.set('0')

def func_spongeCake():
    if spongeCake.get() == 1:
        txtspongeCake.configure(state = NORMAL)
        txtspongeCake.focus()
        txtspongeCake.delete('0', END)
        E_SpongeCake.set('')
    elif spongeCake.get() == 0:
        txtspongeCake.configure(state = DISABLED)
        E_SpongeCake.set('0')


def func_butterCake():
    if butterCake.get() == 1:
        txtbutterCake.configure(state = NORMAL)
        txtbutterCake.focus()
        txtbutterCake.delete('0', END)
        E_ButterCake.set('')
    elif butterCake.get() == 0:
        txtbutterCake.configure(state = DISABLED)
        E_ButterCake.set('0')

def func_bakedFlourlessCake():
    if bakedFlourlessCake.get() == 1:
        txtbakedFlourlessCake.configure(state = NORMAL)
        txtbakedFlourlessCake.focus()
        txtbakedFlourlessCake.delete('0', END)
        E_FlourLessCake.set('')
    elif bakedFlourlessCake.get() == 0:
        txtbakedFlourlessCake.configure(state = DISABLED)
        E_FlourLessCake.set('0')

def func_chiffonCake():
    if chiffonCake.get() == 1:
        txtchiffonCake.configure(state = NORMAL)
        txtchiffonCake.focus()
        txtchiffonCake.delete('0', END)
        E_ChiffonCake.set('')
    elif chiffonCake.get() == 0:
        txtchiffonCake.configure(state = DISABLED)
        E_ChiffonCake.set('0')
        
def func_carrotCake():
    if carrotCake.get() == 1:
        txtcarrotCake.configure(state = NORMAL)
        txtcarrotCake.focus()
        txtcarrotCake.delete('0', END)
        E_CarrotCake.set('')
    elif beer.get() == 0:
        txtcarrotCake.configure(state = DISABLED)
        E_CarrotCake.set('0')

def func_redVelvetCake():
    if redVelvetCake.get() == 1:
        txtredVelvetCake.configure(state = NORMAL)
        txtredVelvetCake.focus()
        txtredVelvetCake.delete('0', END)
        E_RedCake.set('')
    elif redVelvetCake.get() == 0:
        txtredVelvetCake.configure(state = DISABLED)
        E_RedCake.set('0')

def func_angelFoodCake():
    if angelFoodCake.get() == 1:
        txtangelFoodCake.configure(state = NORMAL)
        txtangelFoodCake.focus()
        txtangelFoodCake.delete('0', END)
        E_AngelCake.set('')
    elif angelFoodCake.get() == 0:
        txtangelFoodCake.configure(state = DISABLED)
        E_AngelCake.set('0')


poundCake = IntVar()
spongeCake = IntVar()
butterCake = IntVar()
bakedFlourlessCake = IntVar()
chiffonCake = IntVar()
carrotCake = IntVar()
redVelvetCake = IntVar()
angelFoodCake = IntVar()




PoundCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Pound Cake", variable=poundCake,command=func_poundCake).grid(row=0,column=0,sticky=W)


SpongeCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Sponge Cake", variable=spongeCake,command=func_spongeCake).grid(row=1,column=0,sticky=W)


ButterCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Butter Cake", variable=butterCake,command=func_butterCake).grid(row=2,column=0,sticky=W)


BakedFlourlessCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Baked Flourless Cake", variable=bakedFlourlessCake,command=func_bakedFlourlessCake).grid(row=3,column=0,sticky=W)

ChiffonCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Chiffon Cake", variable=chiffonCake,command=func_chiffonCake).grid(row=4,column=0,sticky=W)



CarrotCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Carrot Cake\t", variable=carrotCake,command=func_carrotCake).grid(row=5,column=0,sticky=W)



RedVelvetCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Red Velvet Cake\t", variable=redVelvetCake,command=func_redVelvetCake).grid(row=6,column=0,sticky=W)


AngelFoodCake = Checkbutton(Cakes_Frame, bg='powder blue', font=('arial',18,'bold'), 
                    onvalue=1, offvalue=0, text="Angel Food Cake\t", variable=angelFoodCake,command=func_angelFoodCake).grid(row=7,column=0,sticky=W)

# =========================== Cake entries ================================== #
#=== their variables =======#
E_PoundCake = StringVar()
E_SpongeCake = StringVar()
E_ButterCake = StringVar()
E_FlourLessCake = StringVar()
E_ChiffonCake = StringVar()
E_CarrotCake = StringVar()
E_RedCake = StringVar()
E_AngelCake = StringVar()


E_PoundCake.set('0')
E_SpongeCake.set('0')
E_ButterCake.set('0')
E_FlourLessCake.set('0')
E_ChiffonCake.set('0')
E_CarrotCake.set('0')
E_RedCake.set('0')
E_AngelCake.set('0')

txtpoundCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_PoundCake,width=12, state = DISABLED)
txtpoundCake.grid(row=0, column=1)

txtspongeCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), width=12, textvariable=E_SpongeCake,state = DISABLED)
txtspongeCake.grid(row=1, column=1)

txtbutterCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), width=12, textvariable=E_ButterCake,state = DISABLED)
txtbutterCake.grid(row=2, column=1)


txtbakedFlourlessCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), width=12, textvariable=E_FlourLessCake,state = DISABLED)
txtbakedFlourlessCake.grid(row=3, column=1)


txtchiffonCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_ChiffonCake,width=12, state = DISABLED)
txtchiffonCake.grid(row=4, column=1)

txtcarrotCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_CarrotCake,width=12, state = DISABLED)
txtcarrotCake.grid(row=5, column=1)

txtredVelvetCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_RedCake,width=12, state = DISABLED)
txtredVelvetCake.grid(row=6, column=1)

txtangelFoodCake = Entry(Cakes_Frame, bd=6, font=('arial',16,'bold'), textvariable=E_AngelCake,width=12, state = DISABLED)
txtangelFoodCake.grid(row=7, column=1)









# ========================== Inside Receipt frame ====================================#
txtReceipt = Text(receipt_Frame, width=50,height=15,bg="white", font=('arial',12,'bold'), bd=5,)
txtReceipt.pack()


# =============== calculator functions ======================#

def Reset():

    CostOfDrinks.set("")
    CostOfCakes.set("")
    ServiceCharge.set("")
    PaidTax.set("")
    SubTotal.set("")
    Total.set("")


    # ====== Drinks ===== #
    E_Beer.set('0')
    E_hardSoda.set('0')
    E_Expresso.set('0')
    E_Tea.set('0')
    E_Soda.set('0')
    E_Smoothie.set('0')
    E_MilkShake.set('0')
    E_Juice.set('0')


    # ==== Cakes ====== #
    E_PoundCake.set('0')
    E_SpongeCake.set('0')
    E_ButterCake.set('0')
    E_FlourLessCake.set('0')
    E_ChiffonCake.set('0')
    E_CarrotCake.set('0')
    E_RedCake.set('0')
    E_AngelCake.set('0')

    #===== drinks check button =====#
    beer.set('0')
    hard_soda.set('0')
    expresso.set('0')
    tea.set('0')
    soda.set('0')
    smoothie.set('0')
    milkshake.set('0')
    juice.set('0')

    # ======= cakes checkbutton ======#
    poundCake.set('0')
    spongeCake.set('0')
    butterCake.set('0')
    bakedFlourlessCake.set('0')
    chiffonCake.set('0')
    carrotCake.set('0')
    redVelvetCake.set('0')
    angelFoodCake.set('0')

    # ====== receipt Text =======#
    txtReceipt.delete(1.0, END)

    # ====== disabling all texts ====#
    txtBeer.configure(state=DISABLED)
    txtHard_Soda.configure(state=DISABLED)
    txtExpresso.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtSoda.configure(state=DISABLED)
    txtSmoothie.configure(state=DISABLED)
    txtMilkShake.configure(state=DISABLED)
    txtJuice.configure(state=DISABLED)

    txtpoundCake.configure(state=DISABLED)
    txtspongeCake.configure(state=DISABLED)
    txtbutterCake.configure(state=DISABLED)
    txtbakedFlourlessCake.configure(state=DISABLED)
    txtchiffonCake.configure(state=DISABLED)
    txtcarrotCake.configure(state=DISABLED)
    txtredVelvetCake.configure(state=DISABLED)
    txtangelFoodCake.configure(state=DISABLED)
    
def CostTotal():
    COSTBEAR = float(E_Beer.get())
    COSTHARDSODA = float(E_hardSoda.get())
    COSTEXPRESSO  = float(E_Expresso.get())
    COSTTEA  = float(E_Tea.get())
    COSTSODA  = float(E_Soda.get())
    COSTSMOOTHIE  = float(E_Smoothie.get())
    COSTMILKSHAKE = float(E_MilkShake.get())
    COSTJUICE  = float(E_Juice.get())

    COSTPOUNDCAKE  = float(E_PoundCake.get())
    COSTSPONGECAKE  = float(E_SpongeCake.get())
    COSTBUTTERCAKE  = float(E_ButterCake.get())
    COSTFLOURLESSCAKE  = float(E_FlourLessCake.get())
    COSTCHIFFONCAKE  = float(E_ChiffonCake.get())
    COSTCARROTCAKE  = float(E_CarrotCake.get())
    COSTREDCAKE  = float(E_RedCake.get())
    COSTANGELCAKE  = float(E_AngelCake.get())
    TotalCostOfDrinks = (COSTBEAR * 200) + (COSTHARDSODA * 60) + (COSTEXPRESSO * 150) + (COSTTEA * 25) + (COSTSODA * 50) + (COSTSMOOTHIE * 180) + (COSTMILKSHAKE * 90) + (COSTJUICE * 70)
    TotalCostOfCakes = (COSTPOUNDCAKE * 600)+(COSTSPONGECAKE * 700)+(COSTBUTTERCAKE * 750)+(COSTFLOURLESSCAKE * 650)+(COSTCHIFFONCAKE * 500)+(COSTCARROTCAKE * 850)+(COSTREDCAKE * 400)+(COSTANGELCAKE * 600)

    OverAllCostOfDrinks = "रू", str(('%.2f' % (TotalCostOfDrinks)))
    OverAllCostOfCakes = "रू", str(("%.2f" % (TotalCostOfCakes)))
    OverAllCostOfServiceCharge = "रू", str("%.2f" % (2))
    OverAllCostOfSubTotal = "रू", str("%.2f" % (TotalCostOfDrinks+TotalCostOfCakes))
    OverAllCostOfTax = "रू", str("%.2f" % ((TotalCostOfDrinks + TotalCostOfCakes + 2) * 0.13))
    ActualTaxAmount = ((TotalCostOfDrinks + TotalCostOfCakes + 2) * 0.13)
    OverAllTotalCost = "रू", str("%.2f" % ((TotalCostOfDrinks + TotalCostOfCakes + 2) + 2 + ActualTaxAmount))

    CostOfDrinks.set(OverAllCostOfDrinks)
    CostOfCakes.set(OverAllCostOfCakes) 
    ServiceCharge.set(OverAllCostOfServiceCharge)
    PaidTax.set(OverAllCostOfTax)
    SubTotal.set(OverAllCostOfSubTotal)
    Total.set(OverAllTotalCost)

def Receipt():
    x = random.randint(10680, 60321)
    random_ref = str(x)
    txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t' + 'BILL: ' + random_ref + '\n')
    txtReceipt.insert(END, 'Items:\t\t\t\t' + 'Cost Of Items' + '\n')
    txtReceipt.insert(END, 'Beer:\t\t\t\t' + E_Beer.get() + '\n')
    txtReceipt.insert(END, 'Hard Soda:\t\t\t\t' + E_hardSoda.get() + '\n')
    txtReceipt.insert(END, 'Tea:\t\t\t\t' + E_Tea.get() + '\n')
    txtReceipt.insert(END, 'Soda:\t\t\t\t' + E_Soda.get() + '\n')
    txtReceipt.insert(END, 'Smoothie:\t\t\t\t' + E_Smoothie.get() + '\n')
    txtReceipt.insert(END, 'Milkshake:\t\t\t\t' + E_MilkShake.get() + '\n')
    txtReceipt.insert(END, 'Juice:\t\t\t\t' + E_Juice.get() + '\n')

    txtReceipt.insert(END, 'Pound Cake:\t\t\t\t' + E_PoundCake.get() + '\n')
    txtReceipt.insert(END, 'Sponge Cake:\t\t\t\t' + E_SpongeCake.get() + '\n')
    txtReceipt.insert(END, 'Butter Cake:\t\t\t\t' + E_ButterCake.get() + '\n')
    txtReceipt.insert(END, 'Baked Flour Cake:\t\t\t\t' + E_FlourLessCake.get() + '\n')
    txtReceipt.insert(END, 'Chiffon Cake:\t\t\t\t' + E_ChiffonCake.get() + '\n')
    txtReceipt.insert(END, 'Carrot Cake:\t\t\t\t' + E_CarrotCake.get() + '\n')
    txtReceipt.insert(END, 'RedVelvet Cake:\t\t\t\t' + E_RedCake.get() + '\n')
    txtReceipt.insert(END, 'AngelFood Cake:\t\t\t\t' + E_AngelCake.get() + '\n')

    txtReceipt.insert(END, 'Cost Of Drinks:\t\t\t\t' + CostOfDrinks.get()+ 
                    '\nTax Paid:\t\t\t\t' + PaidTax.get() + '\n')

    txtReceipt.insert(END, 'Cost Of Cakes:\t\t\t\t' + CostOfCakes.get() + 
                    '\nSub Total Cost:\t\t\t\t' + SubTotal.get() + '\n')

    txtReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get() + 
                    '\nTotal Cost:\t\t\t\t' + Total.get() + '\n')


def btnExit():
    exit_value = tkinter.messagebox.askyesno("Exit System", "Do You Really Want To Close This System?")
    if exit_value > 0:
        root.destroy()
        return

operator = ""
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    calc_insert.set(operator)

def btnClear():
    global operator
    operator = ""
    calc_insert.set(operator)

def btnEqual():
    try:
        global operator
        solve = str(eval(operator))
        calc_insert.set(solve)
        operator = ""
    except ZeroDivisionError:
        calc_insert.set("Cannot Divide By Zero")


#=========================== CALCULATOR DISPLAY =====================================#
calc_insert = StringVar()
txtDisplay = Entry(Calc_Frame, width=50, font=('arial',12,'bold'),insertwidth=4,bd=4, justify=RIGHT, bg='white', textvariable=calc_insert)
txtDisplay.grid(row=0,column=0,columnspan=4, pady=1)
txtDisplay.insert(0, '0')



# ======================= INSIDE CALCULATOR FRAME SETTING UP BUTTONS ============================#
btn9 = Button(Calc_Frame, text='9', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('9')).grid(row=2,column=0)


btn8 = Button(Calc_Frame, text='8', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('8')).grid(row=2,column=1)


btn7 = Button(Calc_Frame, text='7', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('7')).grid(row=2,column=2)


btnadd = Button(Calc_Frame, text='+', bd=7,bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('+')).grid(row=2,column=3)


# ======= part 2=========#

btn6 = Button(Calc_Frame, text='6', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('6')).grid(row=3,column=0)


btn5 = Button(Calc_Frame, text='5', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('5')).grid(row=3,column=1)


btn4 = Button(Calc_Frame, text='4', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('4')).grid(row=3,column=2)


btnsub = Button(Calc_Frame, text='-', bd=7,bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('-')).grid(row=3,column=3)

# ======= part 3=========#

btn3 = Button(Calc_Frame, text='3', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('3')).grid(row=4,column=0)


btn2 = Button(Calc_Frame, text='2', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('2')).grid(row=4,column=1)


btn1 = Button(Calc_Frame, text='1', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('1')).grid(row=4,column=2)


btnmul = Button(Calc_Frame, text='*', bd=7,bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('*')).grid(row=4,column=3)


# ======= part 4=========#

btn0 = Button(Calc_Frame, text='0', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('0')).grid(row=5,column=0)


btnC = Button(Calc_Frame, text='C', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = btnClear).grid(row=5,column=1)


btnEql = Button(Calc_Frame, text='=', bd=7,bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = btnEqual).grid(row=5,column=2)


btndiv = Button(Calc_Frame, text='/', bd=7, bg='gold', width=10, 
                font=('arial',12,'bold'),fg='black', command = lambda:btnClick('/')).grid(row=5,column=3)










# ===================== setting buttons in Receipt frame TOTAL, RESET, CLEAR, EXIT ============#
btnReceipt = Button(Button_Frame, width=7, height=1, text="RECEIPT",
                    font=('arial',16,'bold'),bd=8,bg='powder blue',command=Receipt)
btnReceipt.grid(row=2,column=0)

btnTotal = Button(Button_Frame, width=7, height=1, text="TOTAL", 
                    font=('arial',16,'bold'),bd=8,bg='powder blue',command=CostTotal)
btnTotal.grid(row=2,column=1)

btnReset = Button(Button_Frame, width=7, height=1, text="RESET",
                     font=('arial',16,'bold'),bd=8,bg='powder blue',command=Reset)
btnReset.grid(row=2,column=2)

btnExit = Button(Button_Frame, width=7, height=1, text="EXIT",
                     font=('arial',16,'bold'),bd=8,bg='powder blue',command=btnExit)
btnExit.grid(row=2,column=3)





# ====================== setting up costs frame ==============================#
#==== their variables======#
CostOfDrinks = StringVar()
CostOfCakes = StringVar()
ServiceCharge = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
Total = StringVar()




lblCostOfDrinks = Label(Cost_Frame, text='Cost Of Drinks', font=('arial',18,'bold'), 
                        bd=10, bg = 'powder blue',fg="black").grid(row=0,column=0,sticky=W)

txtCostOfDrinks = Entry(Cost_Frame, bd=4, justify=RIGHT, insertwidth=4, 
                        font=('arial',14,'bold'),width=21, textvariable=CostOfDrinks).grid(row=0,column=1)



lblCostOfCakes = Label(Cost_Frame, text='Cost Of Cakes', font=('arial',18,'bold'), 
                        bd=10, bg = 'powder blue',fg="black").grid(row=1,column=0,sticky=W)

txtCostOfCakes = Entry(Cost_Frame, bd=4, justify=RIGHT, insertwidth=4, 
                        font=('arial',14,'bold'),width=21, textvariable=CostOfCakes).grid(row=1,column=1)




lblServiceCharge = Label(Cost_Frame, text='Service Charge', font=('arial',18,'bold'), 
                        bd=10, bg = 'powder blue',fg="black").grid(row=2,column=0,sticky=W)

txtServiceCharge = Entry(Cost_Frame, bd=4, justify=RIGHT, insertwidth=4, 
                        font=('arial',14,'bold'),width=21, textvariable=ServiceCharge).grid(row=2,column=1)




lblPaidTax = Label(Cost_Frame, text='Paid Tax', font=('arial',18,'bold'), 
                        bd=10, bg = 'powder blue',fg="black").grid(row=0,column=2,sticky=W)

txtPaidTax = Entry(Cost_Frame, bd=4, justify=RIGHT, insertwidth=4, 
                        font=('arial',14,'bold'),width=21, textvariable=PaidTax).grid(row=0,column=3)




lblSubTotal = Label(Cost_Frame, text='Sub Total', font=('arial',18,'bold'), 
                        bd=10, bg = 'powder blue',fg="black").grid(row=1,column=2,sticky=W)

txtSubTotal = Entry(Cost_Frame, bd=4, justify=RIGHT, insertwidth=4, 
                        font=('arial',14,'bold'),width=21, textvariable=SubTotal).grid(row=1,column=3)




lblTotal = Label(Cost_Frame, text='Total', font=('arial',18,'bold'), 
                        bd=10, bg = 'powder blue',fg="black").grid(row=2,column=2,sticky=W)

txtTotal = Entry(Cost_Frame, bd=4, justify=RIGHT, insertwidth=4, 
                        font=('arial',14,'bold'),width=21, textvariable=Total).grid(row=2,column=3)




# ================= root configuration ======================================= #
root.config(background='Cadet Blue')
root.geometry("1920x1080")
root.title("Restauurant Management System")
root.mainloop()