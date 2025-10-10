# QC-PS1

Introduction 

This repository is created to provide the solution for the Problem Satement 1 given for the inductions of QC Club. Although the code block is written by me, I kept the basic functions same as that from the Qiskit to minimize confusion while running the program. Hope you like it! Just wanna share my experience, I just completed the theory and algos as well as completed the Section 1 by 3rd October. But because the deadline shifted to 10th, I decided to write the program another day. And here we are at 1 pm on 10th October and I am starting to write the program (Procrastination ftw) while the deadline is just 11 hours! Enough of this talk, Let's Start!!!

My Thought Process

After thinking for about half an hour in my today's English lecture, I got the idea of how to write the codes. The first thing to do was to define some important single qubit gates. So, I can not use numpy, I decided to construct the matrices by using lists in lists so form the gates. 

Now what's the next the thing to do? Ya, form multiple qubits from single qubis using Tensor Product. So, I created a function named tensor_product so that it can take two matrices and don their Tensor Product Thing. this expands two matrices into a block-matrix, the nested loops take every pair of rows and produce the element-wise products in the correct order. This is also useful to build full 2^n * 2^n operators from single qubit gates.

Now to apply these single qubit gates to a qubit, I formed a function named apply_gate to do the task. Sorry! After trying so hard, I did not get a single idea how to do that. So I had to get a code block from ChatGPT. (I promise I will replace it as soon as I understand it).

Now rather than defining the long CX, CY

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


