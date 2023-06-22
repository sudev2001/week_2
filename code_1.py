# # _-_-_-_-_-_MEAN_-_-_-_-_-_[1.a]

# list1=[83,70,70,63,70,70]

# def mean(list):
#     return sum(list) / len(list)
# print("Mean=",mean(list1))

# # _-_-_-_-_-_Using Numpy Module_-_-_-_-_-_[1.b]
# import numpy as np
# list1=[83,70,70,63,70,70]
# mean1= np.mean(list1)
# print("Mean=",mean1)

# # _-_-_-_-_-_MODE_-_-_-_-_-_[2.a]

# list1=[1,2,1,2,3,4,3]
# def mode(list1):
#     count={}
#     for num in list1:
#         if num in count:
#             count[num]+=1
#         else:
#             count[num]=1

    
#     mode= [num for num,ctr in count.items() if max(count.values())==ctr]
#     return mode
# print("Mode=",mode(list1))

# _-_-_-_-_-_Using Statistics Module_-_-_-_-_-_[2.b]
# import statistics as ss
# list1=[1,2,1,2,3,4,3]
# mode1 = ss.multimode(list1)
# print("Mode=",mode1)

# _-_-_-_-_-_MEDIAN_-_-_-_-_-_[3.a]
# list1=[1,3,4,2,6,5]
# def median(list1):
#     list1.sort()
#     n = len(list1)
#     if n%2!=0:
#         median = list1[n//2]
#     else:
#         median = (list1[(n//2)-1] + list1[(n//2)])/2
#     return median
# print(median(list1))

# _-_-_-_-_-_Using Numpy Module_-_-_-_-_-_[3.b]
# import numpy as ss
# list1=[1,3,4,2,6,5]
# median = ss.median(list1)
# print("Median=",median)

# _-_-_-_-_-_RANGE_-_-_-_-_-_[4.a]
# def range(list1):
#     maximum=max(list1)
#     minimum = min(list1)
#     range = maximum - minimum
#     return range

# list1=[1,2,1,2,3,4,3]
# print("Range=",range(list1))

# _-_-_-_-_-_VARIANCE_-_-_-_-_-_[5.a]
# list1=[1,2,1,2,3,4,3]

# def variance(list1):
#     mean = sum(list1)/len(list1)
#     sum1=0
#     for num in list1:
#         num = (num-mean)**2
#         sum1 += num
#     variance = sum1/len(list1)
#     return variance

# print(variance(list1))

# _-_-_-_-_-_Using Numpy Module_-_-_-_-_-_[5.b]
# import numpy as np
# var = np.var(list1)
# print(var)

# _-_-_-_-_-_STANDARD DEVIATION_-_-_-_-_-_[6.a]
# list1=[83,70,70,63,70,70]

# from  math import sqrt
# def standard_deviation(list1):
#     mean = sum(list1)/len(list1)
#     sum1=0
#     for num in list1:
#         num = (num-mean)**2
#         sum1 += num
#     variance = sum1/len(list1)
#     s_d = sqrt(variance)
#     return s_d

# print(standard_deviation(list1))

# # _-_-_-_-_-_Using Numpy Module_-_-_-_-_-_[6.b]

# import numpy as np
# s_d = np.std(list1)
# print(s_d)

# # _-_-_-_-_-_COVARIANCE_-_-_-_-_-_[7.a]
# hour = [1,2,3,4,5,6]
# w_loss=[1.5,2.25,3.375,5.0625,7.59375,11.390625]

# def covariance(list1,list2):
#     leng = len(list1)
#     mean_list1 = sum(list1)/len(list1)
#     mean_list2 = sum(list2)/len(list2)
#     sums = sum((list1[i]-mean_list1) * (list2[i]-mean_list2) for i in range(leng))
#     cov = sums/(leng-1)
#     return cov

# print(covariance(hour,w_loss))

# # _-_-_-_-_-_Using Numpy Module_-_-_-_-_-_[7.b]
# import numpy as np
# cov1 = np.cov(hour,w_loss)[0,1]
# print(cov1)

# # _-_-_-_-_-_CORRELATION_-_-_-_-_-_[8.a]
# import math

# hour = [1,2,3,4,5,6]
# w_loss=[1.5,2.25,3.375,5.0625,7.59375,11.390625]

# def correlation(list1,list2):
#     leng = len(list1)
#     mean_list1 = sum(list1)/len(list1)
#     mean_list2 = sum(list2)/len(list2)
#     sums = sum((list1[i]-mean_list1) * (list2[i]-mean_list2) for i in range(leng))
#     sq_root = math.sqrt((sum(((list1[i]-mean_list1)**2) for i in range(leng)) * sum(((list2[i]-mean_list2)**2) for i in range(leng))))
#     cor = sums/sq_root
#     return cor

# print(correlation(hour,w_loss))

# # _-_-_-_-_-_Using Numpy Module_-_-_-_-_-_[8.b]
# import numpy as np
# cor = np.corrcoef(hour,w_loss)[0,1]
# print(cor)

# def maximizeSum(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: int
#     """
#     sum=0
#     p=0
#     for i in range(k):
#         max = nums[0]
#         for j in range(len(nums)):
#             if max < nums[j]:
#                 max = nums[j]
#                 p=j
#         sum+=max
#         nums[p] +=1
        
#     return sum

# nums = [10,4,7,9,6,3,1,8,6,1,1,1,9,10,9,3,7,6,10,10,5,2,10,6,2,10,6,2,1,6,3,9,9,7,1,4,3,3,6,4,8,3,10,7,2,10,8,1,3,3,9,3]
# print(maximizeSum(nums,6))

a1 = ['ab','c']

# def passThePillow(n, time):
#         """
#         :type n: int
#         :type time: int
#         :rtype: int
#         """
#         i=j=1
#         p=1
#         while True:
#             print(j,'---')
#             print(i,'-,,')
#             if j < n:
#                 if i == time:
#                     return j
#                 else:
#                     i+=1
#                     j+=1
#             else:
#                 if n-p > 1:
#                     if i == time:
#                         return j-p
#                     else:
#                         i+=1
#                         p+=1
#                 else:
#                     n=1
# print(passThePillow(4,5))

def findNum(n,v):


print(findNum(18,38))