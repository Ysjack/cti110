# CTI-110
# P2HW2 - Score Avg
# Yashua Mcdougal
# 4/16/2022
#
print('Enter a series of 7 numbers')
score_list = list(map(int,input().split()))
print ('Enter score #1:',score list)
print ('Enter score #2:')
print ('Enter score #3:')
print ('Enter score #4:')
print ('Enter score #5:')
print ('Enter score #6:')
print ('Enter score #7:')
low = min(score_list)
high = max(score_list)
total = sum(score_list)
avg = total/len(score_list)
print("Lowest score:",low)
print('Modified List:',score_list)
print('scores Average:',avg)
series_set = set(score_list)
print('set content:',end=' ')
for i in score_list:
    print(i,end=' ')
