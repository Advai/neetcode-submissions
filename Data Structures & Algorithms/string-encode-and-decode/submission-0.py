class Solution:

    def encode(self, strs: List[str]) -> str:
        # we use # as the delimiter
        # Hello World
        # 5#Hello5#World
        str_builder = []
        for str_to_encode in strs:
            if not len(str_to_encode):
                str_builder.append("0#")
            else:
                str_builder.append(str(len(str_to_encode)) + "#" + str_to_encode)
        return "".join(str_builder)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            result.append(s[start : start + length])
            i = start + length
        return result

