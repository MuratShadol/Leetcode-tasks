"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

"""


def dailyTemperatures(temperatures):
    monotonic = []
    answer = []
    for temp in range(len(temperatures)-1, -1, -1):
        if not monotonic:
            answer.append(0)
            monotonic.append((temperatures[temp], temp))
        elif monotonic[-1][0] < temperatures[temp]:
            
            while True:
                if monotonic[-1][0] <= temperatures[temp]:
                    monotonic.pop()
                    if not monotonic:
                        answer.append(0)
                        monotonic.append((temperatures[temp], temp))
                        break
                else:
                    answer.append(monotonic[-1][1] - temp)
                    monotonic.append((temperatures[temp], temp))
                    break
        elif monotonic[-1][0] > temperatures[temp]:
            answer.append(1)
            monotonic.append((temperatures[temp], temp))
    return answer[::-1], monotonic

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
# assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]