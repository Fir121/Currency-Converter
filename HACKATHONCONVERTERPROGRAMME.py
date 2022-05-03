'''
IMPORTING REQUIRED MODULES [22 lines]
'''
try:
    import requests, json
except ImportError:
    print('You require the module requests AND json')
    quit()
try:
    import datetime
except ImportError:
    print('You dont have module: datetime which is required for this conversion')
    quit()
try:
    from tkinter import *
except ImportError:
    try:
        from Tkinter import *
    except ImportError:
        print('You require the Tkinter module to run this')
        quit()
try:
    import time
except ImportError:
    None
    
'''
DEFINING CONVERSION FUNCTIONS [122 lines]
'''
#defining mass conversion
mass=['pounds to kilograms','kilograms to pounds','stones to pounds','pounds to stones','stones to kilograms','kilograms to stones']
pounds_c=2.204623 
stone_c=0.157473 
def massconversion(conversion_type,value):
    if value<0:
        return 'Negative Mass is not possible'
    if conversion_type==mass[0]:
        return value/pounds_c
    elif conversion_type==mass[1]:
        return value*pounds_c
    elif conversion_type==mass[2]:
        return value*14
    elif conversion_type==mass[3]:
        return value/14
    elif conversion_type==mass[4]:
        return value/stone_c
    elif conversion_type==mass[5]:
        return value*stone_c

#defining length conversion
length=['inches to centimetres','centimetres to inches','yards to metres','metres to yards','miles to kilometres','kilometres to miles']
inches_c=0.3937007874
yards_c=1.0936
miles_c=0.62137119
def lengthconversion(conversion_type,value):
    if value<0:
        return 'Negative Length is not possible'
    if conversion_type==length[0]:
        return value/inches_c
    elif conversion_type==length[1]:
        return value*inches_c
    elif conversion_type==length[2]:
        return value/yards_c
    elif conversion_type==length[3]:
        return value*yards_c
    elif conversion_type==length[4]:
        return value/miles_c
    elif conversion_type==length[5]:
        return value*miles_c

#defining speed conversions
speed=['Mph to Kmph','Kmph to Mph','Knots to Mph','Mph to Knots','Knots to Kmph','Kmph to Knots']
mph_c=0.6213711922
knots_c=0.868976
kmph_c=1.852 
def speedconversion(conversion_type,value):
    if conversion_type==speed[0]:
        return value/mph_c
    elif conversion_type==speed[1]:
        return value*mph_c
    elif conversion_type==speed[2]:
        return value/knots_C
    elif conversion_type==speed[3]:
        return value*knots_c
    elif conversion_type==speed[4]:
        return value*kmph_c
    elif conversion_type==speed[5]:
        return value/kmph_c

#defining temperature conversions
temp=['°F to °C','°C to °F','Kelvin to °F','°F to Kelvin','Kelvin to °C','°C to Kelvin']
def tempconversion(conversion_type,value):
    if conversion_type==temp[0]:
        return ((value-32)*5)/9
    elif conversion_type==temp[1]:
        return ((value/5)*9)+32
    elif conversion_type==temp[2]:
        return (((value-273.15)*9)/5)+32
    elif conversion_type==temp[3]:
        return (((value-32)*5)/9)+273.15
    elif conversion_type==temp[4]:
        return value-273.15
    elif conversion_type==temp[5]:
        return value+273.15

#defining currency conversions
currency=['aed to usd','usd to aed','gbp to usd','usd to gbp','aed to gbp','gbp to aed']
try:
    response=requests.get('https://api.ratesapi.io/api/latest?base=GBP')
    api_data=response.json()
    gbp_to_usd_c=api_data['rates']['USD']
except:
    print('Could not access API, using a default valuation')
    gbp_to_usd_c=1.2568348959
usd_to_aed=3.67
def moneyconversion(conversion_type,value):
    if value<0:
        return 'Negative Currency Value is not possible'
    if conversion_type==currency[0]:
        return value/usd_to_aed
    elif conversion_type==currency[1]:
        return value*usd_to_aed
    elif conversion_type==currency[2]:
        return value*gbp_to_usd_c
    elif conversion_type==currency[3]:
        return value/gbp_to_usd_c
    elif conversion_type==currency[4]:
        return moneyconversion('usd to gbp',moneyconversion('aed to usd',value))
    elif conversion_type==currency[5]:
        return moneyconversion('usd to aed',moneyconversion('gbp to usd',value))

