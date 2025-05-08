from qiskit import Aer
from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance

#provider = IBMProvider(token="46cdfd219d4bb6e73b66ae218c9ebd407a20a4ebbd9e40359c136f8e463b5f66b12e08607210b1cd0f75b14df58ed177da2eb030f2269d6dd7505e1ca303ab49")
#backend  = provider.get_backend("ibmq_qasm_simulator")


backend = Aer.get_backend("aer_simulator")
qi = QuantumInstance(backend, shots=1024)
shor = Shor(quantum_instance=qi)
N=21
result = shor.factor(N)
print("Factorii lui",N, "sunt:", result.factors)

