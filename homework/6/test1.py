class solution:
    def __init__(self, amount: int, coins: list) -> None:
        self.amount: int = amount
        self.coins: list = sorted(coins, reverse=True)
        self.up: int = max(coins)
        self.down: int = min(coins)
        self.ok: int = None

    def utils(self, rest_money: int, num: int) -> None:
        """递归函数

        Args:
            rest_money (int): 剩余的钱
            num (int): 已有的钱的数量
        """
        if rest_money == 0:
            # 搜集结果
            if (self.ok == None) or (num < self.ok):
                self.ok = num
            return
        if rest_money < 0:
            # 找零失败
            return
        if (self.ok != None) and (rest_money / self.up + num > self.ok):
            # 剪枝
            return
        for i in self.coins:
            self.utils(rest_money - i, 1 + num)
            pass

    def handle(self):
        self.utils(self.amount, 0)
        if self.ok == None:
            print(-1)
        else:
            print(self.ok)


if __name__ == "__main__":
    print("hello world")
    s = solution(0, [1])
    s.handle()
