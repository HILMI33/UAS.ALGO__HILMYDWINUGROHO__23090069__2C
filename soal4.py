# Define the parent class Buah
class Buah:
    def init(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def Information(self):
        return f"Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}"
# Define the child class Mangga that inherits from Buah
class Mangga(Buah):
    def init(self, nama, warna, rasa, vitamin):
        super().init(nama, warna, rasa)
        self.vitamin = vitamin
    
    def setVitamin(self, vitamin):
        self.vitamin = vitamin
    
    def Information(self):
        parent_info = super().Information()
        return f"{parent_info}, Vitamin: {self.vitamin}"

# Create an instance of the child class Mangga
mangga = Mangga("Mangga Harum Manis"),