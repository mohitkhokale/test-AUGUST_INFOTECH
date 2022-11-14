# 5) Write a program or algorithm to implement bubble sort. [5 marks]
# You do not have to use any library for this.

def bub_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                swapped = True
                arr[j],arr[j+1]= arr[j+1],arr[j]

        if not swapped:

            return
arr=[64,34,25,12,11,22,90]
bub_sort(arr)

print("sort arr")

for i in range(len(arr)):
    print(" ", arr[i],end="")