from kurs import kurs

def konversi(dari, ke, jumlah):
    if dari == ke:
        return jumlah

    # IDR ke asing
    if dari == "IDR" and ke in kurs:
        return jumlah / kurs[ke]

    # asing ke IDR
    if ke == "IDR" and dari in kurs:
        return jumlah * kurs[dari]

    # asing ke asing
    if dari in kurs and ke in kurs:
        dalam_idr = jumlah * kurs[dari]
        return dalam_idr / kurs[ke]

    return None