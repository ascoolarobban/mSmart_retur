import os
from tkinter.messagebox import showinfo

from fillpdf import fillpdfs
from datetime import date
import tkinter as tk
from tkinter import ttk
import requests
import subprocess

#GET THE PDF
url = 'https://drive.google.com/u/0/uc?id=14R-5nL4oBKGjJT0WzmPziOyYW1iWDzUF&export=download'
pdf_path = "mSmart_util.pdf"
#
r = requests.get(url, allow_redirects=True)
with open(pdf_path, 'wb') as f:
    f.write(r.content)


# print(fillpdfs.get_form_fields(pdf_path))



#Dict form to fill out the pdf
data_dict = {'location': "",
             'receiver': "",
             "date": "",
             'company': "",
             'name': "",
             'phone': "",
             'email': "",
             'number': "",
             'product': "",
             'serial': "",
             'return': "",
             'buy': "",
             'fmi': "",
             'condition': "",
             'app': "",
             'charger': "",
             'closed': "",
             }


# root window
root = tk.Tk()
root.geometry("300x650")
root.resizable(False, False)
root.title('mSmart Retur')

#variables:
today = date.today()
location = tk.StringVar()
receiver = tk.StringVar()
username = tk.StringVar()
company = tk.StringVar()
phone = tk.StringVar()
email = tk.StringVar()
number = tk.StringVar()
product = tk.StringVar()
serial = tk.StringVar()
returned = tk.StringVar()
fmi = tk.StringVar()
buy = tk.StringVar()
damage = tk.StringVar()
app = tk.StringVar()
charger = tk.StringVar()
filemaker = tk.StringVar()

def setData():
    global data_dict
    data_dict['location'] = location.get()
    data_dict['receiver'] = receiver.get()
    data_dict['date'] = today
    data_dict['company'] = company.get()
    data_dict['name'] = username.get()
    data_dict['phone'] = phone.get()
    data_dict['email'] =email.get()
    data_dict['number'] = number.get()
    data_dict['product'] = product.get()
    data_dict['serial'] = serial.get()
    data_dict['return'] = returned.get()
    data_dict['buy'] = buy.get()
    data_dict['fmi'] = fmi.get()
    data_dict['damage'] = damage.get()
    data_dict['app'] = app.get()
    data_dict['charger'] = charger.get()
    data_dict['filemaker'] = filemaker.get()
    return


### BUTTON ACTION ###

def save_clicked():
    global company
    setData()


    try:
        temp_fileName = 'mSmart_retur_{}_{}.pdf'.format(company.get(), today)
        #temp_fileName = "mSmart_final.pdf"
        fillpdfs.write_fillable_pdf(pdf_path, f'{temp_fileName}', data_dict)
        subprocess.call(('open', temp_fileName))
        clear()
    except Exception as e:
        import traceback as tb
        msg = tb.format_exc()
        showinfo(title='Robban är ett jävla geni',
            message= msg)#str(e)
    finally:
        return



# Form frame
msmart_return = ttk.Frame(root)
msmart_return.pack(padx=15, pady=15, fill='x', expand=True)
#------------#

##CLEAR ENTRY ##
def clear():
    receiver.set("")
    company.set("")
    username.set("")
    phone.set("")
    email.set("")
    number.set("")
    product.set("")
    #
    # ###checkbocxes##
    returned.set("")
    buy.set("")
    fmi.set("")
    damage.set("")
    app.set("")
    charger.set("")
    filemaker.set("")

####FORMS####

#location
location_label = ttk.Label(msmart_return, text="Inlämningsställe:")
location_label.pack(fill='x', expand=True)

location_entry = ttk.Entry(msmart_return, textvariable=location)
location_entry.pack(fill='x', expand=True)
location_entry.focus()

# receiver
receiver_label = ttk.Label(msmart_return, text="Mottaget av:")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=receiver)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()

#company
receiver_label = ttk.Label(msmart_return, text="Företag:")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=company)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()

# username
receiver_label = ttk.Label(msmart_return, text="För & Efternamn Kund:")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=username)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()

# phone
receiver_label = ttk.Label(msmart_return, text="Telefon:")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=phone)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()

#email
receiver_label = ttk.Label(msmart_return, text="E-post: ")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=email)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()

#number
receiver_label = ttk.Label(msmart_return, text="Affärsnummer:")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=number)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()

#product
receiver_label = ttk.Label(msmart_return, text="Produkt:")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=product)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()

#serial
receiver_label = ttk.Label(msmart_return, text="Serienummer: ")
receiver_label.pack(fill='x', expand=True)

receiver_entry = ttk.Entry(msmart_return, textvariable=serial)
receiver_entry.pack(fill='x', expand=True)
receiver_entry.focus()






#Checkbutton
#Return?
return_check = ttk.Checkbutton(msmart_return, text="Återlämnas",
                           onvalue = "X",
                           offvalue = " ",
                           variable = returned)
return_check.pack(fill='x',expand=True)

#buy
buy_check = ttk.Checkbutton(msmart_return, text="Köpas ut",
                           onvalue = "X",
                           offvalue = " ",
                           variable = buy)
buy_check.pack(fill='x',expand=True)

#FMI
fmi_check = ttk.Checkbutton(msmart_return, text="Find my iphone avaktiverat",
                           onvalue = "X",
                           offvalue = " ",
                           variable = fmi)
fmi_check.pack(fill='x',expand=True)

# Damaged?
damage_check = ttk.Checkbutton(msmart_return, text="Enheten i normalt bruksskick",
                           onvalue = "X",
                           offvalue = " ",
                           variable = damage)
damage_check.pack(fill='x',expand=True)

# App+
app_check = ttk.Checkbutton(msmart_return, text="Enheten täcks av Apple Care +",
                           onvalue = "X",
                           offvalue = " ",
                           variable = app)
app_check.pack(fill='x',expand=True)

# Chargers?
charger_check = ttk.Checkbutton(msmart_return, text="Laddare medföljer",
                           onvalue = "X",
                           offvalue = " ",
                           variable = charger)
charger_check.pack(fill='x',expand=True)


# Filemaker?
filemaker_check = ttk.Checkbutton(msmart_return, text="Affär avslutad i filemaker",
                           onvalue = "X",
                           offvalue = " ",
                           variable = filemaker)
filemaker_check.pack(fill='x',expand=True)







#####################################################
#Save button
save_button = ttk.Button(msmart_return, text="Klar", command=save_clicked)
save_button.pack(fill='x', expand=True, pady=10)




root.mainloop()









#
#

#
# # If you want it flattened:
# fillpdfs.flatten_pdf('new.pdf', 'newflat.pdf')