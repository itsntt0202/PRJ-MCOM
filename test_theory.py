import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#Create Eb/N0 from 0 to 10 dB
eb_n0_db = np.linspace(0, 10, 50)

#Change dB into linear
eb_n0_lin = 10 ** (eb_n0_db / 10)

#Calculate BER base on the formula QPSK AWGN
ber_theory = 0.5 * sp.erfc(np.sqrt(eb_n0_lin))

#Plot the semilogy
plt.figure(figsize=(8, 6))
plt.semilogy(eb_n0_db, ber_theory, 'b-', linewidth=2, label='QPSK Theory: $P_b = Q(\\sqrt{2E_b/N_0})$')
plt.title('Theoretical BER for QPSK over AWGN Channel', fontsize=13)
plt.xlabel('$E_b/N_0$ (dB)', fontsize=11)
plt.ylabel('Bit Error Rate (BER)', fontsize=11)
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.ylim([1e-5, 1.0])
plt.legend(fontsize=11)

plt.tight_layout()
plt.savefig('test_theory.png', dpi=300)