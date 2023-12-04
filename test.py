class Solution:
    def largestGoodInteger(self, num: str) -> str:
        save = []

        for i in range(len(num) -1):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                save.append(int(num[i]))

        return (f"{max(save)}{max(save)}{max(save)}")
    
solution = Solution()
    
print(solution.largestGoodInteger("6777133339"))