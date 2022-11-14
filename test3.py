# 3) Write a program to find the second largest number in an array. [2.5 marks]

no = [1,2,3,4,5,6]

max = max(no[0],no[1])
sec_max = min(no[0],no[1])
n = len(no)

for i in range (2,n):
    if no[i]> max:
        sec_max = max
        max = no[i]
    elif no[i] > sec_max and max != no[i]:
        sec_max = no[i]
    elif max == sec_max and sec_max != no[i]:
        sec_max = no[i]

print("Sec larget no:",sec_max)

