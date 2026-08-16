class Solution:
    # money : 10, c = 4
    # c1: 7, c2: 1, c3: 1, c4: 1
    # money: 16 c = 4
    # c1: 13, c2: 1, c3: 1, c4: 1
    # c1: 8, money: 8, c= 3
    ##
    # money = 9,c = 2
    # money = 12, c = 2, max_amo_f_child= 12-1: 11; money - 8 == 4
    # money = 12, c =3
    def distMoney(self, money: int, children: int) -> int:
        max_amo_f_child = money - (children - 1)
        if money < children:
            return -1
        if money < 8 or max_amo_f_child < 8:
            return 0
        if money - 8 == 4 and children - 1 == 1:
            return 0
        if children == 1 and money > 8:
            return 0
        rec = self.distMoney(money-8, children-1) # 9, 1
        if rec == 0:
            return 1
        return 1 + rec

        