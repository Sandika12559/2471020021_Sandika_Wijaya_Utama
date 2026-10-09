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
nilai = [d["nilai"] for d in data] 
rata = sum(nilai) / len(nilai) 
print(f"Rata-rata: {rata:.1f}") 

lulus = [d["nama"] for d in data
         if d["nilai"] >= 75]
print("Lulus:", lulus) 

top = max(data, key=lambda d: d["nilai"]) 
print("Tertinggi:", top["nama"])