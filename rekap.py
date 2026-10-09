import csv

# --- BAGIAN 1: MEMBACA DATA DARI CSV ---
# (Ini yang membuat variabel 'data' terdefinisi)
data = []
with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

# --- BAGIAN 2: MENGOLAH DATA ---
# (Sekarang kode di bawah ini bisa berjalan karena 'data' sudah ada isinya)

# Mencari rata-rata
rekap = {} 
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}") 
for k, v in sorted(rekap.items()): 
        rata = sum(v) / len(v) 
        print(f"{k:<6}{len(v):>8}{rata:>8.1f}")