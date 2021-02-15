'''https://leetcode.com/problems/trapping-rain-water/'''

class Solution:
    """two pointer"""

    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        lp = 0
        rp = len(height) - 1
        max_r = height[rp]
        max_l = height[lp]
        fill = 0

        while lp < rp:
            if height[lp] > height[rp]:
                fill += max_r - height[rp]
                rp -= 1
                max_r = max(max_r, height[rp])
            else:
                fill += max_l - height[lp]
                lp += 1
                max_l = max(max_l, height[lp])
        return fill

        # fill = 0
        # for idx,wall in enumerate(height):
        #     max_left = max(height[:idx+1])
        #     max_right = max(height[idx:])
        #     fill += (min(max_left,max_right)-wall)
        # return fill


#         while cur<max_rp:

#             while left and cur<=max_rp:
#                 if height[cur]>=height[lp]:
#                     lp = cur
#                     cur += 1
#                 else:
#                     left = False
#                     rp = cur

#             while not left and rp<max_rp:
#                 if height[cur]<=height[rp]:
#                     cur = rp
#                     rp += 1
#                 else:
#                     left = True
#                     lp = cur
#                     min_height = min(height[lp],height[rp])
#                     for k in range(lp+1,rp):
#                         water += (min_height-height[k])

#         return water