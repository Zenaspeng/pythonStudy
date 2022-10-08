from tkinter import *
import socket
import threading
from tkinter import messagebox
# 登录按钮逻辑




root = Tk()
text=Text(root)
text.pack()

root.title("系统登录")
root.geometry("400x300")

# 标签 用户名密码
Label(root, text='IP地址:').place(x=100, y=120)
Label(root, text='端口号:').place(x=100, y=160)
# 用户名输入框
var_usr_name = StringVar()
entry_usr_name = Entry(root, textvariable=var_usr_name,font=("Arial",10))
entry_usr_name.place(x=160, y=120)
# 密码输入框
var_usr_pwd = IntVar()
entry_usr_pwd = Entry(root, textvariable=var_usr_pwd, font=("Arial",10))
entry_usr_pwd.place(x=160, y=160)
bt_login = Button(root, text='开启', command=lambda :r_start())
bt_login1 = Button(root, text='开启', command=lambda :l_loopstart())
bt_login.place(x=190, y=230)
bt_login1.place(x=230, y=260)




def usr_log_in():
    # 输入框获取用户名密码
    IP = var_usr_name.get()
    PORT = var_usr_pwd.get()

    # 实例化一个套接字对象   family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM
    net_com = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 重复使用ip端口
    net_com.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定ip地址和端口号
    net_com.bind((IP, PORT))
    # 最大挂起的链接数量
    net_com.listen(5)
    print(PORT)
    # 等待客户端链接  连接后拿到客户端地址
    print('服务端已启动...')

    conn, client_addr = net_com.accept()
    print('连接成功', client_addr)
    l_loopstart(conn,net_com)



def r_start():
    t = threading.Thread(target=usr_log_in())
    t.start()
def l_loopstart(coon,net_com):
    t1=threading.Thread(target=loop(coon,net_com))
    t1.start()
def loop(conn,net_com):


    while True:  # 通信循环


        try:
            # 接收消息
            data = conn.recv(1024)  # 1024代表接收数据的最大字节数
            print('客户端发送的数据:', data.decode('utf-8'))
            text.insert(END,data.decode('utf-8'))
            msg = input('>> ').strip()
            # 发给客户端
            conn.send(msg.encode('utf-8'))
        except ConnectionResetError:
            break

    # 关闭连接
    conn.close()
    # 关闭服务端
    net_com.close()
if __name__ == '__main__':
 root.mainloop()


