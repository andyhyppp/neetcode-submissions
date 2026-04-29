import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.user_posts = defaultdict(list)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        # O(1)
        # Store (timestamp, tweetId) so we can sort by time
        self.time += 1
        self.user_posts[userId].append((self.time, tweetId))
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # We only need the 10 most recent tweets per followee.
        # F = number of followees + 1
        min_heap = []
        for uid in self.following[userId] | {userId}:
            posts = self.user_posts[uid]
            # look at only the last 10 tweets from this user
            for ts, tid in posts[-10:]:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, (ts, tid))
                else:
                    # if this tweet is newer than the oldest in heap, replace it
                    if ts > min_heap[0][0]:
                        heapq.heapreplace(min_heap, (ts, tid))
        
        # now heap contains the 10 newest tweets by timestamp
        # extract them into a list ordered most-recent first
        res = [tid for (_ts, tid) in heapq.nlargest(10, min_heap)]
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        # O(1)
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # O(1)
        self.following[followerId].discard(followeeId)
