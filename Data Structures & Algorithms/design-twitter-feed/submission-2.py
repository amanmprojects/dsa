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
        followees = self.followMap[userId]
        allTweets = []
        for followee in followees:
            if followee in self.tweetMap:
                allTweets += self.tweetMap[followee]

        heapq.heapify(allTweets)

        return [tweet[2] for tweet in heapq.nlargest(10, allTweets, key=lambda x: x[0])]

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
