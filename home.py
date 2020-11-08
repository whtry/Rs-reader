# -*-coding:utf-8-*-

from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox as tkms
import tkinter.filedialog
import language

# ---------参数-----------
# 语言
lan = 'Chinese'
language.Chinese()

# 显示
font_size = 10
everypagewords = 1000
fenhang = 40
bgc = "lightyellow"

# ================================================
#                        以下是界面，功能
# ================================================

# -------- 阅读 read 界面 ----------


def cutwords():  # 分页
    f = open(fr, 'r', encoding='utf-8')
    f = f.readlines()
    fs = []
    for i in f:
        fs.append(''.join(i.split()))

    f = ''.join(fs)
    fl = []
    every_st = []
    screen_things = []
    n = 0
    for i in f:
        n += 1
        fl.append(i)
        if n >= fenhang:
            fl.append('\n')
            n = 0

    num = 0  # 分页计时器
    for i in fl:
        screen_things.append(i)
        num += 1
        if num >= everypagewords:
            every_st.append(''.join(screen_things))
            screen_things = []
            num = 0

    return every_st

# 样式1 read_page1


def lastpage():  # 上一页
    global esw, page, est
    if page == 0:
        tkms.showerror(language.error, language.error3)
    else:
        page -= 1
        esw = est[page]
        sc['text'] = esw
        pagenum['text'] = '{}/{}'.format(page + 1, len(est))


def nextpage():  # 下一页
    global esw, page, est
    if page == len(est)-1:
        tkms.showerror(language.error, language.error4)
    else:
        page += 1
        esw = est[page]
        sc['text'] = esw
        pagenum['text'] = '{}/{}'.format(page + 1, len(est))

# 界面


def read_page1():
    global page, esw, est, sc, pagenum
    page = 0

    est = cutwords()
    read_page1 = Tk()
    read_page1.geometry('{}x{}'.format(
        everypagewords//fenhang*2*font_size+90, fenhang*font_size+140))
    read_page1.title('{}-{}'.format(language.software_name, fr))
    read_page1.configure(background=bgc)

    # 背景，有些不兼容
    # img = Image.open('icon/rpbg.gif')
    # home_img = ImageTk.PhotoImage(img)
    # rp_img = Label(read_page1, image=home_img)
    # rp_img.image = home_img
    # rp_img.place(x=-2, y=-2)

    esw = est[page]
    # 显示内容
    sc = Label(read_page1, text=esw, font=(fon, font_size), bg=bgc)
    sc.pack(side='top')
    # 底栏
    Button(read_page1, text=language.last_page, bg=bgc, width=10,
           command=lastpage).pack(side='left')
    Button(read_page1, text=language.next_page, bg=bgc, width=10,
           command=nextpage).pack(side='right')
    pagenum = Label(
        read_page1, text='1/{}'.format(len(est)), bg=bgc, font=(fon, 10))
    pagenum.pack(side='bottom')
    # Button(read_page1,text=language.lists).pack(side='button')


# 读取文件
def read_file():
    global fr
    fr = tkinter.filedialog.askopenfilename()
    if fr == '':
        tkms.showerror(language.error, language.error2)
    else:
        home.destroy()
        read_page1()

# -------- 设置 setting 界面 --------


def sets():
    global lan
    if lan == 'Chinese':
        setting = Tk()
        setting.geometry('320x300')
        setting.title(language.setting)
        Label(setting, text='显示：', font=('微软雅黑', 15)).grid(row=0, column=0)

        # 每页显示的字数
        def getwnE():
            global everypagewords
            wg = wnE.get()
            if wg == '':
                tkms.showerror(language.error, language.error2)
            else:
                everypagewords = int(wg)

        Label(setting, text='每页显示的字数：').grid(row=1, column=0)
        wnE = Entry(setting)
        wnE.grid(row=1, column=1)
        Button(setting, text='确定', command=getwnE).grid(row=1, column=2)

        # 每行显示的字数
        def getfhE():
            global fenhang
            fg = fhE.get()
            if fg == '':
                tkms.showerror(language.error, language.error2)
            else:
                fenhang = int(fg)

        Label(setting, text='每行显示的字数：').grid(row=2, column=0)
        fhE = Entry(setting)
        fhE.grid(row=2, column=1)
        Button(setting, text='确定', command=getfhE).grid(row=2, column=2)

        # 字样
        Label(setting, text='字样：', font=('微软雅黑', 15)).grid(row=3, column=0)

        # 字体
        def wryh():
            global fon
            f = open('fonts.txt', 'w')
            f.write('微软雅黑')
            f.close()
            fon = '微软雅黑'

        def st():
            global fon
            f = open('fonts.txt', 'w')
            f.write('宋体')
            f.close()
            fon = '宋体'

        Label(setting, text='字体选择：').grid(row=4, column=0)
        Button(setting, text='微软雅黑', command=wryh).grid(row=4, column=1)
        Button(setting, text='—宋体—', command=st).grid(row=4, column=2)

        # 字体大小
        def cfz():
            global font_size
            fz = fzE.get()
            if fz == '':
                tkms.showerror(language.error, language.error2)
            else:
                font_size = int(fz)

        Label(setting, text='字体大小：').grid(row=5, column=0)
        fzE = Entry(setting)
        fzE.grid(row=5, column=1)
        Button(setting, text='确定', command=cfz).grid(row=5, column=2)

        Label(setting, text='每行字数默认：40', font=(fon, 9)).grid(row=6, column=1)
        Label(setting, text='每页字数默认：1000', font=(fon, 9)).grid(row=7, column=1)
        Label(setting, text='字体默认：微软雅黑', font=(fon, 9)).grid(row=8, column=1)
        Label(setting, text='字体大小默认：10', font=(fon, 9)).grid(row=9, column=1)

    else:
        tkms.showwarning(language.error, language.error5)

# -------- 首页 home 界面 --------


def home_page():
    global home, fon, roads
    home = Tk()
    # 字体
    try:
        f = open('fonts.txt', 'r')
        fon = f.read()
        f.close()
    except:
        fon = '微软雅黑'
        f = open('fonts.txt', 'w')
        f.write(fon)
        f.close()
        tkms.showerror(language.error, language.error1+fon+language.sen_end)
        home.destroy()

    home.title(language.home)
    home.geometry('520x292')
    home.resizable(0, 0)

    menubar = Menu(home)
    menu_lan = Menu(menubar, tearoff=0)
    # 设置
    menubar.add_command(label=language.setting, command=sets)

    # 语言
    menubar.add_cascade(label=language.language, menu=menu_lan)
    menu_lan.add_command(label='中文', command=Chinese)
    #menu_lan.add_command(label='English', command=English)

    home.config(menu=menubar)

    img = Image.open('icon/bg.gif')
    home_img = ImageTk.PhotoImage(img)
    label_img = Label(home, image=home_img)
    label_img.image = home_img
    label_img.place(x=-2, y=-2)

    Label(home, text=language.home_welcome, font=(fon, 10),bg='white').pack(side='bottom')
    Button(home, text=language.home_go, width=24, font=(
        fon, 15), bg='white',command=read_file).pack(side='bottom')


def Chinese():  # 语言cn
    global lan
    lan = 'Chinese'
    language.Chinese()
    home.destroy()
    home_page()


def English():  # 语言en
    global lan
    lan = 'English'
    language.English()
    home.destroy()
    home_page()


home_page()

mainloop()
