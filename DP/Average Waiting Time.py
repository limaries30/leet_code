"""https://leetcode.com/problems/average-waiting-time/"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        end = 0
        ans = 0
        working = False

        for customer in customers:

            if end < customer[0]:
                end = sum(customer)
                ans += customer[1]
            else:
                end += customer[1]
                ans += end - customer[0]

        return ans / len(customers)
