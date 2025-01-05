class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define a set of vowels
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # Extract all vowels from the string
        vowel_list = [char for char in s if char in vowels]
        
        # Reconstruct the string with reversed vowels
        result = []
        for char in s:
            if char in vowels:
                result.append(vowel_list.pop())  # Replace with the last vowel in the reversed list
            else:
                result.append(char)  # Keep consonants unchanged
        
        return ''.join(result)
    
if __name__ == "__main__":
    case1 = "IceCreAm"
    case2 = "leetcode"
    s = [case1, case2]

    for i in s:
        print(Solution().reverseVowels(i))
        
        