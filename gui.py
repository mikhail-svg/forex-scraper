from tkinter import *
from tkinter import messagebox
from funcs import get_value


def populate():
    try:
        currenc = []
        currenc.append(get_value("US DOLLAR"))
        currenc.append(get_value("EURO"))
        currenc.append(get_value("STG POUND"))
        usd_entry.insert(END, currenc[0])
        euro_entry.insert(END, currenc[1])
        stg_pound_entry.insert(END, currenc[2])
    except IndexError:
        pass    

app = Tk()

#Text Fields
usd_text = StringVar()
usd_label = Label(app, text='USD: ', font=('bold',12), pady=15, padx=15)
usd_label.grid(row=0, column=0, sticky=W)
usd_entry = Entry(app, textvariable=usd_text)
usd_entry.grid(row=0, column=1)

euro_text = StringVar()
euro_label = Label(app, text='EURO: ', font=('bold',12), pady=15, padx=15)
euro_label.grid(row=1, column=0, sticky=W)
euro_entry = Entry(app, textvariable=euro_text)
euro_entry.grid(row=1, column=1)

stg_pound_text = StringVar()
stg_pound_label = Label(app, text='STG POUND: ', font=('bold',12), pady=15, padx=15)
stg_pound_label.grid(row=2, column=0, sticky=W)
stg_pound_entry = Entry(app, textvariable=stg_pound_text)
stg_pound_entry.grid(row=2, column=1)

#Button
upd_btn = Button(app, text='Update', width=12, command=populate)
upd_btn.grid(row=3, column=0, rowspan=2)

app.title('FOREX Scraper')
app.geometry('300x300')

app.mainloop()

