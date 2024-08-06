import tkinter as tk

def setup_display():
    # 在按钮被点击时，获取文本框的内容并打印到控制台

    print("Input file load complete!")
    
    
# def txt_display():
#     # 在按钮被点击时，获取文本框的内容并打印到控制台
#     print(txt_button.get()+"加载完成！")

# 创建一个新的窗口
UI = tk.Tk()  
UI.minsize(500,350)     # 设置窗口的最小尺寸
UI.maxsize(500,500)     # 设置窗口的最大尺寸
UI.title("通过I2C协议生成SMT8 pattern软件")     # 设置窗口的标题
UI.geometry("+370+150")     # 设置窗口的位置


# 创建一个文本框，用于用户输入setup内容
input_file = tk.Entry(UI) 
input_file.place(x=50,y=50)


# 创建一个按钮，当这个按钮被点击时，会调用display函数
setup_button = tk.Button(UI, text="请输入配置文件名", command=setup_display)
setup_button.place(x=70,y=100)


#创建一个文本框，用于用户输入txt文件内容
txt_file = tk.Entry(UI)
txt_file.place(x=270,y=50)

# 创建一个按钮，当这个按钮被点击时，会调用display函数
txt_button = tk.Button(UI, text="请输入pattern文件名", command=txt_display)
txt_button.place(x=280,y=100)



# 开始事件循环
UI.mainloop()
