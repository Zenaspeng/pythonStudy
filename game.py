#================��Ϸ����==============
# ���
from random import randint
from time import  sleep

class Player:

    def __init__(self,stoneNumber,name):
        self.stoneNumber = stoneNumber # ��ʯ����
        self.warriors = {}  # ӵ�е�սʿ�������������͸�ͷ��
        self.name = name

# սʿ
class Warrior:

    # ��ʼ������������ֵ
    def __init__(self, strength):
        self.strength = strength

    # ����ʯ����
    def healing(self, stoneCount):
        # ����Ѿ������������ֵ����ʯ�������ã��˷���
        if self.strength == self.maxStrength:
            #print("��Ӣ������ֵ����")
            return

        self.strength += stoneCount

        # ���ܳ����������ֵ
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength
# ������ �� սʿ������
class Archer(Warrior):
    # ��������
    typeName = '������'

    # ��Ӷ�� 100��ʯ�����ھ�̬����
    price = 100

    # �������ֵ �����ھ�̬����
    maxStrength = 100

 # ��ʼ������������ֵ, ����
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # ������ս��
    def fightWithMonster(self,monster):
        if monster.typeName== 'ӥ��':
            self.strength -= 20
        elif monster.typeName== '����':
            self.strength -= 80
        else:
            print('δ֪���͵����֣�����')
# ��ͷ�� �� սʿ������
class Axeman(Warrior):
    # ��������
    typeName = '��ͷ��'

    # ��Ӷ�� 120��ʯ
    price = 120

    # �������ֵ
    maxStrength = 120


    # ��ʼ������������ֵ, ����
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # ������ս��
    def fightWithMonster(self,monster):
        if monster.typeName== 'ӥ��':
            self.strength -= 80
        elif monster.typeName== '����':
            self.strength -= 20
        else:
            print('δ֪���͵����֣�����')

# ӥ��
class Eagle():
    typeName = 'ӥ��'

# ����
class Wolf():
    typeName = '����'

# ɭ��
class Forest():
    def __init__(self,monster):
        # ��ɭ�����������
        self.monster = monster
print('''
***************************************
****           ��Ϸ��ʼ             ****
***************************************

'''
)
print("�����������Ϸ�ǳƣ�ȷ���󲻿��޸ģ���������")
name = input()
play =Player(1000,name)
print("============")
print("=��ɫ�����ɹ�=")
print("============")
print("= ��ɫ������Ϣ")
print("= �ǳ� :"+name)
print("= ԭʯ :1000")
print("============")
print("��Ϸ������.",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".")

# ɭ������
forest_num = 7

# ɭ�� �б�
forestList = []
print("��Ϸ���򣡣���ͨ������ɭ�֣����Ҿ�����ʣ��϶��ԭʯ��ԭʯԽ��Խ�л��Ὰѡ�ɹ���������")
print("����ʮ���ӵ�ʱ���סɭ�ֵ����ֲַ�����֮����г��н�������ʾ")

print("����'ok',������һ��")
ok=input(":")
while ok !='ok':
    print('������ok�����޷�������Ϸ')
    ok = input(":")
# Ϊÿ��ɭ��������� ӥ������ ����
notification = 'ǰ��ɭ����������ǣ�'  # ��ʾ����Ļ�ϵ�����
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'��{i+1}��ɭ�������� {forestList[i].monster.typeName}  '

