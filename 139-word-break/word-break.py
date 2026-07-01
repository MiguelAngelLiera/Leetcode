class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        mem = [False]*(N+1)
        mem[0] = True
        for idx, i in enumerate(range(N-1, -1, -1)):
            j = i + 1
            while s[i:j] not in wordDict and j < N or not mem[idx+1-(j-i)] :
                j += 1
                # if s[i:j] in wordDict and not mem[idx+1-(j-i)]:
                #     break
            # print(s[i:j])
            if s[i:j] not in wordDict:
                mem[idx+1] = False
            else:
                # print(s[i:j], mem[idx+1-(j-i)])
                mem[idx+1] = True and mem[idx+1-(j-i)]
                
        # print(mem)
        return mem[-1]
                
            
        