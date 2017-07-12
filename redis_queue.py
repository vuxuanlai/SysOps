# Created by Peter Hoffmann

import redis
class RedisQueue(object):
    def __init__(self, name, namespace= 'queue', **redis_kwargs):
        self.__db = redis.Redis(**redis_kwargs)
        self.key = '%s:%s' %(namespace, name)
    
    # Size of queue
    def qsize(self):
        return self.__db.llen(self.key)
    
    # Put item into queue
    def put(self, item):
        self.__db.rpush(self.key, item)
    
    # Remove and return an item of the queue
    def get(self, block=True, timeout=None):
        if block:
            item = self.__db.blpop(self.key, timeout = timeout)
        else:
            item = self.__db.blpop(self.key)
            
        if item:
            item = item[1]
        return item
    
    # Equivalent to get(False)
    def get_nowait(self):
        return self.get(False)
