class Solution:

    def encode(self, strs: List[str]) -> str:
        length = len(strs)
        if length == 0:
            return None
        if length != 0 and not strs:
            return strs[0]
        else:
            an = strs[0]
            for i in strs[1:]:
                an += f'decoded_sheesh{i}'
            return an 

    def decode(self, s: str) -> List[str]:
        if s:
            return s.split('decoded_sheesh') 
        if s in ['', ""]:
            return [s]
        return []
