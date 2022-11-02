
memory_size = 16


class Memory:
    #Internal memory implemented as dictionary (Address: value)
    def __init__(self) -> None:
        self.memory={}
    
    def search_memory(self, address):
        if address in self.memory:
            return self.memory[address]
        return None

    def write_memory(self, address, value):
        self.memory[address]= value

    def get_value(self, address):
        return self.memory[address]
 