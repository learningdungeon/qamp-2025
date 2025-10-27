from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def show(qc):
    sv = Statevector.from_instruction(qc)
    a, b = sv.data  # α, β
    x = 2*(a.conjugate()*b).real
    y = 2*(a.conjugate()*b).imag
    z = abs(a)**2 - abs(b)**2
    print("State:", sv)
    print(f"Bloch approx: x={x:.3f}, y={y:.3f}, z={z:.3f}")

# NE point: θ=π/2, φ=π/4
qc = QuantumCircuit(1)
qc.ry(3.14159265/2, 0)
qc.rz(3.14159265/4, 0)
show(qc)
