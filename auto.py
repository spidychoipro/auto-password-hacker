import random
import time
from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter import StringVar

# 비밀번호 생성
password = str(random.randint(1, 9999)).zfill(4)

# 입력창 생성
root = Tk()
root.title("Hacking Program")

input_var = StringVar()
input_var.set("0000")

def hide_input():
    # 2초 뒤에 입력값을 ●로 변환하는 함수
    input_val = input_var.get()
    input_var.set("●" * len(input_val))

root.after(2000, hide_input)

def show_input():
    # 보이기 버튼 누르면 2초 동안 ●로 가려진 문자열을 복원해 보여줌
    input_val = input_var.get()
    input_var.set(input_val.replace("●", ""))
    root.after(2000, hide_input)

input_box = Entry(root, width=4, font=("Helvetica", 24), justify="center", textvariable=input_var)
input_box.pack(pady=20)

# false 리스트 생성
false_list = []

def check_password():
    global password
    input_val = input_box.get()
    input_val = input_val.replace("●", "")  # "●" 문자열 삭제
    input_val = input_val.zfill(4)  # 비밀번호와 길이를 맞추기 위해 왼쪽에 0 채우기
    
    if input_val == password:
        messagebox.showinfo("Hacking Success", "Hacking Success")
        root.destroy()
    else:
        messagebox.showwarning("Password Incorrect", "Password is Incorrect")
        false_list.append(input_val)
        auto_input(input_val)

def entry_update():
    global false_list
    for i in range(len(input_var.get())):
        if input_var.get()[i] != "●":
            input_box.delete(i, i)
            input_box.insert(i, input_var.get()[i])
    false_list = []

def auto_input(input_val):
    input_val = str(int(input_val) + 1).zfill(4)
    input_box.delete(0, 'end')
    input_box.insert(0, input_val)

    if input_val == password:
        messagebox.showinfo("Hacking Success", "Hacking Success")
        root.destroy()
    elif input_val == "0000":
        check_password()
    else:
        root.after(50, auto_input, input_val)

def start_auto_input(event=None):
    input_val = input_box.get()
    input_val = input_val.replace("●", "")  # "●" 문자열 삭제
    input_val = input_val.zfill(4)  # 비밀번호와 길이를 맞추기 위해 왼쪽에 0 채우기
    
    if input_val == "0000":
        auto_input("0000")  # 0000부터 시도 시작
    else:
        messagebox.showwarning("Start Error", "Please enter 0000 to start auto hacking")

start_button = Button(root, text="Auto Hacking Start", font=("Helvetica", 16), command=start_auto_input)
start_button.pack(pady=10)

root.bind('<Return>', start_auto_input)  # 엔터키로도 시작 가능

root.mainloop()