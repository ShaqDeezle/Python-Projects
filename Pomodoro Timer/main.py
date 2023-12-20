from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .10
SHORT_BREAK_MIN = .10
LONG_BREAK_MIN = .25
reps = 0
checks = []
# checks = "✔"
timer = None



# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global checks
  global reps
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text = "00:00")
  my_label.config(text = "Timer", fg = GREEN)
  checks.clear()
  checkmarks.config(text = checks)
  reps = 0
  
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  global checks
  reps += 1
  
  work_sec = (WORK_MIN * 60)
  short_break_sec = (SHORT_BREAK_MIN * 60)
  long_break_sec = (LONG_BREAK_MIN * 60)

  if (reps % 2 != 0):
    button_clicked(work_sec)
    my_label.config(text = "Work Time", fg = GREEN)
  
  elif (reps % 2 == 0) and not(reps % 8 == 0):
    button_clicked(short_break_sec)
    my_label.config(text = "Break Time", fg = PINK)
  
  elif (reps % 8 == 0):
    button_clicked(long_break_sec)
    my_label.config(text = "Just Chill", fg = RED)
    
    checks.append("✔")
    checkmarks.config(text = checks)
    # checks += "✔"

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def button_clicked(number: int):

  minutes = (number / 60)

  count_min = math.floor(minutes)

  count_sec = (number % 60)
  
  if (count_sec < 10):
    count_sec = f"0{count_sec}"
  
  canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")

  if (number > -1):
    global timer
    timer = window.after(1000, button_clicked, number - 1)
  elif (number < 0):
    start_timer()
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Pomodoro Timer")

window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 250, height = 250, bg = YELLOW, highlightthickness = 0)

tomato_img = PhotoImage(file = "tomato.png")

canvas.create_image(125, 125, image = tomato_img)
canvas.grid(row = 1, column = 1)

timer_text = canvas.create_text(125, 145, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

my_label = Label(text = "Timer", fg = GREEN, font = (FONT_NAME, 40), bg = YELLOW)
my_label.grid(row = 0, column = 1)

button_1 = Button(text = "Start", command = start_timer, highlightthickness = 0)
button_1.grid(row = 2, column = 0)

button_2 = Button(text = "Reset", command = reset_timer, highlightthickness = 0)
button_2.grid(row = 2, column = 2)

checkmarks = Label(fg = GREEN, font = (FONT_NAME, 20), bg = YELLOW)
checkmarks.grid(row = 3, column = 1) 

window.mainloop()
