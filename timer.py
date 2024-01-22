from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_lable.config(text="Timer")
    tik_lable.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_see = WORK_MIN * 60
    short_see = SHORT_BREAK_MIN *60
    long_see = LONG_BREAK_MIN*60

    
    if(reps %8 ==0):
        count_down(long_see)
        timer_lable.config(text="Long Break",fg=RED)
    elif(reps %2==0):
        count_down(short_see)
        timer_lable.config(text="Short Break",fg=PINK)
    else:
        count_down(work_see)
        timer_lable.config(text="Get Back to work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_see = count % 60
    if count_see < 10:
        count_see =f"0{count_see}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_see}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        tik_lable.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Promodoro Task Timer")
window.config(padx=100,pady=50,bg=YELLOW)


timer_lable = Label(text="Timer",bg=YELLOW, font=(FONT_NAME,35,"bold"))
timer_lable.grid(column=1,row=0)

canvas = Canvas(width=200,height=300,bg=YELLOW,highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image =tomato_img)

timer_text = canvas.create_text(100,125,fill="white",text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",command=start_timer,highlightthickness=0,bg=YELLOW,font=(FONT_NAME,25,"bold"))
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",command=reset_timer,highlightthickness=0,bg=YELLOW,font=(FONT_NAME,25,"bold" ))
reset_button.grid(column=2,row=2)

tik_lable = Label(bg=YELLOW,font=(FONT_NAME,25,"bold"))
tik_lable.grid(column=1,row=3)





window.mainloop()