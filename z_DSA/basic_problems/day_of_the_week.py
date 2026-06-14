'''
Day of the Week
Difficulty: EasyAccuracy: 41.67%Submissions: 14K+Points: 2
Given an array date[] = [d, m, y], where d denotes the day, m denotes the month, and y denotes the year, Write a program that calculates the day of the week for any particular date in the past or future.

Examples:

Input: date[] = [28, 12, 1995]
Output: Thursday
Explanation: 28 December 1995 was a Thursday.
Input: date[] = [30, 8, 2010]
Output: Monday
Explanation: 30 August 2010 was a Monday.
Constraints:
1 ≤ d ≤ 31
1 ≤ m ≤ 12
1 ≤ y ≤ 2100
'''

# from datetime import date

# class Solution:
#     def getDayOfWeek(self, day, month, year):

#         days = [
#             "Monday",
#             "Tuesday",
#             "Wednesday",
#             "Thursday",
#             "Friday",
#             "Saturday",
#             "Sunday"
#         ]

#         d = date(year, month, day)

#         return days[d.weekday()]
    
'''Solution 2 without import'''
# class Solution:
#     def getDayOfWeek(self, date: list[int]) -> str:

#         d = date[0]  # day
#         m = date[1]  # month
#         y = date[2]  # year

#         days = [
#             "Sunday",
#             "Monday",
#             "Tuesday",
#             "Wednesday",
#             "Thursday",
#             "Friday",
#             "Saturday"
#         ]

#         # Jan and Feb come before leap day,
#         # so formula treats them as months 13 and 14
#         # of the previous year
#         if m < 3:
#             m += 12
#             y -= 1

#         # last 2 digits of year
#         # ex: 1995 -> 95
#         k = y % 100

#         # century part
#         # ex: 1995 -> 19
#         j = y // 100

#         # Zeller's formula gives a number from 0 to 6
#         h = (
#             d +
#             (13 * (m + 1)) // 5 +
#             k +
#             k // 4 +
#             j // 4 +
#             5 * j
#         ) % 7

#         # formula numbering:
#         # 0->Sat, 1->Sun, 2->Mon ...
#         # converting it to our days list numbering
#         mapping = [6, 0, 1, 2, 3, 4, 5]

#         return days[mapping[h]]