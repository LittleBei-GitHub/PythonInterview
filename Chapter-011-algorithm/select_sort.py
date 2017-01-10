# coding=utf-8

def select_sort(nums):
    nums_len=len(nums)

    for i in range(nums_len):
        mix_index = i
        j=i+1
        while j<nums_len:
            if nums[mix_index]>nums[j]:
                mix_index=j
            j+=1
        temp=nums[i]
        nums[i]=nums[mix_index]
        nums[mix_index]=temp
    return nums


if __name__ == '__main__':
    nums = [10, 8, 4, -1, 2, 6, 7, 3]
    print(nums)
    print(select_sort(nums))