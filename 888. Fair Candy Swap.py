class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        avg=(sum(A)+sum(B))/2
        diff=avg-sum(A)
        dict={x:x for x in B}
        for n in A:
            if n+diff in dict:
                return [n,n+diff]
                break


sln=Solution()
assert [5,4]==sln.fairCandySwap([1,2,5],[2,4])
assert [2,3]==sln.fairCandySwap([2],[1,3])
assert [1,2]==sln.fairCandySwap([1,2],[2,3])
assert [1,2]==sln.fairCandySwap([1,1],[2,2])