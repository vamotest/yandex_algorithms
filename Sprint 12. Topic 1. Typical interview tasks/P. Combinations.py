
class Solution:
    
    def __init__(self):
        self.characters = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        
    def letter_combinations(self, digits):
        if len(digits) == 0:
            return []
        
        result = []
        self.solve(digits, result)
        return result
    
    def solve(self, digits, result, current_string='',
              current_level=0):
        if current_level == len(digits):
            result.append(current_string)
            return
        
        for i in self.characters[int(digits[current_level])]:
            self.solve(digits, result, current_string + i, current_level + 1)


sol = Solution()
res = sol.letter_combinations(str(input()))
print(*res)
