import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pyautogui
import pygetwindow

class normal_btn(tk.Button):
  def __init__(self, master = None, cnf = None, *, activebackground = None, activeforeground = None, anchor = "center", background = None, bd = None, bg = None, bitmap = "", borderwidth = None, command = "", compound = "none", cursor = "", default = "disabled", disabledforeground = None, fg = None, font = "TkDefaultFont", foreground = None, height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 1, image = "", justify = "center", name = None, overrelief = "", padx = None, pady = None, relief = None, repeatdelay = None, repeatinterval = None, state = "normal", takefocus = "", text = "", textvariable = None, underline = -1, width = 0, wraplength = 0):
    super().__init__(master, cnf, activebackground=activebackground, activeforeground=activeforeground, anchor=anchor, background="PeachPuff2", bd=bd, bg=bg, bitmap=bitmap, border=0, borderwidth=borderwidth, command=command, compound=compound, cursor=cursor, default=default, disabledforeground=disabledforeground, fg=fg, font=font, foreground=foreground, height=3, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, image=image, justify=justify, name=name, overrelief=overrelief, padx=padx, pady=pady, relief=relief, repeatdelay=repeatdelay, repeatinterval=repeatinterval, state=state, takefocus=takefocus, text=text, textvariable=textvariable, underline=underline, width=15, wraplength=wraplength)

class normal_lbl(tk.Label):
  def __init__(self, master = None, cnf = None, *, activebackground = None, activeforeground = None, anchor = "center", background = None, bd = None, bitmap = "", border = None, borderwidth = None, compound = "none", cursor = "", disabledforeground = None, fg = None, font = "TkDefaultFont", height = 0, highlightbackground = None, highlightcolor = None, highlightthickness = 0, image = "", justify = "center", name = None, padx = 1, pady = 1, relief = "flat", state = "normal", takefocus = 0, text = "", textvariable = None, underline = -1, width = 0, wraplength = 0):
    super().__init__(master, cnf, activebackground=activebackground, activeforeground=activeforeground, anchor=anchor, background="PeachPuff2", bd=bd, bitmap=bitmap, border=border, borderwidth=borderwidth, compound=compound, cursor=cursor, disabledforeground=disabledforeground, fg=fg, font=font, height=1, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, image=image, justify=justify, name=name, padx=padx, pady=pady, relief=relief, state=state, takefocus=takefocus, text=text, textvariable=textvariable, underline=underline, width=55, wraplength=wraplength)

normal_font = ()



class app(tk.Tk):
  def __init__(self, master=None, *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self.title("to-do List")
    self.state("zoomed")
    self.frame = main_frame(self, width=1920, height=1050, bg="grey12").pack()

class main_frame(tk.Frame):
  def __init__(self, master = None, *args, **kwargs):
    super().__init__(master, *args, **kwargs)
    self.master = master
    self.tasks = {"task1": {"name":"the name",
                  "time": "11:11"},
                  "task2": {"name":"the name",
                  "time": "11:11"}}
    self.canvas = tk.Canvas(self, width=1200, height=600, bg="PeachPuff2")
    self.canvas.place(x=300, y=100)
    self.v = tk.Scrollbar(self, width=30, orient="vertical", command=self.canvas.yview)
    self.v.place(x=1500, y=100, height=600)
    self.frame = tk.Frame(self.canvas, bg="PeachPuff2", width=1200, height=600)
    self.frame.pack(expand=True)
    self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
    self.type_label = normal_lbl(self.frame, text="task", borderwidth=3, relief="raised")
    self.type_label.grid(column=0, row=0)
    
    self.date_label = normal_lbl(self.frame, text="date", borderwidth=3, relief="raised")
    self.date_label.grid(column=1, row=0)
    
    self.task_count = 1
    self.row_count = 1
    for i in self.tasks:
      n = normal_lbl(self.frame, text=f"{self.tasks[f"task{self.task_count}"]["name"]}"
              )
      n.grid(column=0, row=self.row_count)
      n.bind()
      p = normal_lbl(self.frame, text=f"{self.tasks[f"task{self.task_count}"]["time"]}"
              )
      p.grid(column=1, row=self.row_count)
      self.row_count += 1
      self.task_count += 1
    
    self.save_btn = normal_btn(self, text="save", command=self.save_command)
    self.save_btn.place(x=400, y=800)
    
    self.add_task_btn = normal_btn(self, text="Add Task", command=self.add_task)
    self.add_task_btn.place(x=1200, y=800)
    
  def add_task(self):
    if not hasattr(self, "entry1"):
      self.entry1 = tk.Entry(self.frame, bg="lightblue", width=55)
      self.entry1.grid(column=0, row=self.row_count)
    if not hasattr(self, "entry2"):
      self.entry2 = tk.Entry(self.frame, bg="lightblue", width=55)
      self.entry2.grid(column=1, row=self.row_count)
    if not hasattr(self, "submit_btn"):
      self.submit_btn = normal_btn(text="submit", command=self.submit_btn_command)
      self.submit_btn.place(x=600, y=800)

  def submit_btn_command(self):
    self.tasks.__setitem__(f"task{self.task_count}", dict([["name", f"{self.entry1.get()}"],
                                                      ["time", f"{self.entry2.get()}"]]))
    lbl1 = tk.Label(self.frame, bg="PeachPuff2", width=55, height=1, text=self.entry1.get())
    lbl2 = tk.Label(self.frame, bg="PeachPuff2", width=55, height=1, text=self.entry2.get())
    if hasattr(self, "entry1"):
      self.entry1.destroy()
      self.__delattr__("entry1")
    if hasattr(self, "entry2"):
      self.entry2.destroy()
      self.__delattr__("entry2")
    if hasattr(self, "submit_btn"):
      self.submit_btn.destroy()
      self.__delattr__("submit_btn")
    lbl1.grid(column=0, row=self.row_count)
    lbl2.grid(column=1, row=self.row_count)
    self.row_count += 1
  def save_command(self):
    file = filedialog.asksaveasfile()

def hotreload(app):
  myapp.quit()
  window = pygetwindow.getWindowsWithTitle("Command Prompt")[0]
  if window:
    window.activate()
    pyautogui.typewrite("py to-do_list.py")
    pyautogui.press("enter")
    window = pygetwindow.getWindowsWithTitle("to-do List")[0]
    window.activate()
  else:
    print("error with the window")

if __name__ == "__main__":
  myapp = app()
  myapp.bind("q", quit)
  myapp.bind("u", hotreload)
  myapp.mainloop()
