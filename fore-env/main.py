from tkinter import *
import requests
from bs4 import BeautifulSoup


##
def pageget():
    #Retrieves a requests.Response object and stores it in page variable
    url = "https://www.centralbank.go.ke/forex/"
    page = requests.get(url)
    return page



def resultget():
    #Get DOM info from page and filter by "td" class and class name, first 6 lines only
    soup = BeautifulSoup(pageget().content, "html.parser")
    results = soup.find_all("td", class_="tg-4eph")
    list_of_currencies = []
    for elem_ent in results[:6]:
        list_of_currencies.append(elem_ent.text)
    return list_of_currencies


#create individual lists then a dictionary
currency = resultget()[:6:2]
value = resultget()[1:6:2]
list_of_currency = dict(zip(currency, value))



def get_value(curr_name):
    #function to map currency key to corresponding values
    return list_of_currency[curr_name]
##


def populate():
    #push figures to entry upon button press
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
upd_btn = Button(app, text='Fetch', width=12, command=populate)
upd_btn.grid(row=3, column=0, rowspan=2)

app.title('FOREX Scraper')
app.geometry('300x300')

app.mainloop()