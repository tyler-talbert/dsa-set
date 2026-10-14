class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dictionary 
        # key sorted(tuple((a: 1), (c: 1), (t: 1)) --> list['cat', 'act']

        anagrams = defaultdict(list)

        for word in strs:
            letter_count = defaultdict(int)
            for ch in word:
                letter_count[ch] += 1
            
            anagrams[frozenset(letter_count.items())].append(word)
        
        return list(anagrams.values())