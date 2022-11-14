# 10) Write a program or algorithm for Two Elements whose sum is closest to zero. [2.5 marks]
# Example
# You are given an array [-23, 12, -35, 45, 20, 36] then the two elements would be -35 & 36 as their pair sum is 1 which is closest to 0

def minsum(arr,arr_size):
    cnt =0

    if arr_size <2:
        print("Invalid Input")
        return

    lmin = 0
    rmin = 1
    minsum = arr[0] +arr[1]
    for 1 in range(0,arr_size):