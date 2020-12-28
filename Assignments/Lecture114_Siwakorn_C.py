from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from forex_python.bitcoin import BtcConverter

c = CurrencyRates()
n = CurrencyCodes()
b = BtcConverter()

def currency_calculate(event):
    rate = c.get_rate(currency_box2.get(),currency_box1.get())
    result = format(float(money_box.get())/rate,".2f")
    result_label.config(text="แลกได้" + str(result)+n.get_symbol(currency_box2.get()))

def btc_save(event):
    def btc_calculate(event):
        buy_with_currency1 = b.convert_to_btc(float(money_box.get()), currency_box1.get())
        buy_with_currency2 = b.convert_to_btc(float(float(money_box.get()) / c.get_rate(currency_box2.get(), currency_box1.get())), currency_box2.get())

        if btc_combo.get() == currency_box1.get():
            if buy_with_currency1 >= buy_with_currency2:
                btc_result_label.config(text="ซื้อได้จำนวน "+str(buy_with_currency1)+" BTC")
                advice_label.config(text="ซื้อด้วยสกุล "+ currency_box1.get() +" มีความคุ้มค่ามากที่สุด")
            else:
                different = buy_with_currency2 - buy_with_currency1
                btc_result_label.config(text="ซื้อได้จำนวน "+str(buy_with_currency1)+" BTC")
                advice_label.config(text="ซื้อด้วยสกุล "+ currency_box2.get() +" คุ้มกว่าแตกต่างกันอยู่ " + str(different) + " BTC")
        elif btc_combo.get() == currency_box2.get():
            if buy_with_currency2 >= buy_with_currency1:
                btc_result_label.config(text="ซื้อได้จำนวน " + str(buy_with_currency2) + " BTC")
                advice_label.config(text="ซื้อด้วยสกุล " + currency_box2.get() + " มีความคุ้มค่ามากที่สุด")
            else:
                different = buy_with_currency1 - buy_with_currency2
                btc_result_label.config(text="ซื้อได้จำนวน " + str(buy_with_currency1) + " BTC")
                advice_label.config(text="ซื้อด้วยสกุล " + currency_box1.get() + " คุ้มกว่าแตกต่างกันอยู่ " + str(different) + " BTC")

    btc_combo = ttk.Combobox(main_window, values=[currency_box1.get(), currency_box2.get()])
    btc_combo.grid(row=6, column=1)

    btc_button = Button(main_window, text="==>")
    btc_button.bind('<Button-1>', btc_calculate)
    btc_button.grid(row=6, column=2)


#Main
main_window = Tk()
main_window.title("Exchange")

exchange_title_lable = Label(main_window, text="Exchange", font=("Leelawadee",36), bg="#fdd678", fg="black")
exchange_title_lable.grid(row=0, column=0)

currency_lable1 = Label(main_window, text="Your currency ::", font=("Leelawadee",18))
currency_lable1.grid(row=1, column=0)

currency_box1 = Entry(main_window)
currency_box1.grid(row=1, column=1)

money_lable = Label(main_window, text="  Amount ::", font=("Leelawadee",18))
money_lable.grid(row=1, column=2)

money_box = Entry(main_window)
money_box.grid(row=1, column=3)

currency_lable2 = Label(main_window, text="Currency change :: ", font=("Leelawadee",18))
currency_lable2.grid(row=2, column=0)

currency_box2 = Entry(main_window)
currency_box2.grid(row=2, column=1)

currency_button = Button(main_window, text="==>")
currency_button.bind('<Button-1>',currency_calculate)
currency_button.grid(row=2, column=2)

result_label = Label(main_window, text="จำนวนเงินที่ได้ ???", font=("Leelawadee",12))
result_label.grid(row=2, column=3)

save_change_lable = Label(main_window, text="Save to change to Bitcoin", font=("Leelawadee", 18))
save_change_lable.grid(row=3, column=1)

save_change_button = Button(main_window, text="SAVE !!!")
save_change_button.bind('<Button-1>', btc_save)
save_change_button.grid(row=4, column=1)

btc_title_lable = Label(main_window, text="Currency to Bitcoin", font=("Leelawadee", 36), bg="#fdd678", fg="black")
btc_title_lable.grid(row=5, column=0)

btc_lable1 = Label(main_window, text="Your currency ::", font=("Leelawadee", 18))
btc_lable1.grid(row=6, column=0)

btc_combo = ttk.Combobox(main_window, values=[currency_box1.get(), currency_box2.get()])
btc_combo.grid(row=6, column=1)

btc_button = Button(main_window, text="==>")
btc_button.grid(row=6, column=2)

btc_result_label = Label(main_window, text="จำนวน Bitcoin ???", font=("Leelawadee", 12))
btc_result_label.grid(row=6, column=3)

advice_label = Label(main_window, text="***ประเมิณความคุ้มค่า***", font=("Leelawadee", 12))
advice_label.grid(row=7, column=3)

main_window.mainloop()

#Program Concept : เป็นโปรเเกรมที่ช่วยในการคำนวณเพื่อหาว่าจะใช้สกุลเงินใดคุ้มกว่ากันในการซื้อ Bitcoin เพื่อให้ได้จำนวน Bitcoin ที่มากกว่า