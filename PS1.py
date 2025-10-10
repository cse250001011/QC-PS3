import math
import cmath

def tensor_product(a, b):
    result = []
    for row_a in a:
        for row_b in b:
            result.append([x * y for x in row_a for y in row_b])
    return result

def apply_gate(state, gate, target, num_qubits):
    """Applies a single-qubit gate on target qubit."""
    size = 2 ** num_qubits
    new_state = [0] * size
    for i in range(size):
        bit = (i >> target) & 1
        for j in range(2):
            new_index = (i & ~(1 << target)) | (j << target)
            new_state[new_index] += gate[j][bit] * state[i]
    return new_state

def apply_cx(state, control, target, num_qubits):
    """Applies a CX (CNOT) gate."""
    size = 2 ** num_qubits
    new_state = state[:]
    for i in range(size):
        if (i >> control) & 1:  # if control qubit = 1
            flipped = i ^ (1 << target)
            new_state[flipped] = state[i]
            new_state[i] = state[flipped]
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
        self.state[0] = 1  # start in |00...0>
    
    def apply(self, gate, target):
        self.state = apply_gate(self.state, gate, target, self.num_qubits)

    def apply_cx(self, control, target):
        self.state = apply_cx(self.state, control, target, self.num_qubits)
    
    def measure(self):
        print("Final statevector:")
        for i, amp in enumerate(self.state):
            print(f"|{format(i, f'0{self.num_qubits}b')}> : {amp:.3f}")

# ---------- Example Usage ----------

qc = QuantumCircuit(2)
qc.apply(H, 0)          # Apply Hadamard on qubit 0
qc.apply_cx(0, 1)       # Apply CNOT with qubit 0 as control
qc.measure()
