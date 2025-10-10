# QC-PS1

Introduction 

This repository is created to provide the solution for the Problem Satement 1 given for the inductions of QC Club. Although the code block is written by me, I kept the basic functions same as that from the Qiskit to minimize confusion while running the program. Hope you like it! Just wanna share my experience, I just completed the theory and algos as well as completed the Section 1 by 3rd October. But because the deadline shifted to 10th, I decided to write the program another day. And here we are at 1 pm on 10th October and I am starting to write the program (Procrastination ftw) while the deadline is just 11 hours! Enough of this talk, Let's Start!!!

My Thought Process

The first thing to write in the program was to

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


