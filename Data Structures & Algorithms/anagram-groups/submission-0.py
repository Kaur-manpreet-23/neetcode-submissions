class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            fm = [0] * 26
            for a in i:
                fm[ord(a) - ord('a')] += 1
            key = tuple(fm)  
            if key in dic:   
                dic[key].append(i)  
            else:
                dic[key] = [i]
                
        return list(dic.values())