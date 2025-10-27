from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(1,1)
qc.h(0); qc.rz(3.14159265, 0); qc.h(0)
sv = Statevector.from_instruction(qc)
print("State:", sv)  # proportional to |−>
qc.measure(0,0)
print(qc)
