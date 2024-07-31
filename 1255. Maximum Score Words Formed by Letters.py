from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_score = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [],
                        'j': [], 'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [],
                        's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
        words_values = {}

        j = 0
        for i in letter_score:
            letter_score[i] = score[j]
            j += 1

        temp_sum = 0
        for i in words:
            for j in i:
                temp_sum += letter_score[j]
            if i not in words_values:
                words_values[i] = []
            words_values[i] = temp_sum
            temp_sum = 0

        # Check if Words can be formed
        for i in words:
            for j in i:
                if j in letters:
                    letters.remove(j)


sol = Solution()
print(sol.maxScoreWords(["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                        [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
