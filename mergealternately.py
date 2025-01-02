class solution():
    def mergealternately(self,word1:str,word2:str):
        res=''
        for i in range(min(len(word1),len(word2))):
            res+=word1[i]+word2[i]
        return res+word1[i+1:]+word2[i+1:]
    
if __name__ == "__main__":
    # Create an instance of solution
    s = solution()
    
    # Test cases
    word1 = "abc"
    word2 = "pqr"
    result = s.mergealternately(word1, word2)
    print(f"Merged string: {result}")