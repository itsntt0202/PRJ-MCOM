"""
PRJ-MCOM: Automated QPSK BER Sweep Testbed over AWGN Channel
Course: 61ECE314 — Mobile Communications (VGU)
Task: MCOM-04 (GATE-3 Deliverable) | Author: Thuy Tien
"""

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt


# Block 1: Gray-mapped QPSK modulator (Es = 1)
def qpsk_modulate(bits):
    b_I = bits[0::2]
    I = (1 - 2 * b_I) / np.sqrt(2)

    b_Q = bits[1::2]
    Q = (1 - 2 * b_Q) / np.sqrt(2)

    symbols = I + 1j * Q
    return symbols


# Block 2: AWGN channel with target Eb/N0 in dB
def add_awgn_noise(symbols, eb_n0_db):
    eb_n0_lin = 10.0 ** (eb_n0_db / 10.0)

    # Physical parameters: Es = 1, 2 bits/symbol => Eb = 0.5
    Es = 1.0
    bits_per_symbol = 2
    Eb = Es / bits_per_symbol

    # Noise power spectral density N0 and standard deviation sigma per axis
    N0 = Eb / eb_n0_lin
    sigma = np.sqrt(N0 / 2.0)

    # Generate complex Gaussian noise
    noise_I = sigma * np.random.randn(len(symbols))
    noise_Q = sigma * np.random.randn(len(symbols))
    noise = noise_I + 1j * noise_Q

    rx_symbols = symbols + noise
    return rx_symbols


# Block 3: Hard-decision coherent QPSK demodulator (Decision Slicer)
def qpsk_demodulate(rx_symbols):
    # Threshold slicing at 0: > 0 is bit 0, <= 0 is bit 1
    b_I_hat = (rx_symbols.real < 0).astype(int)
    b_Q_hat = (rx_symbols.imag < 0).astype(int)

    # Recombine bits into original bitstream
    rx_bits = np.zeros(2 * len(rx_symbols), dtype=int)
    rx_bits[0::2] = b_I_hat
    rx_bits[1::2] = b_Q_hat
    return rx_bits


# Block 4: Monte Carlo simulation point
def simulate_qpsk_ber(eb_n0_db, num_bits=500000):
    tx_bits = np.random.randint(0, 2, num_bits)
    tx_symbols = qpsk_modulate(tx_bits)
    rx_symbols = add_awgn_noise(tx_symbols, eb_n0_db)
    rx_bits = qpsk_demodulate(rx_symbols)

    bit_errors = int(np.sum(tx_bits != rx_bits))
    ber = bit_errors / num_bits
    return ber, bit_errors


# Main sweep execution and validation plot
if __name__ == '__main__':
    print("==========================================================================")
    print("  PRJ-MCOM GATE-3: AUTOMATED QPSK BER SWEEP TESTBED (AWGN CHANNEL)       ")
    print("==========================================================================")

    # Sweep parameters: Eb/N0 from 0 to 10 dB in 2 dB steps
    eb_n0_db_range = np.array([0, 2, 4, 6, 8, 10])
    num_bits_per_point = 500000
    empirical_ber = []

    print(f"\n[INFO] Starting Monte Carlo sweep with {num_bits_per_point:,} bits per point...")
    print("--------------------------------------------------------------------------")
    print("|  Eb/N0 (dB)  |  Transmitted Bits  |   Bit Errors   |     Measured BER     |")
    print("--------------------------------------------------------------------------")

    for eb_n0 in eb_n0_db_range:
        ber, errors = simulate_qpsk_ber(eb_n0, num_bits=num_bits_per_point)
        empirical_ber.append(ber)
        print(f"|    {eb_n0:5.1f}     |     {num_bits_per_point:9,d}      |     {errors:6d}     |     {ber:13.6e}    |")

    print("--------------------------------------------------------------------------")

    # Theoretical closed-form benchmark curve
    eb_n0_fine_db = np.linspace(0, 10, 150)
    eb_n0_fine_lin = 10.0 ** (eb_n0_fine_db / 10.0)
    theoretical_ber = 0.5 * sp.erfc(np.sqrt(eb_n0_fine_lin))

    # Plotting validation curves (Theory vs Empirical)
    print("\n[INFO] Plotting validation curves (Theory vs Empirical)...")
    plt.figure(figsize=(9, 6.5))

    plt.semilogy(
        eb_n0_fine_db, 
        theoretical_ber, 
        'b-', 
        linewidth=2, 
        label=r'QPSK Theory: $P_b = Q(\sqrt{2E_b/N_0})$'
    )

    plt.semilogy(
        eb_n0_db_range, 
        empirical_ber, 
        'ro', 
        markersize=7, 
        label='Empirical Simulation (Monte Carlo)'
    )

    plt.title('Bit Error Rate (BER) of QPSK over AWGN Channel', fontsize=13, fontweight='bold')
    plt.xlabel(r'$E_b/N_0$ (dB)', fontsize=11)
    plt.ylabel('Bit Error Rate (BER)', fontsize=11)
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.ylim([1e-5, 1.0])
    plt.xlim([-0.5, 10.5])
    plt.legend(fontsize=11, loc='upper right')
    plt.tight_layout()

    # Save output deliverables
    png_path = 'awgn_ber_qpsk.png'
    pdf_path = 'awgn_ber_qpsk.pdf'
    plt.savefig(png_path, dpi=300)
    plt.savefig(pdf_path)
    plt.close()

    print("[SUCCESS] Deliverables generated successfully:")
    print(f"  -> Raster Image (Presentation & Slides): {png_path}")
    print(f"  -> Vector Graphic (IEEE XeLaTeX Report):  {pdf_path}")
    print("==========================================================================")