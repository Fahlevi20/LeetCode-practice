nums = [-1,0,1,2,-1,-4]
res = []
nums.sort()
print(nums)

for i, a in enumerate(nums):
	
    if i >0 and a == nums[i-1]:
     continue
     
    l, r = i+1, len(nums)-1
    print('ini adalah l',l)
    print('ini r',r)
    while l<r:
     threeSum = a+nums[l]+nums[r]
     if threeSum> 0:
      r-=1
      print('after:',r)
      print(threeSum)
     elif threeSum <0:
      l+=1
      print('after:',l)
      print(threeSum)
     else:
      res.append([a,nums[l],nums[r]])
     
