from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.known_pairs = {}

        def uncrossedHelper(AFrom: int, BFrom: int) -> int:
            if (AFrom, BFrom) in self.known_pairs:
                return self.known_pairs[(AFrom, BFrom)]

            maxNumber = 0
            maxJ = len(B)
            for i in range(AFrom, len(A)):
                j = BFrom
                while (j < maxJ):
                    if A[i] == B[j]:
                        # if one match found, no need to look for both larger i and j
                        maxJ = j
                        if (i == len(A) - 1 or j == len(B) - 1):
                            maxNumber = max(maxNumber, 1)
                        else:
                            currentNumber = 1 + uncrossedHelper(i + 1, j + 1)
                            maxNumber = max(maxNumber, currentNumber)
                    j += 1
            self.known_pairs[(AFrom, BFrom)] = maxNumber
            return maxNumber

        return uncrossedHelper(0, 0)


s = Solution()
A = [1, 3, 7, 1, 7, 5]
B = [1, 9, 2, 5, 1]
print(s.maxUncrossedLines(A, B))
