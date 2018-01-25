
# count the number of inversions in an array of ints
def read_nums(fname):
    nums = []
    with open(fname,'r') as f:
        for line in f.read().split():
            nums.append(int(line))
    return nums

def inversion(nums):
    n = len(nums)
    if n < 2:
        return 0, nums
    
    lcount, left = inversion(nums[:n//2])
    rcount, right = inversion(nums[n//2:])
    
    merged =[]
    ileft = 0
    iright = 0
    count = 0
    while ileft < len(left) and iright < len(right):
        if left[ileft] <= right[iright]:
            merged.append(left[ileft])
            ileft += 1
        else:
            merged.append(right[iright])
            iright += 1
            count += len(left) - ileft
    merged.extend(left[ileft:])
    merged.extend(right[iright:])
    totalcount = lcount + rcount + count
    return totalcount, merged

fname = 'IntegerArray.txt'
nums = read_nums(fname)
print(inversion(nums)[0])

