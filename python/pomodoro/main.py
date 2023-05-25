from tkinter import *
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
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps = 0
    elif (reps % 2) == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    count_mins = count // 60
    count_secs = count % 60
    if (count_secs//10)==0:
        count_secs = "0"+str(count_secs)
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
       global my_timer 
       my_timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 2 ==0:
            mark = ""
            for _ in range(reps//2):
                mark += "✓"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
#window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#image
canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,34,"bold"))
canvas.grid(row=2,column=2)
#timer title
timer_label = Label(text="Timer",font=((FONT_NAME,44,"bold")))
timer_label.grid(row=1,column=2)
timer_label.config(bg=YELLOW,fg=GREEN)
#check mark
check_mark=Label(bg=YELLOW,fg=GREEN)
check_mark.grid(row=4,column=2)
check_mark.config(bg=YELLOW,fg=GREEN)
#start button
start_button = Button(text="Start", bg=YELLOW,highlightthickness=0, command=start_timer,highlightbackground=YELLOW)
start_button.grid(row=3,column=1)
#Reset button
reset_botton = Button(text="Reset", bg=YELLOW,highlightthickness=0, command=reset_timer,highlightbackground=YELLOW)
reset_botton.grid(row=3,column=3)







window.mainloop()