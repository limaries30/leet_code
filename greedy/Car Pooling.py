class Solution:
    """heap sort : O(NlogN)"""

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        transactions = []
        current_people = 0

        for trip in trips:
            heapq.heappush(transactions, (trip[1], trip[0]))
            heapq.heappush(transactions, (trip[2], -trip[0]))

        for i in range(2 * len(trips)):
            trip = heapq.heappop(transactions)
            current_people += trip[1]
            if current_people > capacity:
                return False
        return True


class Solution:
    """heap sort and end time : O(NlogN)"""

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        current_passengers = 0
        current = []
        trips.sort(key=lambda x: x[1])

        for trip in trips:
            while current and current[0][0] <= trip[1]:
                drop = heapq.heappop(current)
                current_passengers -= drop[1][0]
            current_passengers += trip[0]
            heapq.heappush(current, (trip[2], trip))
            if current_passengers > capacity:
                return False
        return True


class Solution:
    """hard coding"""

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        passengers = {}

        for trip in trips:
            for station in range(trip[1], trip[2]):
                if station not in passengers.keys():
                    passengers[station] = trip[0]
                else:
                    passengers[station] += trip[0]
                if passengers[station] > capacity:
                    return False

        return True