#defining date conversions
nowtime=datetime.datetime.now()
introduction_year=1752
datelist=['Gregorian to Julian', 'Julian To Gregorian']
def dateconversion(typeofconversion,y=nowtime.year,m=nowtime.month,d=nowtime.day):
    checkvar=0
    dayaddition=(y-introduction_year)/128
    sub=int(dayaddition+11)
    now_date=datetime.date(y,m,d)
    if typeofconversion=='Gregorian to Julian':
        if now_date.year<=1752:
            checkvar=1
        d=now_date- datetime.timedelta(days=sub)
    if typeofconversion=='Julian To Gregorian':
        if now_date.year<=1752:
            checkvar=1
        d=now_date+ datetime.timedelta(days=sub)
    if checkvar!=0:
        return [d,'You are attempting to convert a date older than 1752,\nWhen the Gregorian Calendar was first introduced.\nThere may be errors in this conversion.']
    return d

'''
INITIALISING INTERFACE AND INTERFACE FUNCTIONS [293 lines]
'''
master=Tk()
master.title('Universal Converter')
master.geometry('700x340')
master.resizable(width=False, height=False) #fixing window size
conversiontype=['Mass','Length','Speed','Temperature','Currency','Date']

def clearscreen():
    widget_list = master.winfo_children()
    for item in widget_list:
        if isinstance(item,Menu): #checking if widget is menu to avoid removal
            continue
        else:
            item.destroy()
            
#defining pop up used for errors
def popupmsg(msg):
    popup = Tk()
    popup.wm_title("ERROR")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Ok", command = lambda:[popup.destroy()])
    B1.pack(pady=10)
    popup.mainloop()
    
