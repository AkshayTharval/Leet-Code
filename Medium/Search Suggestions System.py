class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        output = []
        products.sort()
        for i in range(len(searchWord)):
            temp_list = []
            for word in products:
                if len(temp_list) == 3:
                    break
                if searchWord[0:i+1] in word:
                    temp_list.append(word)
            
            output.append(temp_list)
        
        return output
        