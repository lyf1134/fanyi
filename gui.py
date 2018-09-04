from trans import *

import tkinter as tk
import win32api
from trans import __translate

def about():
	win32api.ShellExecute(0, 'open', 'notepad.exe', 'about.md', '', 1)
def shuoming():
	win32api.ShellExecute(0, 'open', 'notepad.exe', 'shuoming.txt', '', 1)
def trans():
	#t=time.time()
	result.delete(0.0,'end')
	var = text.get(1.0,'end-1c')
	lin = l1.get()#文字
	lout = l2.get()
	#print(lin,lout)
	var = __translate(lin, lout, v.get(), var)
	result.insert('end',var)
	#print('fanyi')
	#print(str(time.time()-t)+'s')

def fresh():
	global om1,om2
	om1.destroy()
	om2.destroy()
	l1.set('auto')
	l2.set('中文')
	if v.get() == 'Baidu':
		om1 = tk.OptionMenu(app, l1,*(['auto']+list_b1))
		om2 = tk.OptionMenu(app, l2,*list_b1)
	elif v.get() == 'Google':
		om1 = tk.OptionMenu(app, l1,*(['auto']+list_g1))
		om2 = tk.OptionMenu(app, l2,*list_g1)
	else:
		om1 = tk.OptionMenu(app, l1,*(['auto']+list_y1))
		om2 = tk.OptionMenu(app, l2,*(['auto']+list_y1))
	om1.place(x = 270, y = 35)
	om2.place(x = 270, y = 65)

app = tk.Tk()
app.title('翻译')
app.geometry('600x400')
app.resizable(False, False)

menubar = tk.Menu(app)

v = tk.StringVar()
v.set('Baidu')

#新建一个空的菜单,将menubar的menu属性指定为filemenu，即filemenu为menubar的下拉菜单
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_radiobutton(label = 'Baidu', command = fresh, variable = v)
filemenu.add_radiobutton(label = 'Google', command = fresh, variable = v)
filemenu.add_radiobutton(label = 'Youdao', command = fresh, variable = v)
menubar.add_cascade(label = '翻译源', menu = filemenu)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label = '使用说明',command = shuoming)
filemenu.add_command(label = '关于',command = about)
menubar.add_cascade(label='帮助', menu = filemenu)

app['menu']=menubar

label1 = tk.Label(app,text = '请选择翻译语言：')
label1.pack(pady = 5, side = 'top')
label2 = tk.Label(app,text = '从		')
label2.pack(pady = 5, side = 'top')
label3 = tk.Label(app,text = '到		')
label3.pack(pady = 5, side = 'top')

l1 = tk.StringVar(app)
l1.set('auto')
om1 = tk.OptionMenu(app, l1,*(['auto']+list_b1))
om1.place(x = 270, y = 35)
l2 = tk.StringVar(app)
l2.set('中文')
om2 = tk.OptionMenu(app, l2,*list_b1)
om2.place(x = 270, y = 65)

b1 = tk.Button(app, text = 'translate', command = trans,bg = 'red')
b1.pack(padx=10, pady=5)
text = tk.Text(app, height = 10, width = 40)
text.pack(padx=10, pady=5, side='left')
result = tk.Text(app, height = 10, width = 40)
result.pack(padx=10, pady=5, side='left')

tk.Button(app, text='Quit', command = app.quit).place(x = 540, y = 370, width=45, height=30)
#print('加载')
#print(str(time.time()-t)+'s')
app.mainloop()
