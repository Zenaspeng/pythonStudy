#================游戏测试==============
# 玩家
from random import randint
from time import  sleep

class Player:

    def __init__(self,stoneNumber,name):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵
        self.name = name

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            #print("该英雄生命值已满")
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength
# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100

 # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')
# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster
print('''
***************************************
****           游戏开始             ****
***************************************

'''
)
print("请输入你的游戏昵称（确定后不可修改）！！！！")
name = input()
play =Player(1000,name)
print("============")
print("=角色创建成功=")
print("============")
print("= 角色基本信息")
print("= 昵称 :"+name)
print("= 原石 :1000")
print("============")
print("游戏加载中.",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".",end="")
sleep(1)
print(".")

# 森林数量
forest_num = 7

# 森林 列表
forestList = []
print("游戏规则！！！通过所有森林，并且尽可能剩余较多的原石，原石越多越有机会竞选成功国王！！")
print("你有十秒钟的时间记住森林的妖怪分布，在之后的行程中将不再提示")

print("输入'ok',进入下一步")
ok=input(":")
while ok !='ok':
    print('请输入ok否则无法进入游戏')
    ok = input(":")
# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,end='')
sleep(10)
print("在进入森林之前你可以雇佣士兵为你战斗")
print("==================================================")
print("======              士兵基本信息         ===========")
print("==================================================")
sleep(1)
print("(1)弓箭兵：                                              (2)斧头兵：                    ")
print("----雇佣价： 100 灵石                                     ----雇佣价： 120 灵石")
print("----最大生命值： 100                                       ----最大生命值： 120     ")
print("----杀伤力                                                ----杀伤力")
print("---------- 杀死鹰妖  ： 损耗生命值 20                        ---------- 杀死鹰妖  ： 损耗生命值 80")
print("---------  杀死狼妖  :  损耗生命值 80                        ---------  杀死狼妖  :  损耗生命值 20")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("请选择佣兵/不少于一个(一次选择一个英雄，输入后回车即可，如果选择完成请输入8以进入下一步)")
print(":输入英雄对应编号")
flag=0
playnum=[]
while(flag!=8 and play.stoneNumber>=0 ):
    print(">>")
    pn=int(input())
    flag=pn

    if(pn==1 and play.stoneNumber>=100):
        print("选择成功")
        print("原石-100")
        playnum.append(pn)
        play.stoneNumber=play.stoneNumber-100
        print(f'原石剩余：{play.stoneNumber}')
        print('如果您选择完毕，可输入8以进入游戏')
    elif(pn==2 and play.stoneNumber>=120):
        print("选择成功")
        print("原石-120")
        playnum.append(pn)
        play.stoneNumber = play.stoneNumber - 120
        print(f'原石剩余：{play.stoneNumber}')
        print('如果您选择完毕，可输入8以进入游戏')

    elif (pn == 8 and len(playnum)==0):
        flag =9
        print("您至少选择一位英雄作战,请重新选择")

    elif (pn == 8 and len(playnum)>0):
        print("》》》》》》英雄选择成功《《《《《《《")
        print("------游戏即将开始-----")
        sleep(1)
        print("》",end="")
        sleep(1)
        print("》", end="")
        sleep(1)
        print("》", end="")
        sleep(1)
        print("》》》》》》》》》》》》")
        print("《《《您目前拥有的角色信息《《《")
        pa = 0
        pb = 0
        for i in range(len(playnum)):
          if playnum[i]==1:
              pa=pa+1
          else:
              pb=pb+1

        print(f'弓箭兵X{pa}')
        print(f'斧头兵X{pb}')
        begin(pa,pb)
    elif (pn == 2 and play.stoneNumber < 120):
        print("原石数目不足")
        print("输入8以退出并保存选择")
    elif (pn == 1 and play.stoneNumber < 100):
        print("原石数目不足")
        print("输入8以退出并保存选择")

    elif(pn!=1 or pn!=2 or pn!=8):
        print("未知指令")

    else:
        print("原石数目不足")
    @staticmethod
    def begin(pa,pb):

       print(f"您即将开始冒险",end="")
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
            print("您的英雄全部阵亡，游戏失败")
            flag=0
            break
        print(f'您即将进入第{flag}座森林')
        sleep(1)
        print("当前英雄状态：")
        sleep(0.5)
        print('弓箭兵----')
        maxarm = len(ARm)
        maxaxm = len(AXm)
        for i in range(len(ARm)):
           print("弓箭兵 ", end='')
           print("[", end='')
           print(ARm.get(i).name, end='')
           print("]", end='')
           print("  生命值 :", end='')
           print(ARm.get(i).strength)
        print('斧头兵----')
        for i in range(len(AXm)):
           print("斧头兵 ", end='')
           print("[", end='')
           print(AXm.get(i).name, end='')
           print("]", end='')

           print("  生命值 :", end='')
           print(AXm.get(i).strength)
        print("请选择你的出站英雄 [弓箭兵(1),斧头兵(2)]   ")
        sele = int(input(":"))
        index = 0
        index1 = 0
        while 1:
         if sele == 1 and len(ARm)>0:
           for i in range(len(ARm)):
               print(" | ", end='')
               print("弓箭兵 ", end='')
               print("[", end='')
               print(ARm.get(i).name, end='')
               print("]", end='')
               print("  生命值 :", end='')
               print(ARm.get(i).strength)

           print("请选择要作战英雄编号")
           vsNum = int(input(":"))
           if vsNum in ARm:
               VsArm[index] = ARm.get(vsNum)
               index = index + 1
               # ARm.pop(vsNum)
               for i in range(len(VsArm)):
                   print("弓箭兵 ", end='')
                   print("[", end='')
                   print(ARm.get(i).name, end='')
                   print("]", end='')
                   print("  生命值 :", end='')
                   print(ARm.get(i).strength)
                   print(" | ", end='')
               break
           else:
               print("您输入的英雄编号无效请重新选择")
               sleep(1)

         elif sele == 2 and len(AXm)>0:

           for i in range(len(AXm)):
               print(" | ",end='' )
               print("斧头兵",end='' )
               print("[",end='')
               print(AXm.get(i).name, end='')
               print("]",end='')
              # print("  :  ", end='')
               print("  生命值 :",end='')
               print(AXm.get(i).strength, end='')

           print("请选择要作战英雄编号")
           vsNum = int(input(":"))
           if vsNum in AXm:
               VsAXm[index] = AXm.get(vsNum)
               index = index + 1
               # AXm.pop(vsNum)
               for i in range(len(VsAXm)):
                   print(" | ", end='')
                   print("斧头兵 ", end='')
                   print("[", end='')
                   print(AXm.get(i).name, end='')
                   print("]", end='')
                   # print("  :  ", end='')
                   print("  生命值 :", end='')
                   print(AXm.get(i).strength)

               print("")
               break
           else:
               print("您输入的英雄编号无效请重新选择")
               sleep(1)
         else:
            print("您未获得该英雄，请重新选择英雄")
            print("请选择你的出站英雄 [弓箭兵(1),斧头兵(2)]   ")
            sele = int(input(":"))

        print(">>")

        sleep(1)
        print("您的英雄正在与怪物战斗中.",end='')
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)

        if forestList[flag-1].monster.typeName == '狼妖':
           if sele == 1 and ARm.get(vsNum).strength - 80>=0:

               ARm.get(vsNum).strength = ARm.get(vsNum).strength - 80
               # print(ARm.get(vsNum).strength)
           elif sele == 1 and ARm.get(vsNum).strength - 80<0:
               print("由于您的英雄在这次战斗中牺牲，你无法通过该森林，请重新选择英雄出站")
               ARm.get(vsNum).strength = 0
               continue
           elif sele == 2 and AXm.get(vsNum).strength - 20>=0:

               AXm.get(vsNum).strength = AXm.get(vsNum).strength - 20
           elif sele == 2 and AXm.get(vsNum).strength - 20 < 0:
               print("由于您的英雄在这次战斗中牺牲，你无法通过该森林，请重新选择英雄出站")
               AXm.get(vsNum).strength = 0
               continue
               # print(AXm.get(vsNum).strength)
        elif forestList[flag-1].monster.typeName == '鹰妖':
            if sele == 1 and ARm.get(vsNum).strength - 20>= 0:

                ARm.get(vsNum).strength = ARm.get(vsNum).strength - 20
                # print(ARm.get(vsNum).strength)
            elif sele == 1 and ARm.get(vsNum).strength - 20 < 0:
                print("由于您的英雄在这次战斗中牺牲，你无法通过该森林，请重新选择英雄出站")
                ARm.get(vsNum).strength = 0
                continue
            elif sele == 2 and AXm.get(vsNum).strength - 80 >= 0:

                AXm.get(vsNum).strength = AXm.get(vsNum).strength - 80
            elif sele == 2 and AXm.get(vsNum).strength - 80 < 0:
                print("由于您的英雄在这次战斗中牺牲，你无法通过该森林，请重新选择英雄出站")
                AXm.get(vsNum).strength = 0
                continue
                # print(AXm.get(vsNum).strength)
        sleep(1)
        print("战斗结束！")
        sleep(1)
        print("当前英雄状态：")
        print('弓箭兵')
        maxarm = len(ARm)
        maxaxm = len(AXm)
        for i in range(len(ARm)):
           print("弓箭兵 ", end='')
           print("[", end='')
           print(ARm.get(i).name, end='')
           print("]", end='')
           print("  生命值 :", end='')
           print(ARm.get(i).strength)
        print('斧头兵')
        for i in range(len(AXm)):
            print("斧头兵",end='')
            print("[", end='')
            print(AXm.get(i).name, end='')
            print("]", end='')
            # print("  :  ", end='')
            print("  生命值 :", end='')
            print(AXm.get(i).strength)
        yuanshi = play.stoneNumber
        print("您可以消耗原石为您的英雄恢复体力")
        print("不恢复，直接下一关(1),恢复(2)")
        ss = 2
        ans = int(input(":"))
        while ans != 1 and ans !=2:
            print("未知指令,请重新输入")
            sleep(1)
            ans = int(input(":"))




        while ans == 2 and ss == 2:
           print("请选择(1)弓箭兵(2)斧头兵")
           add = int(input(":"))
           if add == 1:
               print('请选择你要恢复的英雄')
               for i in range(len(ARm)):
                   print("弓箭兵 ", end='')
                   print("[", end='')
                   print(ARm.get(i).name, end='')
                   print("]", end='')
                   print("  生命值 :", end='')
                   print(ARm.get(i).strength)
               obb = int(input(":编号"))
               while 1:
                if  obb in ARm:
                 money = int(input('请输入恢复数量'))
                 if yuanshi >= money and ARm.get(obb).strength + money <= ARm.get(obb).maxStrength:
                   ARm.get(obb).strength = ARm.get(obb).strength + money
                   yuanshi = yuanshi - money
                   break
                 elif yuanshi >= money and ARm.get(obb).strength + money > ARm.get(obb).maxStrength:
                   print('已达到最大生命值，多余原石被扣除不返回')
                   ARm.get(obb).strength = ARm.get(obb).maxStrength
                   yuanshi = yuanshi - money
                   break
                 elif yuanshi <money:
                   print('余额不足')
                   sleep(1)

                 else:
                     print("请输入正确编号")
                     obb = int(input(":编号"))


           if add == 2:
               print('请选择你要恢复的英雄')
               for i in range(len(AXm)):
                   print("斧头兵 ", end='')
                   print("[", end='')
                   print(AXm.get(i).name, end='')
                   print("]", end='')
                   # print("  :  ", end='')
                   print("  生命值 :", end='')
                   print(AXm.get(i).strength)
               obb = int(input(":编号"))
               while 1:
                   if obb in AXm:
                    money = int(input('请输入恢复数量'))
                    if yuanshi >= money and AXm.get(obb).strength + money <= AXm.get(obb).maxStrength:
                     AXm.get(obb).strength = AXm.get(obb).strength + money
                     yuanshi = yuanshi - money
                     break
                    elif yuanshi >= money and AXm.get(obb).strength + money > AXm.get(obb).maxStrength:
                      print('已达到最大生命值，多余原石被扣除不返回')
                      AXm.get(obb).strength = AXm.get(obb).maxStrength
                      yuanshi = yuanshi - money
                      break
                    elif yuanshi<money:
                       print('余额不足')
                       sleep(1)

                   else:
                       print("请输入正确编号")
                       obb = int(input(":编号"))
           print("当前英雄状态：")
           print('弓箭兵')
           maxarm = len(ARm)
           maxaxm = len(AXm)
           for i in range(len(ARm)):
               print("弓箭兵 ", end='')
               print("[", end='')
               print(ARm.get(i).name, end='')
               print("]", end='')
               print("  生命值 :", end='')
               print(ARm.get(i).strength)
               print('斧头兵')
           for i in range(len(AXm)):
               print("斧头兵 ", end='')
               print("[", end='')
               print(AXm.get(i).name, end='')
               print("]", end='')
               # print("  :  ", end='')
               print("  生命值 :", end='')
               print(AXm.get(i).strength)
           print("输入(1)进入下一关，输入2继续治疗")
           ss = int(input(":"))
           while ss != 1 and ss != 2:
               print("未知指令,请重新输入")
               sleep(1)
               ss = int(input(":"))


        print(f"恭喜您，成功穿越第{flag}座森林")
        flag = flag + 1
       print(f"恭喜您，穿越了所有森林，您剩余原石数目为{play.stoneNumber}，快去竞选吧！！！")










