import pandas as pd
import numpy as np

data = [
    ["Mahasiswa1",95, 85],
    ["Mahasiswa2",66, 70],
    ["Mahasiswa3",55, 60],
]
mata_kuliah = ["Nama","Algoritma dan struktur Data 2","Matematika Numeric"]

df = pd.DataFrame(data,columns=mata_kuliah)
               
rata_rata_mata_kuliah = df.mean(axis=0,numeric_only=True)
PendingDeprecationWarning("Rata-rata nilai untuksetiap mata kuliah:")
print(rata_rata_mata_kuliah)
df["Rata-rata"] = df.mean(axis=1, numeric_only=True)
rata_rata_mahasiswa = df[["Nama", "Rata-rata"]]
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(rata_rata_mahasiswa)           