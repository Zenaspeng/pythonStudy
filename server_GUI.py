from tkinter import *
import socket
import threading
from tkinter import messagebox
# ��¼��ť�߼�




root = Tk()
text=Text(root)
text.pack()

root.title("ϵͳ��¼")
root.geometry("400x300")

# ��ǩ �û�������
Label(root, text='IP��ַ:').place(x=100, y=120)
Label(root, text='�˿ں�:').place(x=100, y=160)
# �û��������
var_usr_name = StringVar()
entry_usr_name = Entry(root, textvariable=var_usr_name,font=("Arial",10))
entry_usr_name.place(x=160, y=120)
# ���������
var_usr_pwd = IntVar()
entry_usr_pwd = Entry(root, textvariable=var_usr_pwd, font=("Arial",10))
entry_usr_pwd.place(x=160, y=160)
bt_login = Button(root, text='����', command=lambda :r_start())
bt_login1 = Button(root, text='����', command=lambda :l_loopstart())
bt_login.place(x=190, y=230)
bt_login1.place(x=230, y=260)




def usr_log_in():
    # ������ȡ�û�������
    IP = var_usr_name.get()
    PORT = var_usr_pwd.get()

    # ʵ����һ���׽��ֶ���   family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM
    net_com = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # �ظ�ʹ��ip�˿�
    net_com.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # ��ip��ַ�Ͷ˿ں�
    net_com.bind((IP, PORT))
    # ���������������
    net_com.listen(5)
    print(PORT)
    # �ȴ��ͻ�������  ���Ӻ��õ��ͻ��˵�ַ
    print('�����������...')

    conn, client_addr = net_com.accept()
    print('���ӳɹ�', client_addr)
    l_loopstart(conn,net_com)



def r_start():
    t = threading.Thread(target=usr_log_in())
    t.start()
def l_loopstart(coon,net_com):
    t1=threading.Thread(target=loop(coon,net_com))
    t1.start()
def loop(conn,net_com):


    while True:  # ͨ��ѭ��


        try:
            # ������Ϣ
            data = conn.recv(1024)  # 1024����������ݵ�����ֽ���
            print('�ͻ��˷��͵�����:', data.decode('utf-8'))
            text.insert(END,data.decode('utf-8'))
            msg = input('>> ').strip()
            # �����ͻ���
            conn.send(msg.encode('utf-8'))
        except ConnectionResetError:
            break

    # �ر�����
    conn.close()
    # �رշ����
    net_com.close()
if __name__ == '__main__':
 root.mainloop()


