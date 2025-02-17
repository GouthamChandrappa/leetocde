class Solution():
    def maximumSwap(self, num:int) -> int:
        num_str = list(str(num))
        last_occurence = {int(digit): i for i, digit in enumerate(num_str)}


        for i , digit in enumerate(num_str):
            for d in range(9, int(digit), -1):
                if d in last_occurence and last_occurence[d] > i:
                    num_str[i], num_str[last_occurence[d]] = num_str[last_occurence[d]], num_str[i]
                    return int("".join(num_str))
                
        return num
    

soln = Solution()
print(soln.maximumSwap(2273))