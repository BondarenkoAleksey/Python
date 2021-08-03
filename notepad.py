from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Блокнот")
root.resizable(True, True)
root.geometry('400x400+0+0')

main_menu = Menu(root)
root.config(menu=main_menu)

def about_program():
  messagebox.showinfo("Блокнот", "Версия программы - 0.0.0")

def quit_program():
  answer = messagebox.askokcancel("Выход", "Вы действительно решили выйти из этого чудо-блокнота?")
  if answer:
    root.destroy()

def change_theme(theme):
  t['bg'] = theme_colors[theme]['text_bg']
  t['fg'] = theme_colors[theme]['text_fg']
  t['insertbackground'] = theme_colors[theme]['cursor']
  t['selectbackground'] = theme_colors[theme]['select_bg']

def open_file():
  file_path = filedialog.askopenfilename(title = "Выбор файла", filetypes = (("текстовые документы (*.txt)","*.txt"),("Все файлы","*.*")))
  if file_path:
    t.delete('1.0', END)
    t.insert('1.0', open(file_path, encoding='utf-8').read())

def save_file():
  file_path = filedialog.asksaveasfilename(title = "Выбор файла", filetypes = (("текстовые документы (*.txt)","*.txt"),("Все файлы","*.*")))
  f = open(file_path, 'w', encoding='utf-8')
  text = t.get('1.0', END)
  f.write(text)
  f.close()

file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label = "Файл", menu=file_menu)
file_menu.add_command(label = "Открыть", command=open_file)
file_menu.add_command(label = "Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label = "Выход", command=quit_program)

theme_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Разное", menu=theme_menu)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu.add_cascade(label = "Оформление", menu=theme_menu_sub)
theme_menu_sub.add_command(label = "Light Theme", command=lambda: change_theme('light'))
theme_menu_sub.add_command(label = "Dark Theme", command=lambda: change_theme('dark'))
theme_menu.add_command(label = "О программе", command=about_program)



theme_menu_sub = Menu(theme_menu, tearoff=0)

# theme_menu_sub.add_command(label="Онлайн")
# theme_menu_sub.add_command(label="Оффлайн")

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
  "dark" : {
      'text_bg' : '#343D46', 'text_fg' : '#C6DEC1', 'cursor' : '#EDA756', 'select_bg' : '#4E5a65'
  },
  "light" : {
      'text_bg' : '#fff', 'text_fg' : '#000', 'cursor' : '#8000FF', 'select_bg' : '#777'
  }
}

t = Text(f_text, font = "Tahoma 12", bg = theme_colors['dark']['text_bg'], fg = theme_colors['dark']['text_fg'], padx = 10, pady = 10, wrap = WORD, insertbackground = theme_colors['dark']['cursor'], selectbackground = theme_colors['dark']['select_bg'], width=0, spacing3=10)
t.pack(fill=X,expand=1, side=LEFT)


scroll = Scrollbar(f_text,command=t.yview)
scroll.pack(fill=Y,side=LEFT)
t.config(yscrollcommand = scroll.set)


root.mainloop()