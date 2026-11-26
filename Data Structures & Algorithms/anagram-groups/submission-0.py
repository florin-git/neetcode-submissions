class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                idx = ord(c) - ord("a")
                count[idx] += 1
            
            key = []
            for i, info in enumerate(count):
                if info != 0:
                    char = chr(i + ord("a"))
                    key.append(f"{info}_{char}") 

            key = "".join(key)
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]


        return [l for l in hash_map.values()]
        