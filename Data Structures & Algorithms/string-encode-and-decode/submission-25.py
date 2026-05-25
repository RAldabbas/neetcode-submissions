class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = ""
        for s in strs:
            for c in s:
                ret_str += str(ord(c)) + "'"
            ret_str += "|"
        return ret_str

    def decode(self, s: str) -> List[str]:
        ret_list = []
        curr_letter = ""
        curr_word = ""
        for w in s:
            if w == "'":
                curr_word += chr(int(curr_letter))
                curr_letter = ""
                continue
            if w == "|":
                ret_list.append(curr_word)
                curr_word = ""
                continue
            curr_letter += w
        return ret_list
