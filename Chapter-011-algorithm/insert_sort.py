# coding=utf-8

def insert_sort(nums):
    if len(nums)==0:
        return nums
    for i in range(1, len(nums)):
        temp=nums[i]
        j=i-1
        while j>=0:
            if temp<nums[j]:
                nums[j+1]=nums[j]
                j-=1
            else:
                nums[j+1]=temp
                break
        if j==-1:
            nums[0]=temp
    return nums


if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print(nums)
    print(insert_sort(nums))