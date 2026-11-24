"""
Kiem tra ly thuyet BER cho dieu che QPSK tren kenh AWGN
Mon hoc: Mobile Communications (61ECE314) - VGU
Nguoi thuc hien: Thuy Tien
"""

import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

def run_theory_test():
    print("==========================================================")
    print("  KHOI DONG KIEM TRA DUONG CONG LY THUYET BER - QPSK AWGN")
    print("==========================================================")

    # 1. Tao dai Eb/N0 tu 0 den 10 dB
    eb_n0_db = np.linspace(0, 10, 50)
    print(f"[1] Da tao dai Eb/N0 gom {len(eb_n0_db)} diem tu {eb_n0_db[0]:.1f} dB den {eb_n0_db[-1]:.1f} dB.")

    # 2. Doi sang ty so tuyen tinh
    eb_n0_lin = 10.0 ** (eb_n0_db / 10.0)

    # 3. Tinh BER ly thuyet: Pb = 0.5 * erfc(sqrt(Eb/N0))
    ber_theory = 0.5 * sp.erfc(np.sqrt(eb_n0_lin))

    # In ra mot vai diem mau de kiem tra gia tri
    print("\n[2] Bang mau mot so diem kiem tra tinh dung dan:")
    print("----------------------------------------------------------")
    print(f"|  Eb/N0 (dB)  |   Eb/N0 (tuyen tinh)   |     BER ly thuyet     |")
    print("----------------------------------------------------------")
    sample_indices = [0, 10, 20, 30, 40, 49]
    for idx in sample_indices:
        db = eb_n0_db[idx]
        lin = eb_n0_lin[idx]
        ber = ber_theory[idx]
        print(f"|    {db:5.2f}     |        {lin:7.3f}         |     {ber:13.6e}     |")
    print("----------------------------------------------------------")

    # 4. Ve do thi chuan ban logarit (semilogy)
    print("\n[3] Dang ve do thi semilogy va xuat file anh...")
    plt.figure(figsize=(8, 6))
    plt.semilogy(eb_n0_db, ber_theory, 'b-', linewidth=2, label=r'QPSK Theory: $P_b = Q(\sqrt{2E_b/N_0})$')

    plt.title('Theoretical BER for QPSK over AWGN Channel', fontsize=13)
    plt.xlabel(r'$E_b/N_0$ (dB)', fontsize=11)
    plt.ylabel('Bit Error Rate (BER)', fontsize=11)
    plt.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.ylim([1e-5, 1.0])
    plt.legend(fontsize=11)

    output_path = 'test_theory.png'
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"[OK] Hoan tat! Da luu file do thi thanh cong tai: {output_path}")

if __name__ == '__main__':
    run_theory_test()
