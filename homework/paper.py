# one = [1]
# def recursion(digits):
#     if str(type(digits)) == "<class 'int'>":
#         if digits == 9:
#             return[1, 0]
#         else:
#             return [digits + 1]
        
#     elif digits[-1] != 9:
#         digits[-1] += 1
#         return digits
    
#     elif len(digits) == 2:
#         return recursion(digits[0]) + one
#     else:
#         return recursion(digits[0:-1]) + one

# print(recursion([1, 2, 3]))


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        one = [1]
        def recursion(dig):
            if str(type(dig)) == "<class 'int'>":
                if dig == 9:
                    return[1, 0]
                else:
                    return [dig + 1]
                
            elif dig[-1] != 9:
                dig[-1] += 1
                return dig
            
            elif len(dig) == 2:
                return recursion(dig[0]) + one
            else:
                return recursion(dig[0:-1]) + one
        return recursion(digits)     
    
print(Solution.plusOne([1,2,3], [1,2,3]))
  