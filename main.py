
from cpu import CPU

instruction_file = "instruction_input.txt"
data_file = "data_input.txt"


def upload_memory(cpu, file):
    d_file = open(file, 'r')
    data = d_file.readlines()
    data = list(map(lambda s: s.strip(), data))    
    for r in data:
        d = r.split(',')
        cpu.write_memory(int(d[0],2), int(d[1]))
    print("Data loaded in Memory")

def send_instructions(cpu, file):
    i_file = open(file, 'r')
    inst = i_file.readlines()
    inst = list(map(lambda s: s.strip(), inst))
    for i in inst:
        cpu.instruction(i)
        


my_cpu = CPU()

print("---------------------------------------------------")
print("Welcome to the CPU Simulator!")
print("---------------------------------------------------")
print("Initializing Memory from data input file...")
upload_memory(my_cpu,data_file)
print("---------------------------------------------------")
print("Sending instructions to CPU...")
send_instructions(my_cpu, instruction_file)
print("---------------------------------------------------")
print("Terminating CPU Processing...")

        