def conversionfunction(c_type):
    clearscreen()
    if c_type==conversiontype[0]:
        def answer(value):
            try:
                conv_val=massconversion(masstype.get(),float(value))
            except ValueError:
                popupmsg('Cannot convert this value')
                return None
            if type(conv_val)==str:
                popupmsg(conv_val)
                return None
            unit=masstype.get().split()[2]
            value_disp.config(text=(('\n\n\n{:.4f} '.format(conv_val))+unit))
        text2=Label(master,text='\n\n\nInput Value: ')
        text2.pack(pady=3,padx=(20,435))
        value=Entry(master,bd=5,width=20,)
        value.bind('<Return>', (lambda event: answer(value.get())))
        value.pack(side=LEFT,padx=(100,2),anchor=N)
        value.insert(0, '0')
        masstype = StringVar(master)
        masstype.set(mass[0])
        convtypemenu = OptionMenu(master, masstype, *mass)
        convtypemenu.pack(padx=(0,90),side=RIGHT,anchor=N)
        unit=masstype.get().split()[2]
        value_disp=Label(master,text=f'\n\n\n 0 {unit}', font=("Helvetica", 14),anchor=N, justify=CENTER)
        value_disp.pack(anchor=CENTER)
    if c_type==conversiontype[1]:
        def answer(value):
            try:
                conv_val=lengthconversion(lengthtype.get(),float(value))
            except ValueError:
                popupmsg('Cannot convert this value')
                return None
            if type(conv_val)==str:
                popupmsg(conv_val)
                return None
            unit=lengthtype.get().split()[2]
            value_disp.config(text=(('\n\n\n{:.4f} '.format(conv_val))+unit))
        text2=Label(master,text='\n\n\nInput Value: ')
        text2.pack(pady=3,padx=(20,435))
        value=Entry(master,bd=5,width=20,)
        value.bind('<Return>', (lambda event: answer(value.get())))
        value.pack(side=LEFT,padx=(100,2),anchor=N)
        value.insert(0, '0')
        lengthtype = StringVar(master)
        lengthtype.set(length[0])
        convtypemenu = OptionMenu(master, lengthtype, *length)
        convtypemenu.pack(padx=(0,90),side=RIGHT,anchor=N)
        unit=lengthtype.get().split()[2]
        value_disp=Label(master,text=f'\n\n\n 0 {unit}', font=("Helvetica", 14),anchor=N, justify=CENTER)
        value_disp.pack(anchor=CENTER)
    if c_type==conversiontype[2]:
        def answer(value):
            try:
                conv_val=speedconversion(speedtype.get(),float(value))
            except ValueError:
                popupmsg('Cannot convert this value')
                return None
            unit=speedtype.get().split()[2]
            value_disp.config(text=(('\n\n\n{:.4f} '.format(conv_val))+unit))
        text2=Label(master,text='\n\n\nInput Value: ')
        text2.pack(pady=3,padx=(20,435))
        value=Entry(master,bd=5,width=20,)
        value.bind('<Return>', (lambda event: answer(value.get())))
        value.pack(side=LEFT,padx=(100,2),anchor=N)
        value.insert(0, '0')
        speedtype = StringVar(master)
        speedtype.set(speed[0])
        convtypemenu = OptionMenu(master, speedtype, *speed)
        convtypemenu.pack(padx=(0,90),side=RIGHT,anchor=N)
        unit=speedtype.get().split()[2]
        value_disp=Label(master,text=f'\n\n\n 0 {unit}', font=("Helvetica", 14),anchor=N, justify=CENTER)
        value_disp.pack(anchor=CENTER)
    if c_type==conversiontype[3]:
        def answer(value):
            try:
                conv_val=tempconversion(temptype.get(),float(value))
            except ValueError:
                popupmsg('Cannot convert this value')
                return None
            unit=temptype.get().split()[2]
            value_disp.config(text=(('\n\n\n{:.4f} '.format(conv_val))+unit))
        text2=Label(master,text='\n\n\nInput Value: ')
        text2.pack(pady=3,padx=(20,435))
        value=Entry(master,bd=5,width=20,)
        value.bind('<Return>', (lambda event: answer(value.get())))
        value.pack(side=LEFT,padx=(100,2),anchor=N)
        value.insert(0, '0')
        temptype = StringVar(master)
        temptype.set(temp[0])
        convtypemenu = OptionMenu(master, temptype, *temp)
        convtypemenu.pack(padx=(0,90),side=RIGHT,anchor=N)
        unit=temptype.get().split()[2]
        value_disp=Label(master,text=f'\n\n\n 0 {unit}', font=("Helvetica", 14),anchor=N, justify=CENTER)
        value_disp.pack(anchor=CENTER)
    if c_type==conversiontype[4]:
        def answer(value):
            try:
                conv_val=moneyconversion(currencytype.get(),float(value))
            except ValueError:
                popupmsg('Cannot convert this value')
                return None
            if type(conv_val)==str:
                popupmsg(conv_val)
                return None
            unit=currencytype.get().split()[2]
            value_disp.config(text=(('\n\n\n{:.4f} '.format(conv_val))+unit))
        text2=Label(master,text='\n\n\nInput Value: ')
        text2.pack(pady=3,padx=(20,435))
        value=Entry(master,bd=5,width=20)
        value.bind('<Return>', (lambda event: answer(value.get())))
        value.pack(side=LEFT,padx=(100,2),anchor=N)
        value.insert(0, '0')
        currencytype = StringVar(master)
        currencytype.set(currency[0])
        convtypemenu = OptionMenu(master, currencytype, *currency)
        convtypemenu.pack(padx=(0,90),side=RIGHT,anchor=N)
        unit=currencytype.get().split()[2]
        value_disp=Label(master,text=f'\n\n\n 0 {unit}', font=("Helvetica", 14),anchor=N, justify=CENTER)
        value_disp.pack(anchor=CENTER)
        
    if c_type==conversiontype[5]:
        def answer(t,y,m,d):
            global answerlbl
            converted=dateconversion(t,y,m,d)
            if type(converted)==list:
                answerlbl.config(text=f'\n\n{converted[0]}')
                popupmsg(converted[1])
            answerlbl.config(text=f'\n\n{converted}')

        def checkvalues(t,y,m,d):
            chkvar=0
            try:
                y=int(y)
                m=int(m)
                d=int(d)
            except:
                chkvar=1
                popupmsg('Cannot convert this value')
            if m>12 or m<0:
                chkvar=1
                popupmsg('Month value invalid')
            try:
                datetime.date(y,m,d)
            except:
                chkvar=1
                popupmsg('Invalid Date')
            if chkvar==1:
                return 
            return answer(t,y,m,d)
        
        def proceed(dateconvtype):
            global lbl,year,month,day,answerlbl,confirm2
            if dateconvtype=='Gregorian to Julian':
                try:
                    lbl.config(text='Gregorian Date: ')
                    year.delete(0, END)
                    year.insert(0, f'{nowtime.year}')
                    month.delete(0, END)
                    month.insert(0, f'{nowtime.month}')
                    day.delete(0, END)
                    day.insert(0, f'{nowtime.day}')
                    confirm2.config(command=lambda: (checkvalues('Gregorian to Julian',(year.get()),(month.get()),(day.get()))))
                    answerlbl.config(text=f'\n\n{dateconversion("Gregorian to Julian")}')
                except:
                    lbl=Label(master,text='Gregorian Date: ')
                    lbl.pack(side=LEFT,padx=(100,2),anchor=N,pady=(5,0))
                    year=Entry(master,bd=5,width=20)
                    year.pack(side=LEFT,padx=(0,2),anchor=N,pady=(5,0))
                    year.insert(0, f'{nowtime.year}')
                    month=Entry(master,bd=5,width=20)
                    month.pack(side=LEFT,padx=(0,2),anchor=N,pady=(5,0))
                    month.insert(0, f'{nowtime.month}')
                    day=Entry(master,bd=5,width=20)
                    day.pack(side=LEFT,padx=(0,0),anchor=N,pady=(5,0))
                    day.insert(0, f'{nowtime.day}')
                    confirm2=Button(master,text='Convert',command=lambda: (checkvalues('Gregorian to Julian',(year.get()),(month.get()),(day.get()))))
                    confirm2.pack()
                    answerlbl=Label(master,text=f'\n\n{dateconversion("Gregorian to Julian")}',font=("Helvetica", 14))
                    answerlbl.pack()
                
            elif dateconvtype=='Julian To Gregorian':
                try:
                    lbl.config(text='Julian Date: ')
                    d=dateconversion('Gregorian to Julian')
                    year.delete(0, END)
                    year.insert(0, f'{d.year}')
                    month.delete(0, END)
                    month.insert(0, f'{d.month}')
                    day.delete(0, END)
                    day.insert(0, f'{d.day}')
                    confirm2.config( command=lambda: (checkvalues('Julian To Gregorian',(year.get()),(month.get()),(day.get()))))
                    answerlbl.config(text=f'\n\n{dateconversion("Julian To Gregorian",int(year.get()),int(month.get()),int(day.get()))}')
                except:
                    lbl=Label(master,text='Julian Date: ')
                    d=dateconversion('Gregorian to Julian')
                    lbl.pack(side=LEFT,padx=(100,2),anchor=N,pady=(5,0))
                    year=Entry(master,bd=5,width=20)
                    year.pack(side=LEFT,padx=(0,2),anchor=N,pady=(5,0))
                    year.insert(0, f'{d.year}')
                    month=Entry(master,bd=5,width=20)
                    month.pack(side=LEFT,padx=(0,2),anchor=N,pady=(5,0))
                    month.insert(0, f'{d.month}')
                    day=Entry(master,bd=5,width=20)
                    day.pack(side=LEFT,padx=(0,0),anchor=N,pady=(5,0))
                    day.insert(0, f'{d.day}')
                    confirm2=Button(master,text='Convert', command=lambda: (checkvalues('Julian To Gregorian',(year.get()),(month.get()),(day.get()))))
                    confirm2.pack()
                    answerlbl=Label(master,text=f'\n\n{dateconversion("Julian To Gregorian",int(year.get()),int(month.get()),int(day.get()))}',font=("Helvetica", 14))
                    answerlbl.pack()
                    
        dateconv = StringVar(master)
        dateconv.set(datelist[0])
        convtypemenu = OptionMenu(master, dateconv, *datelist)
        convtypemenu.pack(padx=(110,90),side=TOP,anchor=N,pady=(70,0))
        confirmbutton=Button(master,text='Select',command=lambda: (proceed(dateconv.get())))
        confirmbutton.pack(padx=(17,0),side=TOP,anchor=N,pady=(0,0))
    