# ��ʾ ������Ϣ
print(notification,end='')
sleep(10)
print("�ڽ���ɭ��֮ǰ����Թ�Ӷʿ��Ϊ��ս��")
print("==================================================")
print("======              ʿ��������Ϣ         ===========")
print("==================================================")
sleep(1)
print("(1)��������                                              (2)��ͷ����                    ")
print("----��Ӷ�ۣ� 100 ��ʯ                                     ----��Ӷ�ۣ� 120 ��ʯ")
print("----�������ֵ�� 100                                       ----�������ֵ�� 120     ")
print("----ɱ����                                                ----ɱ����")
print("---------- ɱ��ӥ��  �� �������ֵ 20                        ---------- ɱ��ӥ��  �� �������ֵ 80")
print("---------  ɱ������  :  �������ֵ 80                        ---------  ɱ������  :  �������ֵ 20")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("��ѡ��Ӷ��/������һ��(һ��ѡ��һ��Ӣ�ۣ������س����ɣ����ѡ�����������8�Խ�����һ��)")
print(":����Ӣ�۶�Ӧ���")
flag=0
playnum=[]
while(flag!=8 and play.stoneNumber>=0 ):
    print(">>")
    pn=int(input())
    flag=pn

    if(pn==1 and play.stoneNumber>=100):
        print("ѡ��ɹ�")
        print("ԭʯ-100")
        playnum.append(pn)
        play.stoneNumber=play.stoneNumber-100
        print(f'ԭʯʣ�ࣺ{play.stoneNumber}')
        print('�����ѡ����ϣ�������8�Խ�����Ϸ')
    elif(pn==2 and play.stoneNumber>=120):
        print("ѡ��ɹ�")
        print("ԭʯ-120")
        playnum.append(pn)
        play.stoneNumber = play.stoneNumber - 120
        print(f'ԭʯʣ�ࣺ{play.stoneNumber}')
        print('�����ѡ����ϣ�������8�Խ�����Ϸ')

    elif (pn == 8 and len(playnum)==0):
        flag =9
        print("������ѡ��һλӢ����ս,������ѡ��")

    elif (pn == 8 and len(playnum)>0):
        print("������������Ӣ��ѡ��ɹ���������������")
        print("------��Ϸ������ʼ-----")
        sleep(1)
        print("��",end="")
        sleep(1)
        print("��", end="")
        sleep(1)
        print("��", end="")
        sleep(1)
        print("������������������������")
        print("��������Ŀǰӵ�еĽ�ɫ��Ϣ������")
        pa = 0
        pb = 0
        for i in range(len(playnum)):
          if playnum[i]==1:
              pa=pa+1
          else:
              pb=pb+1

        print(f'������X{pa}')
        print(f'��ͷ��X{pb}')
        begin(pa,pb)
    elif (pn == 2 and play.stoneNumber < 120):
        print("ԭʯ��Ŀ����")
        print("����8���˳�������ѡ��")
    elif (pn == 1 and play.stoneNumber < 100):
        print("ԭʯ��Ŀ����")
        print("����8���˳�������ѡ��")

    elif(pn!=1 or pn!=2 or pn!=8):
        print("δָ֪��")

    else:
        print("ԭʯ��Ŀ����")
    @staticmethod
    def begin(pa,pb):

       print(f"��������ʼð��",end="")
       sleep(1)
       print(".",end="")
       sleep(1)
       print(".",end="")
       sleep(1)
       print(".")
       print(">.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>.>")
       ARm = {}
       VsArm = {}
       AXm = {}
       VsAXm = {}

       for i in range(pa):
           # print(i)
           ARm[i] = Archer(i, 100)
           # print(ARm[len(ARm)-1].name)

       for j in range(pb):
           AXm[j] = Axeman(j, 120)
       flag = 1
       while flag <= 7 :


        he = 0
        for i in range(len(ARm)):
           if i in ARm:
               he = he + ARm[i].strength
        for i in range(len(AXm))  :

           if i in AXm:
               he = he +AXm[i].strength

        if he == 0:
            print("����Ӣ��ȫ����������Ϸʧ��")
            flag=0
            break
        print(f'�����������{flag}��ɭ��')
        sleep(1)
        print("��ǰӢ��״̬��")
        sleep(0.5)
        print('������----')
        maxarm = len(ARm)
        maxaxm = len(AXm)
        for i in range(len(ARm)):
           print("������ ", end='')
           print("[", end='')
           print(ARm.get(i).name, end='')
           print("]", end='')
           print("  ����ֵ :", end='')
           print(ARm.get(i).strength)
        print('��ͷ��----')
        for i in range(len(AXm)):
           print("��ͷ�� ", end='')
           print("[", end='')
           print(AXm.get(i).name, end='')
           print("]", end='')

           print("  ����ֵ :", end='')
           print(AXm.get(i).strength)
        print("��ѡ����ĳ�վӢ�� [������(1),��ͷ��(2)]   ")
        sele = int(input(":"))
        index = 0
        index1 = 0
        while 1:
         if sele == 1 and len(ARm)>0:
           for i in range(len(ARm)):
               print(" | ", end='')
               print("������ ", end='')
               print("[", end='')
               print(ARm.get(i).name, end='')
               print("]", end='')
               print("  ����ֵ :", end='')
               print(ARm.get(i).strength)

           print("��ѡ��Ҫ��սӢ�۱��")
           vsNum = int(input(":"))
           if vsNum in ARm:
               VsArm[index] = ARm.get(vsNum)
               index = index + 1
               # ARm.pop(vsNum)
               for i in range(len(VsArm)):
                   print("������ ", end='')
                   print("[", end='')
                   print(ARm.get(i).name, end='')
                   print("]", end='')
                   print("  ����ֵ :", end='')
                   print(ARm.get(i).strength)
                   print(" | ", end='')
               break
           else:
               print("�������Ӣ�۱����Ч������ѡ��")
               sleep(1)

         elif sele == 2 and len(AXm)>0:

           for i in range(len(AXm)):
               print(" | ",end='' )
               print("��ͷ��",end='' )
               print("[",end='')
               print(AXm.get(i).name, end='')
               print("]",end='')
              # print("  :  ", end='')
               print("  ����ֵ :",end='')
               print(AXm.get(i).strength, end='')

           print("��ѡ��Ҫ��սӢ�۱��")
           vsNum = int(input(":"))
           if vsNum in AXm:
               VsAXm[index] = AXm.get(vsNum)
               index = index + 1
               # AXm.pop(vsNum)
               for i in range(len(VsAXm)):
                   print(" | ", end='')
                   print("��ͷ�� ", end='')
                   print("[", end='')
                   print(AXm.get(i).name, end='')
                   print("]", end='')
                   # print("  :  ", end='')
                   print("  ����ֵ :", end='')
                   print(AXm.get(i).strength)

               print("")
               break
           else:
               print("�������Ӣ�۱����Ч������ѡ��")
               sleep(1)
         else:
            print("��δ��ø�Ӣ�ۣ�������ѡ��Ӣ��")
            print("��ѡ����ĳ�վӢ�� [������(1),��ͷ��(2)]   ")
            sele = int(input(":"))

        print(">>")

        sleep(1)
        print("����Ӣ�����������ս����.",end='')
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)

        if forestList[flag-1].monster.typeName == '����':
           if sele == 1 and ARm.get(vsNum).strength - 80>=0:

               ARm.get(vsNum).strength = ARm.get(vsNum).strength - 80
               # print(ARm.get(vsNum).strength)
           elif sele == 1 and ARm.get(vsNum).strength - 80<0:
               print("��������Ӣ�������ս�������������޷�ͨ����ɭ�֣�������ѡ��Ӣ�۳�վ")
               ARm.get(vsNum).strength = 0
               continue
           elif sele == 2 and AXm.get(vsNum).strength - 20>=0:

               AXm.get(vsNum).strength = AXm.get(vsNum).strength - 20
           elif sele == 2 and AXm.get(vsNum).strength - 20 < 0:
               print("��������Ӣ�������ս�������������޷�ͨ����ɭ�֣�������ѡ��Ӣ�۳�վ")
               AXm.get(vsNum).strength = 0
               continue
               # print(AXm.get(vsNum).strength)
        elif forestList[flag-1].monster.typeName == 'ӥ��':
            if sele == 1 and ARm.get(vsNum).strength - 20>= 0:

                ARm.get(vsNum).strength = ARm.get(vsNum).strength - 20
                # print(ARm.get(vsNum).strength)
            elif sele == 1 and ARm.get(vsNum).strength - 20 < 0:
                print("��������Ӣ�������ս�������������޷�ͨ����ɭ�֣�������ѡ��Ӣ�۳�վ")
                ARm.get(vsNum).strength = 0
                continue
            elif sele == 2 and AXm.get(vsNum).strength - 80 >= 0:

                AXm.get(vsNum).strength = AXm.get(vsNum).strength - 80
            elif sele == 2 and AXm.get(vsNum).strength - 80 < 0:
                print("��������Ӣ�������ս�������������޷�ͨ����ɭ�֣�������ѡ��Ӣ�۳�վ")
                AXm.get(vsNum).strength = 0
                continue
                # print(AXm.get(vsNum).strength)
        sleep(1)
        print("ս��������")
        sleep(1)
        print("��ǰӢ��״̬��")
        print('������')
        maxarm = len(ARm)
        maxaxm = len(AXm)
        for i in range(len(ARm)):
           print("������ ", end='')
           print("[", end='')
           print(ARm.get(i).name, end='')
           print("]", end='')
           print("  ����ֵ :", end='')
           print(ARm.get(i).strength)
        print('��ͷ��')
        for i in range(len(AXm)):
            print("��ͷ��",end='')
            print("[", end='')
            print(AXm.get(i).name, end='')
            print("]", end='')
            # print("  :  ", end='')
            print("  ����ֵ :", end='')
            print(AXm.get(i).strength)
        yuanshi = play.stoneNumber
        print("����������ԭʯΪ����Ӣ�ۻָ�����")
        print("���ָ���ֱ����һ��(1),�ָ�(2)")
        ss = 2
        ans = int(input(":"))
        while ans != 1 and ans !=2:
            print("δָ֪��,����������")
            sleep(1)
            ans = int(input(":"))




        while ans == 2 and ss == 2:
           print("��ѡ��(1)������(2)��ͷ��")
           add = int(input(":"))
           if add == 1:
               print('��ѡ����Ҫ�ָ���Ӣ��')
               for i in range(len(ARm)):
                   print("������ ", end='')
                   print("[", end='')
                   print(ARm.get(i).name, end='')
                   print("]", end='')
                   print("  ����ֵ :", end='')
                   print(ARm.get(i).strength)
               obb = int(input(":���"))
               while 1:
                if  obb in ARm:
                 money = int(input('������ָ�����'))
                 if yuanshi >= money and ARm.get(obb).strength + money <= ARm.get(obb).maxStrength:
                   ARm.get(obb).strength = ARm.get(obb).strength + money
                   yuanshi = yuanshi - money
                   break
                 elif yuanshi >= money and ARm.get(obb).strength + money > ARm.get(obb).maxStrength:
                   print('�Ѵﵽ�������ֵ������ԭʯ���۳�������')
                   ARm.get(obb).strength = ARm.get(obb).maxStrength
                   yuanshi = yuanshi - money
                   break
                 elif yuanshi <money:
                   print('����')
                   sleep(1)

                 else:
                     print("��������ȷ���")
                     obb = int(input(":���"))


           if add == 2:
               print('��ѡ����Ҫ�ָ���Ӣ��')
               for i in range(len(AXm)):
                   print("��ͷ�� ", end='')
                   print("[", end='')
                   print(AXm.get(i).name, end='')
                   print("]", end='')
                   # print("  :  ", end='')
                   print("  ����ֵ :", end='')
                   print(AXm.get(i).strength)
               obb = int(input(":���"))
               while 1:
                   if obb in AXm:
                    money = int(input('������ָ�����'))
                    if yuanshi >= money and AXm.get(obb).strength + money <= AXm.get(obb).maxStrength:
                     AXm.get(obb).strength = AXm.get(obb).strength + money
                     yuanshi = yuanshi - money
                     break
                    elif yuanshi >= money and AXm.get(obb).strength + money > AXm.get(obb).maxStrength:
                      print('�Ѵﵽ�������ֵ������ԭʯ���۳�������')
                      AXm.get(obb).strength = AXm.get(obb).maxStrength
                      yuanshi = yuanshi - money
                      break
                    elif yuanshi<money:
                       print('����')
                       sleep(1)

                   else:
                       print("��������ȷ���")
                       obb = int(input(":���"))
           print("��ǰӢ��״̬��")
           print('������')
           maxarm = len(ARm)
           maxaxm = len(AXm)
           for i in range(len(ARm)):
               print("������ ", end='')
               print("[", end='')
               print(ARm.get(i).name, end='')
               print("]", end='')
               print("  ����ֵ :", end='')
               print(ARm.get(i).strength)
               print('��ͷ��')
           for i in range(len(AXm)):
               print("��ͷ�� ", end='')
               print("[", end='')
               print(AXm.get(i).name, end='')
               print("]", end='')
               # print("  :  ", end='')
               print("  ����ֵ :", end='')
               print(AXm.get(i).strength)
           print("����(1)������һ�أ�����2��������")
           ss = int(input(":"))
           while ss != 1 and ss != 2:
               print("δָ֪��,����������")
               sleep(1)
               ss = int(input(":"))


        print(f"��ϲ�����ɹ���Խ��{flag}��ɭ��")
        flag = flag + 1
       print(f"��ϲ������Խ������ɭ�֣���ʣ��ԭʯ��ĿΪ{play.stoneNumber}����ȥ��ѡ�ɣ�����")










