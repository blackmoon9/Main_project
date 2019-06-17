import re
import numpy as np
from tkinter import filedialog # 文件路径对话框
from tkinter import *
import codecs
import matplotlib.pyplot as plt
from pylab import mpl
from PIL import Image, ImageTk
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


class Window(Frame):
 
    def __init__(self, master= None):
 
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
        
    def init_window(self):
    
        
        
        
        
        self.dirPath = StringVar()
        self.dirPath.set("选择txt文件或粘贴地址到此处")

        #Entry(root, width=50,image = img_gif, textvariable=self.dirPath).pack(side=LEFT)
        self.master.title("TXT词频统计器")
        #Button(root ,text="选择TXT文件",compound='center', command=self.openDir).pack(pady=(10,0))
        #Button(root, text="开始统计", command=self.counter_count).pack()
        
        
        entry=Entry(root, width=150, relief='flat',bg='#e8e8e8',bd='0',font=('NSimSun',12),textvariable=self.dirPath)

        bt1=Button(root ,image=bt1Img,relief='flat',compound='center',command=self.openDir)
        bt1.pack()
        bt2=Button(root ,image=bt2Img,relief='flat',compound='center',command=self.counter_count)
        bt2.pack()
        canvas.create_image(300,40, image=entryImg)
        canvas.create_window(285, 40, width=480, height=30,window=entry)
        canvas.create_window(600, 40, width=44, height=44,window=bt1)
        canvas.create_window(325, 150, width=250, height=44,window=bt2)
        
    def openDir(self):
        # 选择要打开的文件夹路径
        self.dirPath.set(filedialog.askopenfilename())
    
    def counter_count(self):
        word = []
        counter = {}
        filename=self.dirPath.get()
        with open(filename) as f:
        #读取文件中的字符串
            txt = f.read()
        #去除字符串中的标点、数字等
            txt = re.sub('[,\.()":;!@#$%^&*\d]|\'s|\'', '', txt)
        #替换换行符，大小写转换，拆分成单词列表
            word_list = txt.replace('\n',' ').replace('  ',' ').lower().split(' ')
            word_count_dict = {}

            for word in word_list:
          #统计字典中的词频
                if word in word_count_dict.keys():
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] =1

        word_count_dict= sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)

        #print(word_count_dict[:100])

        label = list(map(lambda x: x[0], word_count_dict[:20]))
        value = list(map(lambda y: y[1], word_count_dict[:20]))
        plt.bar(range(len(value)), value, tick_label=label)
        plt.savefig("test.png")
        
        root2= Toplevel()
        root2.geometry("800x500")

        
        
        labeltitle=Label(root2,text="     结果显示：本文词频最多的20个单词的条形统计图及本文的所有单词及出现次数",
                         font=('Microsoft YaHei',12 ,'bold' ),height=2,fg='red',anchor=W,width=100).pack()
        picture = PhotoImage(file = 'test.png')
        label2 = Label(root2, image=picture)
        label2.pack(side='left')
        listbox = Listbox(root2)
        scr=Scrollbar(root2)

        listbox.config(yscrollcommand=scr.set)
        scr.config(command=listbox.yview)
        for i in word_count_dict:
            listbox.insert(END,str(i))
                    
        listbox.pack(side='left',fill=Y)
        scr.pack(side='left',fill=Y)
        
       
        
        mainloop()
        


root = Tk()
#root.geometry("500x300")#默认窗口尺寸
titleImg=PhotoImage(file = 'title.gif')
labeltitle111=Label(root,image=titleImg).pack(pady=30)
canvas = Canvas(root, width=650,height=250,bd=0, highlightthickness=0)
entryImg=PhotoImage(file = 'enter.gif')
canvas.create_image(300,40, image=entryImg)
canvas.pack()
bt1Img=PhotoImage(file = 'bt1.gif')
bt2Img=PhotoImage(file = 'bt2.gif')
app = Window(root)
root.mainloop()

