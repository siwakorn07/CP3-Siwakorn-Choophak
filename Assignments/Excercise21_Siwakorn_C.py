from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow((float(textBoxHeight.get())/100),2))
    bmi = float(textBoxWeight.get())/math.pow((float(textBoxHeight.get())/100),2)
    if bmi>30:
        result = "โรคอ้วนอันตราย"
    elif bmi>25:
        result = "โรคอ้วน"
    elif bmi>23:
        result = "น้ำหนักเกิน"
    elif bmi>18.5:
        result = "สมส่วน"
    else:
        result = "น้ำหนักต่ำกว่าเกณฑ์"
    bmi = format(bmi,".2f")
    labelResult.config(text = "คุณอยู่ในภาวะ"+result+" และมีค่า BMI อยู่ที่ "+str(bmi))

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop()