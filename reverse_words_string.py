class solution:
    def stringreverse(self, s: str) -> str :
        words_list =  s.split()
        reversed_words = words_list[::-1]

        return " ".join(reversed_words)
    

if __name__ == "__main__":
    s1 = "the sky is the limit"
    print(f"Input string: {s1}")
    print(f"Output string: the reversed string is {solution().stringreverse(s1)}")

