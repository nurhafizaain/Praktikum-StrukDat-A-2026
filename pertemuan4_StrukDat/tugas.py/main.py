from tabulate import tabulate
from kurs import kurs
from konverter import konversi

def format_rupiah(jumlah):
    return f"Rp {jumlah:,.0f}".replace(",", ".")

print("=== KONVERTER MATA UANG ===")

# Tabel Kurs
data_tabel = []
for kode, nilai in kurs.items():
    teks_kurs = f"{nilai:,}".replace(",", ".")  # 13360 -> 13.360 (string)
    data_tabel.append([kode, teks_kurs])

print(tabulate(
    data_tabel,
    headers=["Kode", "Kurs ke IDR"],
    tablefmt="grid",
    disable_numparse=True   # ← KUNCI AGAR TIDAK JADI 13.36
))

# Input
dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke  (IDR/USD/EUR/SGD/JPY): ").upper()
jumlah = float(input("Jumlah: "))

hasil = konversi(dari, ke, jumlah)

# Output
if hasil is None:
    print("Kode mata uang tidak valid!")
else:
    if dari == "IDR":
        print(f"\n{format_rupiah(jumlah)} = {hasil:.2f} {ke}")
    elif ke == "IDR":
        print(f"\n{jumlah:.2f} {dari} = {format_rupiah(hasil)}")
    else:
        print(f"\n{jumlah:.2f} {dari} = {hasil:.2f} {ke}")
