# class Solution:
#     def merge(self, intervals):
        
#         if len(intervals)==0:
#             return intervals
#         intervals = sorted(intervals, key = lambda x : x[0])

#         prev_len = len(intervals)
#         while True:
#             intervals = self.DiviedAndMerge(intervals)
#             if prev_len==len(intervals):
#                 break
#             prev_len = len(intervals)
        
#         return intervals
    
#     def DiviedAndMerge(self,lists):
        
        
#         if lists is None:
#             return
        
#         if len(lists)==2:
#             result = self.Merge(lists[0],lists[1])
#             return result
        
#         if len(lists)==1:
#             return lists


#         orginal_len = len(lists)
#         idx = math.ceil(len(lists)/2)
        
#         result_1= self.DiviedAndMerge(lists[:idx])
#         result_2 = self.DiviedAndMerge(lists[idx:])
        
#         result_1.extend(result_2)
#         result = result_1
#         if len(result_1)!=orginal_len:

#             result=self.DiviedAndMerge(result_1)
        
#         return result
            
#     def Merge(self,l1,l2):
        
#         if l1[1]>=l2[0]:
#             left = min(l1[0],l2[0])
#             right = max(l1[1],l2[1])
#             return [[left,right]]
#         else:
#             return [l1,l2]