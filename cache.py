from threading import Thread
import time

                
class Cache:
    def __init__(self, maxTime):
        self.__cachedData = {}
        self.__maxTime = maxTime
    def insert(self, keyword: str, datas):
        k = keyword.lower()
        if k not in self.__cachedData:
            self.__cachedData[k] = CacheData(k,datas,self.__maxTime,self)
            self.__cachedData[k].start()
    def remove(self,keyword: str):
        self.__cachedData.pop(keyword.lower(), None)
        print('Cache: removed data with key=',keyword)
    def getData(self,keyword: str):
        k = keyword.lower()
        if k not in self.__cachedData:
            return []
        return self.__cachedData[k].data
    def getAllData(self):
        return list(self.__cachedData.values())
            
class CacheData(Thread):
    def __init__(self, keywork, data,time, root: Cache):
        Thread.__init__(self)
        self.keywork = keywork
        self.data = data
        self.time = time
        self.root = root
    def run(self):
       time.sleep(self.time)
       self.root.remove(self.keywork)           
        


