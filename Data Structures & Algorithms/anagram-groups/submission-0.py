class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)

        for word in strs: 
            output_strs = [0]*26

            for letter in word:
               output_strs[ord(letter) - 97] += 1

            key = tuple(output_strs)
            strs_dict[key].append(word)
        return list(strs_dict.values())