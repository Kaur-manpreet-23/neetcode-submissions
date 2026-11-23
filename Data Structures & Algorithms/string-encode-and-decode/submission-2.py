class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for a in strs:
            encoded.append(str(len(a)) + "," + a)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            comma_idx = s.find(",", i)
            length = int(s[i:comma_idx])
            start = comma_idx + 1
            decoded_strs.append(s[start : start + length])
            i = start + length
        return decoded_strs