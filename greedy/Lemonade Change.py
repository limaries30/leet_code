"""https://leetcode.com/problems/lemonade-change/"""


class Solution:
    """greedy"""

    def lemonadeChange(self, bills: List[int]) -> bool:

        money = [0, 0, 0, 0]  # 5,10,X,20

        for bill in bills:
            bill -= 5
            money[bill // 5] += 1

            for j in range(1, -1, -1):
                while bill >= 5 * (j + 1) and money[j] > 0 and bill > 0:
                    bill -= 5 * (j + 1)
                    money[j] -= 1

            if bill != 0:
                return False
        return True


class Solution:
    """if-else"""

    def lemonadeChange(self, bills: List[int]) -> bool:

        current_money = 0
        bank = {5: 0, 10: 0, 15: 0, 20: 0}
        for bill in bills:
            if bill > 5:
                change = bill - 5
                if bank[change] > 0:
                    bank[change] -= 1
                else:
                    if change == 5:
                        return False
                    if change == 10:
                        if bank[5] >= 2:
                            bank[5] -= 2
                        else:
                            return False
                    if change == 15:
                        if bank[10] > 0 and bank[5] > 0:
                            bank[10] -= 1
                            bank[5] -= 1
                        elif bank[5] >= 3:
                            bank[5] -= 3
                        else:
                            return False
            bank[bill] += 1
        return True