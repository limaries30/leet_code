'''
https://leetcode.com/problems/design-underground-system/
defaultdict 활용!
'''
class UndergroundSystem:

    def __init__(self):
        self.info = {}
        self.traveling = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.traveling[id]=(stationName,t)
        if stationName not in self.info.keys():
            self.info[stationName] ={}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        checkin_station,time = self.traveling[id]
        elapsed_time = t - time
        if stationName not in self.info[checkin_station].keys():

            self.info[checkin_station][stationName] = {}
            current_info = self.info[checkin_station][stationName]
            current_info['time'] = elapsed_time
            current_info['num'] =1 
        else:
            current_info = self.info[checkin_station][stationName]
            current_info['time'] += (elapsed_time- current_info['time'])/(current_info['num']+1)
            current_info['num'] +=1 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.info[startStation][endStation]['time']

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)