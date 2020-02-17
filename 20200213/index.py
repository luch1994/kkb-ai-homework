class People:
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp


class Hero(People):
    def __init__(self, name, damage, hp, country):
        People.__init__(self, name, damage, hp)
        self.country = country

    def get_inf(self):
        print("姓名：{}".format(self.name))
        print("攻击力：{}".format(self.damage))
        print("当前血量：{}".format(self.hp))
        print("阵营：{}".format(self.country))
        print("*" * 20)

    def attack(self, enemy):
        print(self.name)
        print("攻击力为：{}".format(self.damage))
        print("{}目前血量为：{}".format(enemy.name, enemy.hp))
        print("{}攻击{}".format(self.name, enemy.name))
        enemy.hp -= self.damage
        print("{}剩余血量为：{}".format(enemy.name, enemy.hp))
        print("***********************************")

# 练习1，新建一个武器类同时能够将武器赋予某个实例，用以提升攻击力。
# 武器类
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def take_weapon(self, hro):
        """将武器给予英雄，英雄攻击力提升"""
        print("将武器{}装备给英雄{}".format(self.name, hro.name))
        hro.damage += self.damage
        print("{}的攻击力变为{}".format(hro.name, hro.damage))
        print("*" * 20)

# 练习1到练习3，主程序
def main():
    # 新创建People 的实例 XB 和 Hero 类实例 LB 和 ZF。
    XB = People('小兵', 1, 10)
    LB = Hero('吕布', 20, 100, "群雄")
    ZF = Hero('张飞', 7, 80, "蜀国")

    # 获取张飞的信息
    ZF.get_inf()

    # 张飞攻击吕布
    ZF.attack(LB)

    """
    练习2
    新建武器实例,其中包含属性：名称（丈八蛇矛）、伤害值（3）
    将武器赠与张飞
    """
    # 新建武器丈八蛇杖
    ZBSZ = Weapon("丈八蛇杖", 3)
    # 把丈八蛇杖给张飞
    ZBSZ.take_weapon(ZF)

    """
    练习3
    显示“ZF”目前信息
    令“ZF”攻击“LB”
    """
    # 显示张飞目前的信息
    ZF.get_inf()
    # 张飞攻击吕布
    ZF.attack(LB)


"""

提升练习 --“群英战吕布”¶
框架： 建立群英（多个hero实例）及吕布实例（属性值设置合理） 
让一个英雄（英雄1）与吕布持续战斗，当英雄1血量小于吕布攻击时，英雄1失败逃跑 
英雄1回复血量，同时加入英雄2，与吕布持续战斗，当。。。。 
持续添加英雄，直到吕布逃跑

"""

# 提升练习
def tisheng():
    # 创建吕布
    LB = Hero('吕布', 20, 100, "群雄")
    # 补充完善本代码块（实现指定功能即可）
    i = 0
    heros = {}
    while 1:
        i += 1
        # 创建新英雄
        new_hero = Hero("hero"+str(i), 15, 30, "反吕联盟")
        heros["hero"+str(i)] = new_hero
        # 用于判断是不是吕布逃跑
        is_lb_fail = False
        # 新英雄和吕布持续战斗
        while True:
            # 新英雄攻击吕布
            new_hero.attack(LB)
            # 新英雄逃跑，本轮战斗结束
            if LB.hp <= new_hero.damage:
                print("{}击败了吕布，吕布逃跑了。。。".format(new_hero.name))
                is_lb_fail = True
                break
            # 吕布攻击新英雄
            LB.attack(new_hero)
            # 新英雄逃跑，本轮战斗结束
            if new_hero.hp <= LB.damage:
                print("{}逃跑了。。。".format(new_hero.name))
                # 回血回30
                new_hero.hp = 30
                break
        # 吕布逃跑，战斗结束
        if is_lb_fail:
            break
    # 展示吕布的信息
    LB.get_inf()


if __name__ == "__main__":
    # 练习1到练习3
    main()
    # 提升练习
    print('\n\n\n')
    print("*" * 15, "提升练习", "*" * 15)
    tisheng()
