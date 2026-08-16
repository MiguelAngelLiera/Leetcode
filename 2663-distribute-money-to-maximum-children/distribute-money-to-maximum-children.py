class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children
        if money < 0:
            return -1

        recieved = money // 7
        residue = money % 7

        if recieved == children and residue == 0:
            return recieved

        if recieved == children - 1 and residue == 3:
            # 8, 8, 8, 4, recieved = 3, residue= 4
            # 8, 8, 7, 5, recieved = 2, residue = 5
            return recieved - 1

        # money = 10, children = 5
        # money = 5
        # recived = 0, residue = 5
        # children - 1
        return min(children - 1, recieved)


        