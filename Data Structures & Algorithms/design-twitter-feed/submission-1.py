from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.user_tweet = defaultdict(list)
        self.user_friend = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet[userId].append((tweetId , self.count))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        friends = [userId]  + list(self.user_friend[userId])
        for uid in friends:
            tweets = self.user_tweet[uid]
            i = len(tweets) - 1 # storing only last tweet
            if tweets:
                heapq.heappush(heap , (-tweets[i][1] , tweets[i][0] , uid , i))

        result = []
        while heap and len(result) <  10:
            count , tweetid , user , i = heapq.heappop(heap)
            result.append(tweetid)
            if i>0:
                i -= 1
                tweets = self.user_tweet[user]
                heapq.heappush(heap , (-tweets[i][1] , tweets[i][0] , user , i))

        return result


        # lst = self.user_tweet[userId][:]
        # for friend_tweet in self.user_friend[userId]:
        #     lst.extend(self.user_tweet[friend_tweet])
        # lst.sort(key = lambda x : x[1] , reverse = True)
        # return list(x[0] for x in lst)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.user_friend[followerId].add(followeeId)
        # self.user_friend[followeeId].append(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_friend[followerId].discard(followeeId)
        # self.user_friend[followeeId].remove(followerId)
