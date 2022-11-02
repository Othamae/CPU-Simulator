
from cache import Cache
from memory import Memory



#Helper function to get the address from instructions. For example for R3 the function will return 3
def reg_inx(register):    
    return int(register[1:])

class CPU:
    #CPU implemented with internal memory and cache memory.
    def __init__(self) -> None:        
        self.cache = Cache()
        self.memory = Memory()
        self.counter = 0
        self.cache_on = True

    
    def print_memory(self):
        for address, value in self.memory.memory.items():
            print("Address: ", address , " Value: ", value)

    def print_cache(self):
        for address, value in self.cache.cache_memory.items():
            print("Address: ", address , " Value: ", value)

    def search_cache(self, address):
        return self.cache.search_cache(address)

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    def search_memory(self, address):
        return self.memory.search_memory(address)
    
    def write_memory(self, address, value):
        self.memory.write_memory(address, value)

    def set_counter(self, value):
        self.counter= value

    def get_counter(self):
        return self.counter
    
    def reset_counter(self):
        self.counter = 0

    def increase_counter(self):
        self.counter+=1

    def set_cache_on(self):
        self.cache_on = True
    
    def set_cache_off(self):
        self.cache_on = False

    def search_value(self, address):
        a_value= self.search_cache(reg_inx(address))          
        while a_value == None:
            a_mem_value = self.search_memory(reg_inx(address))
            self.write_cache(reg_inx(address),a_mem_value)
            a_value= self.search_cache(reg_inx(address))

    # parsing instructions 
    def instruction(self, instructions):
        print("Instruction: " +instructions)
        self.increase_counter()
        inst = instructions.split(',')                
        if inst[0] == 'ADD':
            self.ADD(inst[1], inst[2], inst[3])
        if inst[0] == 'ADDI':
            self.ADDI(inst[1], inst[2], inst[3])
        if inst[0] == 'J':
            self.J(inst[1])
        if inst[0] == 'CACHE':
            self.CACHE(inst[1])


    # instructions functions    
    def ADD(self, destination, source1, source2):        
        if self.cache_on:
            self.search_value(destination)
            self.search_value(source1)
            self.search_value(source2)        
        self.write_memory(reg_inx(destination), int(self.search_cache(reg_inx(source1)) + self.search_cache(reg_inx(source2)))) 
        self.write_cache(reg_inx(destination), int(self.search_cache(reg_inx(source1)) + self.search_cache(reg_inx(source2))))  
        print("Register ", destination, "has been updated.")
        print("New value: ", self.memory.get_value(reg_inx(destination)))
  


    def ADDI(self, destination, source, constant):
        if self.cache_on:
            self.search_value(destination)
            self.search_value(source)
        self.write_memory(reg_inx(destination), int(self.search_cache(reg_inx(source)) + int(constant))) 
        self.write_cache(reg_inx(destination), int(self.search_cache(reg_inx(source)) + int(constant)))
        print("Register ", destination, "has been updated.")
        print("New value: ", self.memory.get_value(reg_inx(destination)))
  
        

    def J(self, counter):
        self.counter = int(counter)
    
    def CACHE(self, value):
        if int(value) == 0:
            self.set_cache_off()
            print("Cache is OFF")
        if int(value) == 1:
            self.set_cache_on()
            print("Cache is ON")
        if int(value) == 2:
            self.cache.clean_cache()
            print("Cache has been reseted")

