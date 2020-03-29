import re
class Solution(object):

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = paragraph.lower()
        paragraph = re.sub('[^A-Za-z0-9]+', ' ', paragraph)

        freq = {}
        for word in paragraph.split(' '):
            if word in freq:
                freq[str(word)] += 1
            else:
                freq[str(word)] = 1

        max_keys = ''
        current_max = 0
        for key in freq.keys():
            if freq[key] > current_max and key != '' and key not in banned:
                current_max = freq[key]
                max_keys = key

        return max_keys