import heapq
from typing import List


class Twitter:
    def __init__(self):
        self.followMap = {}
        self.tweetMap = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followMap:
            self.followMap[userId] = {userId}
        currTweet = [self.count, userId, tweetId]
        self.count += 1
        if userId in self.tweetMap:
            self.tweetMap[userId].append(currTweet)
            return
        self.tweetMap[userId] = [currTweet]

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap:
            return []
        
        res = []
        maxHeap = []  # (count, userId, tweetId, index in tweetMap[userId])
        
        followees = self.followMap[userId]
        for followee in followees:
            if followee in self.tweetMap:
                tweets = self.tweetMap[followee]
                idx = len(tweets) - 1  # Most recent tweet
                count, _, tweetId = tweets[idx]
                heapq.heappush(maxHeap, (-count, followee, tweetId, idx))
        
        while maxHeap and len(res) < 10:
            negCount, followee, tweetId, idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            
            # Push next most recent tweet from this followee
            if idx > 0:
                tweets = self.tweetMap[followee]
                nextIdx = idx - 1
                count, _, nextTweetId = tweets[nextIdx]
                heapq.heappush(maxHeap, (-count, followee, nextTweetId, nextIdx))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].add(followeeId)
            return
        self.followMap[followerId] = {followerId, followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)
