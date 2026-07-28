from collections import defaultdict
class Solution:
    """
    dict = {}
    patterns[pattern] = [username], score 
    users[joe] = [home, about, career]
    pattern[(home, about, career)] = [joe]
    users[james] = [home, cart, maps, home]
    pattern[(home, cart, maps)] = [james], 1
    pattern[(home, cart, home)] = [james], 1
    pattern[(cart, maps, home)] = [james], 1
    pattern[(home, maps, home)] = [james], 1
    
    """
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        all_ = [(t, u, w) for u, t, w in zip(username, timestamp, website)]
        all_ = sorted(all_)
        timestamp, username, website = zip(*all_) #onlogn
        
        #print(timestamp, username, website)
        
        users = defaultdict(list)
        for u, w in zip(username, website):
            users[u].append(w)
            
        patterns = self.generate_patterns(users)
        
        #max_pair = [(), []]
        pairs = []
        for pattern, users in patterns.items():
            pairs.append((-len(users), pattern))
            # if len(users) > len(max_pair[1]):
            #     max_pair = [pattern, users]

        pairs.sort()
        #print(pairs)
        
        return pairs[0][1]
        
    def generate_patterns(self, users: Dict[str, List[str]]) -> dict:
        patterns = defaultdict(list)
        for u, l_w in users.items():
            combinations = self.aux_generate_patterns(l_w)
            for pattern in combinations:
                patterns[pattern].append(u)
                
        return patterns
    
    def aux_generate_patterns(self, websites: List[str]) -> Set[Tuples[str, str, str]]:
        N = len(websites)
        i = 0
        if N < 3:
            return []
        
        combinations = set()
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    combinations.add((websites[i], websites[j], websites[k]))
        
        return combinations