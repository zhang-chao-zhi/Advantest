from tkinter import *

def display():
    # 在按钮被点击时，获取文本框的内容并打印到控制台
    print(entry.get())

# 创建一个新的窗口
root = Tk()

# 创建一个文本框，用于用户输入内容
entry = Entry(root)
entry.pack()

# 创建一个按钮，当这个按钮被点击时，会调用display函数
button = Button(root, text="显示", command=display)
button.pack()

# 开始事件循环
root.mainloop()
