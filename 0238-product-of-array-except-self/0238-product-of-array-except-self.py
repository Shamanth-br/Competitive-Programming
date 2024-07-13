class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,post = [1],[1]
        i,j = 1, len(nums)-1
        while(i < len(nums)):
            pre.append(pre[i-1]*nums[i-1])
            post.append(post[i-1]*nums[j])
            i += 1
            j -=1
        print(pre)
        print(post)
        # for a,b in zip(pre,post[::-1]):
        #     ans.append(a*b)
        return [a*b for a,b in zip(pre,post[::-1])]
        