class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''

        for l1, l2 in zip(word1, word2):
            merged += l1 + l2

        merged += word1[len(word2):] + word2[len(word1):]

        return merged