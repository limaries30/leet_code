"""
https://leetcode.com/problems/get-watched-videos-by-your-friends/
"""


class Solution:
    def watchedVideosByFriends(
        self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int
    ) -> List[str]:

        friend_info = {}
        visited = set()
        frequency_info = {}

        for idx, friend in enumerate(friends):
            friend_info[idx] = []
            for f in friend:
                friend_info[idx].append(f)

        q = deque([(id, 0)])
        visited.add(id)

        while len(q) > 0:

            friend_id, cnt = q.popleft()

            if cnt == level:
                for w in watchedVideos[friend_id]:
                    if w in frequency_info.keys():
                        frequency_info[w] += 1
                    else:
                        frequency_info[w] = 1
                continue

            for j in friend_info[friend_id]:
                if j not in visited:
                    visited.add(j)
                    q.append((j, cnt + 1))

        answer = []
        for res in frequency_info.keys():
            answer.append((res, frequency_info[res]))
        answer = sorted(answer, key=lambda x: (x[1], x[0]))
        answer = list(map(lambda x: x[0], answer))

        return answer
