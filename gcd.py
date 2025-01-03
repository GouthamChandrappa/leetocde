class solution:
    def gcdofstrings(self, str1 :  str, str2 : str) -> str:    
        if str1 + str2 != str2 +str1:
          return ""
        

        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a
    
        gcd_len = gcd(len(str1),len(str2))
        return str1[:gcd_len]
    

if __name__ == "__main__":
    test_cases = [
        ("ABCABC", "ABC"),
        ("ABABAB", "AB"),
        ("LEET", "CODE")
    ]
    
    for i, (str1, str2) in enumerate(test_cases, 1):
        result = solution().gcdofstrings(str1, str2)
        print(f"Test Case {i}: {result}")