def initialize():
    try:
        clearscreen()
    except Exception as e:
        print(e)
        None
    conv_type = StringVar(master)
    conv_type.set(conversiontype[0])
    text=Label(master,text='Conversion type: ')
    text.pack(pady=(100,0))
    convmenu = OptionMenu(master, conv_type, *conversiontype)
    convmenu.pack(pady=(0,5))
    selectbutton=Button(master,text='Select',command=lambda:[conversionfunction(conv_type.get())])
    selectbutton.pack()
    helptext=Label(master,text='Check the Menubar for more options\n Once you enter a conversion type, hit enter to convert\n Created by Mohamed Firas Adil',font=("Helvetica", 7))
    helptext.pack(side=BOTTOM,pady=(0,10))

def endprogram():
    clearscreen()
    try:
        time.sleep(0.5)
    except:
        None
    master.destroy()
    exit()

#defining menubars
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Home", command=initialize,accelerator="Ctrl+H")
master.bind('<Control-h>',(lambda event: initialize()))
master.bind('<Control-H>',(lambda event: initialize()))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=endprogram)
menubar.add_cascade(label="Options", menu=filemenu)
convertmenu = Menu(menubar, tearoff=0)
convertmenu.add_command(label="Mass", command=(lambda : (conversionfunction(conversiontype[0]))))
convertmenu.add_command(label="Length", command=(lambda : (conversionfunction(conversiontype[1]))))
convertmenu.add_command(label="Speed", command=(lambda : (conversionfunction(conversiontype[2]))))
convertmenu.add_command(label="Temperature", command=(lambda : (conversionfunction(conversiontype[3]))))
convertmenu.add_command(label="Currency", command=(lambda : (conversionfunction(conversiontype[4]))))
convertmenu.add_command(label="Date", command=(lambda : (conversionfunction(conversiontype[5]))))
menubar.add_cascade(label="Convert", menu=convertmenu)
master.config(menu=menubar)  

#initialising GUI part of the program
initialize()

#ending loop
master.mainloop()











