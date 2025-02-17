class solution:
    def palindrome(self, s:str) -> print("The string is palindrome" : bool):
        lower = s.lower()
        combined_string = ''.join(char for char in lower if  char.isalnum())
        print(f"The combined and cleaned string is:{combined_string}")
        return combined_string == combined_string[::-1]
    


soln = solution()

test_case1 = soln.palindrome("A man, a plan, a canal: Panama")
print(test_case1)





        