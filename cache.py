import collections


cache_size = 4

class Cache:
    #Cache created as dictionary(Address: data)
    #Queue implemented for a FIFO cache and limit the size of the cache
    def __init__(self) -> None:  
        self.cache_memory={} 
        self.cache_mem_cola = collections.deque(self.cache_memory, cache_size) 

    def write_cache(self, address, value):
        if address not in self.cache_mem_cola: 
            if self.is_full():  
                self.cache_memory.pop(self.cache_mem_cola.popleft())                  
            self.cache_mem_cola.append(address)
        self.cache_memory[address] = value
        
        
    def print_cache(self):
        print("CACHE ACTUAL")
        for address, value in self.cache_memory.items():
            print("Address: ", address , " Value: ", value)
        print("Cola Actual")
        for i in self.cache_mem_cola:
            print(i)

    def search_cache(self, address):
        if address in self.cache_memory:
            return self.cache_memory[address]
        return None 

    def is_full(self):
        if len(self.cache_mem_cola)== cache_size:
            return True
        return False        

    def clean_cache(self):
        self.cache_memory.clear()
        self.cache_mem_cola.clear()
        print('Cache has been cleared')
