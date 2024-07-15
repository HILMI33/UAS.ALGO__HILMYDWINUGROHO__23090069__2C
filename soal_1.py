def input_mahasiswa():
    data_mahasiswa = []
    while True:
        nim = input("Masukan NIM anda: ")
        nama = input("Masukan Nama anda: ")
        data_mahasiswa.append({"NIM": nim, "Nama":nama})
        
        tambah_lagi = input("ingin tambah lagi? (ya/tidak): ").strip().lower()
        if tambah_lagi == 'tidak:':
          break
          return data_mahasiswa

def tampilkan_data(data_mahasiswa):
  print("Data Mahasiswa:")
  for mahasiswa in data_mahasiswa:
      print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")

def main():
    print("==== Program Input Data Mahasiswa ====")
    data_mahasiswa = input_mahasiswa()
    tampilkan_data(data_mahasiswa)
    print("==== Program selesai ====")

    if __name__ == "_main_":
      main()