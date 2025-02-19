class Twitter:
    # I'm thinking each user has a list (stack) of 
    # tweetIDs. I'm assuming userIDs are also unique
    # so we'd have a hashtable of users to their tweet IDs for one thing
    # rather than just tweet ID, we'll do (tweetID, timeStamp) - like logical clock
    
    
    def __init__(self):
        self.time = 0
        self.userToTweets = defaultdict(list)
        self.userToFollowing = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.userToTweets[userId]) == 10:
            self.userToTweets[userId].pop(0)
        self.userToTweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # iterate through each followed account, and whichever one has the lowest
        # timestamp at the end, append into to the newsFeed
        newsFeed = []
        followedAccounts = list(self.userToFollowing[userId])
        followedAccounts.append(userId)
        indexToCheck = [-1] * len(followedAccounts)
        while len(newsFeed) < 10:
            highestTimestamp = -1
            bestTweetId = -1
            accountOfBestTweet = -1
            for i in range(len(followedAccounts)):
                followedAccount = followedAccounts[i]
                # if the followed account has tweets left to check AND 
                # if the followedAccount's tweet is the latest one
                if (abs(indexToCheck[i]) <= len(self.userToTweets[followedAccount]) and
                    self.userToTweets[followedAccount][indexToCheck[i]][1] > highestTimestamp):
                    

                    bestTweetId = self.userToTweets[followedAccount][indexToCheck[i]][0]
                    highestTimestamp = self.userToTweets[followedAccount][indexToCheck[i]][1]
                    accountOfBestTweet = i
            
            if accountOfBestTweet == -1:
                break
            newsFeed.append(bestTweetId)
            indexToCheck[accountOfBestTweet] -= 1
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollowing[followerId]:
            self.userToFollowing[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)