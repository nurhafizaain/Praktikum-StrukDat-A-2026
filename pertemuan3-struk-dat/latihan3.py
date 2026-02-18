class Person:
    def __init__(self, nama, jenis_kelamin, umur):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin 
        self.umur = umur

    def printnama(self):
        print("Nama:", self.nama)
        print("Jenis Kelamin:", self.jenis_kelamin)
        print("Umur:", self.umur)


class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, umur, gaji):
            super().__init__(nama, jenis_kelamin, umur)
            self.__gaji = gaji

    def set_gaji(self, gaji):
        if 0 <= gaji <= 5000000:
            self.__gaji = gaji
        else:
            print("gaji must be between 0 and 5000000")

    def get_gaji(self):
             return self.__gaji
    
    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("Jenis Kelamin:", self. jenis_kelamin)
        print("Umur:", self.umur)
        print("Gaji:", self.__gaji)
        
class Rekening:
    def __init__(self, No_Rekening, pin):
        self.No_Rekening = No_Rekening
        self.__pin = pin

    def get_pin(self):
        return self.__pin

# Objek Person
p1 = Person("Hafiza", "Perempuan", 19)

# Objek Karyawan
k1 = Karyawan("Ain", "Perempuan", 19, 3000000)

# Objek Rekening
r1 = Rekening("123456789", 1234)

print("Nama Person")
p1.printnama()


print("Nama Karyawan")
k1.tampilkan_data()

print("No Rekening:", r1.No_Rekening)
print("PIN:", r1.get_pin())

    