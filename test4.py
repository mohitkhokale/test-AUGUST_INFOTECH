 # Given an integer array numbers and return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. [5 marks]
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def findtrip(arr,n):
    found =False
    for i in range(0,n-2):

        for j in range(i+1,n-1):
        
            for k in range(j+1,n):

                if(arr[i]+arr[j]+arr[k]==0):
                    print(arr[i],arr[j],arr[k])
                    found =True

    if (found ==False):
        print("nothing")

arr = [-1,0,1,2,-1,-4]

no = len(arr)
findtrip(arr,no)