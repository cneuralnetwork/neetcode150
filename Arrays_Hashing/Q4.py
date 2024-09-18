class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for s in strs:
            sortstr=''.join(sorted(s))
            if sortstr not in dict:
                dict[sortstr]=[]
            dict[sortstr].append(s)
        return list(dict.values())
        
