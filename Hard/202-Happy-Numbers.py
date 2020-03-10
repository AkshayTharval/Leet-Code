class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_string = str(n)
        happy = False
        count = 0
        seen_numbers = []
        seen_numbers.append(n_string)
        while(not happy):
            n_list = list(n_string)
            _sum = 0
            for el in n_list:
                
                _sum += int(el)**2
            
            if _sum == 1:
                happy = True
            
            n_string = str(_sum)
            
            if n_string in seen_numbers:
                break
            seen_numbers.append(n_string)

        return happy