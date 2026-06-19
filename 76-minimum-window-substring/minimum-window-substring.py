class Solution:
    from collections import defaultdict
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        N = len(t)
        M = len(s)
        minw = s
        t_dict = Counter(t)
        s_dict = Counter(s)
        
        if N > M or not t_dict <= s_dict:
            return ""
        left = 0
        right = left + N
        sub = s[left: right]
        sub_dict = Counter(sub)
        while left <= M - N and right <= M:
            
            if t_dict <= sub_dict:
                if len(sub) < len(minw):
                    minw = sub
                sub_dict[s[left]] -= 1 
                left += 1
                
            else:
                if right < M:
                    sub_dict[s[right]] += 1 
                right += 1
                
            sub = s[left: right]
        return minw

    # def create_dict(self, string: str) -> dict:
    #     char_dict = defaultdict(int)
    #     for character in string:
    #         char_dict[character] += 1
        
    #     return char_dict
    
    # def compare_dicts(self, t: dict, slice_: dict) -> bool:
    #     for k, v in t.items():
    #         slice_value = slice_.get(k, -float('inf'))
    #         if slice_value < t[k]:
    #             return False
    #     return True


