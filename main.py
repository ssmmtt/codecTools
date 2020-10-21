import base64
import hashlib
import json
import time
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

import pyperclip

from tabview import TabView


# 在body中生成widget的函数，返回的widget将被添加到tabview的body中
def create_body():
    global body

    toolframe = Frame(body)
    toolframe.pack(fill=BOTH, expand=True)
    gui = ToolsGui(toolframe)
    gui.set_init_window()

    return toolframe


# 点击选项卡时的回调
def select(index):
    print("current selected -->", index)


# 删除选项卡时的回调，如果返回False将不会删除
def remove(index):
    print("remove tab -->", index)
    # if messagebox.askokcancel("标题", "确定要关闭该选项卡吗？"):
    return True
    # else:
    #     return False


class ToolsGui():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def md5_upper_event(self, event):
        self.str_trans_to_md5(True)

    def fast_copy(self):
        data = self.result_data_Text.get(0.0, END).strip()
        pyperclip.copy(data)

    # 设置窗口
    def set_init_window(self):
        # 左侧试图
        self.init_window_name.update()
        print(self.init_window_name.winfo_width())
        frm1 = Frame(self.init_window_name)
        frm1.pack(fill=BOTH, side=LEFT, expand=True)

        self.init_data_label = Label(frm1, text="待处理数据", font=("宋体", 15, "bold"), height=2, bg='dodgerblue')
        self.init_data_label.pack(fill=X)

        self.init_data_Text = ScrolledText(frm1, undo=True)  # 原始数据录入框
        self.init_data_Text.pack(fill=BOTH, expand=True)
        self.log_label = Label(frm1, text="日志", font=("宋体", 15, "bold"), height=2, bg='dodgerblue')
        self.log_label.pack(fill=X)
        self.log_data_Text = ScrolledText(frm1, )  # 日志框
        self.log_data_Text.pack(fill=BOTH, expand=True)

        # 中间按钮试图
        frm2 = Frame(self.init_window_name)
        frm2.pack(fill=BOTH, side=LEFT, expand=True)
        # md5计算
        self.str_trans_to_md5_button = Button(frm2, text="MD5计算\n（右键点击大写）", bg="limegreen",
                                              command=self.str_trans_to_md5)
        self.str_trans_to_md5_button.bind('<Button-3>', self.md5_upper_event, add=True)
        self.str_trans_to_md5_button.pack(fill=BOTH, expand=True)
        # base64编码
        self.str_trans_to_bs64_button = Button(frm2, text="base64编码", bg="gold",
                                               command=self.str_trans_to_bs64)
        self.str_trans_to_bs64_button.pack(fill=BOTH, expand=True)
        # base64解码
        self.bs64_trans_to_str_button = Button(frm2, text="base64解码", bg="limegreen",
                                               command=self.bs64_trans_to_str)
        self.bs64_trans_to_str_button.pack(fill=BOTH, expand=True)
        # url编码
        self.str_trans_to_url_button = Button(frm2, text="URL编码", bg="gold",
                                              command=self.str_trans_to_url)
        self.str_trans_to_url_button.pack(fill=BOTH, expand=True)
        # url解码
        self.url_trans_to_str_button = Button(frm2, text="URL解码", bg="limegreen",
                                              command=self.url_trans_to_str)
        self.url_trans_to_str_button.pack(fill=BOTH, expand=True)
        # unicode转中文
        self.unicode_trans_to_zh_button = Button(frm2, text="Unicode转中文", bg="gold",
                                                 command=self.unicode_trans_to_zh)
        self.unicode_trans_to_zh_button.pack(fill=BOTH, expand=True)
        # json格式化
        self.str_trans_to_json_button = Button(frm2, text="Json格式化", bg="limegreen",
                                               command=self.str_trans_to_json)
        self.str_trans_to_json_button.pack(fill=BOTH, expand=True)
        # 右侧结果试图
        frm3 = Frame(self.init_window_name)
        frm3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.result_data_label = Label(frm3, height=2, text="输出结果", font=("宋体", 15, "bold"), bg="dodgerblue")
        self.result_data_label.pack(fill=X)
        copybtn = Button(self.result_data_label, text='一键复制', command=self.fast_copy)
        copybtn.pack(side=RIGHT)
        self.result_data_Text = ScrolledText(frm3, width=70, height=49)  # 处理结果展示
        self.result_data_Text.pack(fill=BOTH, expand=True)

    # 功能函数
    def str_trans_to_md5(self, upper=False):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                res = myMd5.hexdigest()
                if upper:
                    res = res.upper()
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def str_trans_to_bs64(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                res = base64.b64encode(src)
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def bs64_trans_to_str(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                res = base64.b64decode(src).decode()
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def str_trans_to_url(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                pass
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def url_trans_to_str(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                pass
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def unicode_trans_to_zh(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                pass
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def str_trans_to_json(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                tmp = json.loads(src)
                res = json.dumps(tmp, ensure_ascii=False, indent=2)
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    # 结果展示
    def write_res_to_text(self, res):
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, res)
        self.write_log_to_text("[INFO]:转换成功！")

    # 日志动态打印
    def write_log_to_text(self, logmsg):
        current_time = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
        logmsg_in = str(current_time) + logmsg + "\n"  # 换行
        self.log_data_Text.configure(state='normal')
        self.log_data_Text.insert(END, logmsg_in)
        self.log_data_Text.see(END)
        self.log_data_Text.configure(state='disabled')


# ----------------------- 使用示例 ----------------------------
root = tk.Tk()
root.geometry("1200x640")
tab_view = TabView(root, generate_body=create_body,
                   select_listen=select, remove_listen=remove)

toolframe = Frame(tab_view.body)
toolframe.pack(fill=BOTH, expand=True)
gui = ToolsGui(toolframe)
gui.set_init_window()
tab_view.add_tab(toolframe, '编码工具')
body = tab_view.body

tab_view.pack(fill=BOTH, expand=True, pady=2)
# tab_view.add_tab(mainframe, '转换工具')

# # 第一个参数是向body中添加的widget, 第二个参数是tab标题
# tab_view.add_tab(label_1, "tabs1")
# tab_view.add_tab(label_2, "tabs2")
#
# # TabView需要向x、y方向填充，且expand应设置为yes
# tab_view.pack(fill="both", expand='yes', pady=2)

root.mainloop()
