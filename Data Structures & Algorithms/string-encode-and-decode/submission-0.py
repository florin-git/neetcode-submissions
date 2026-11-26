class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []
        for s in strs:
            l = len(s)
            encoded.append(f"{l}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            l = int(s[i: j])
            res.append(s[j + 1: j + 1 + l])

            i = j + 1 + l

        return res









