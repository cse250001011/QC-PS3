# QC-PS1

Introduction 
This repository is created to provide the solution for the Problem Satement 1 given for the inductions of QC Club

How the program Works?

Step 1: You have to initialise the circuit by specifying the number of qubits the quantum state has.

Example :
qc = QuantumCircuit(2)

Step 2: Apply single gates like H to specified qubits.
Example :
qc.apply(H, 0)   
This applies the Hadamard gate to the qubit zero 

Step 3: Apply controlled gates of your choice like CNOT gate
Example : 
qc.cx(0, 1)       
This applies the CNOT gate where the control qubit is 0 and the target quibit is 1

Step 4: Measure the resultant statevector
Example :
qc.measure()


