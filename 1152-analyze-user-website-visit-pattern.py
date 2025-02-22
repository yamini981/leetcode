class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # could reorganize data into key: user --> value: websites visited (ordered)
        combined = list(zip(timestamp, website, username))
        combined.sort()
        userToWebsite = defaultdict(list)
        for t, w, u in combined:
            userToWebsite[u].append(w)


        patterns = Counter()
        
        for user, sites in userToWebsite.items():
            patterns.update(Counter(set(combinations(sites, 3))))
                    
        
        return max(sorted(patterns), key = patterns.get) 


                    
