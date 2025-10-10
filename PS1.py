import math
import cmath

def tensor_product(a, b):
    result = []
    for row_1 in a:
        for row_2 in b:
            result.append([x * y for x in row_1 for y in row_2])
    return result

def apply_gate(state, gate, target, num_qubits):
    size = 2 ** num_qubits       
    new_state = [0] * size       

    for i in range(size):        
        bit = (i >> target) & 1  
        for j in range(2):       
            new_index = i ^ ((bit ^ j) << target)
            new_state[new_index] += gate[j][bit] * state[i]
    return new_state


def apply_cx(state, control, target, num_qubits):
    size = 2 ** num_qubits
    new_state = state[:]
    for i in range(size):
        if (i >> control) & 1: 
            flipped = i ^ (1 << target)
            new_state[flipped] = state[i]
            new_state[i] = state[flipped]
    return new_state

def apply_cy(state, control, target, num_qubits):
    import cmath
    size = 2 ** num_qubits
    new_state = state[:]
    for i in range(size):
        if (i >> control) & 1: 
            bit = (i >> target) & 1  
            flipped = i ^ (1 << target) 
            if bit == 0:
                new_state[flipped] += 1j * state[i]  
                new_state[i] = 0
            else:
                new_state[flipped] += -1j * state[i] 
                new_state[i] = 0
    return new_state

def apply_cz(state, control, target, num_qubits):
    size = 2 ** num_qubits
    new_state = state[:]
    for i in range(size):
        if ((i >> control) & 1) and ((i >> target) & 1):  
            new_state[i] = -state[i]  
    return new_state


# Defining useful gates

H = [[1 / math.sqrt(2), 1 / math.sqrt(2)],
     [1 / math.sqrt(2), -1 / math.sqrt(2)]]

X = [[0, 1],
     [1, 0]]
Y = [[0, -1j],
     [1j, 0]]
Z = [[1, 0],
     [0, -1]]

S = [[1, 0],
     [0, 1j]]


class QuantumCircuit:
    def init(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = [0] * (2 ** num_qubits)
        self.state[0] = 1 
        
    def apply(self, gate, target):
        self.state = apply_gate(self.state, gate, target, self.num_qubits)

    def apply_cx(self, control, target):
        self.state = apply_cx(self.state, control, target, self.num_qubits)
    
    def measure(self):
        print("Final statevector:")
        for i, amp in enumerate(self.state):
            print(f"|{format(i, f'0{self.num_qubits}b')}> : {amp:.3f}")

if __name__ == "__main__":
    qc = QuantumCircuit(2)
    qc.apply(H, 0)      # Apply Hadamard to qubit 0
    qc.cx(0, 1)         # Apply CNOT (control=0, target=1)
    qc.measure()

