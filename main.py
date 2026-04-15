# class node
class Anggota:
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.bawahan = []

# class struktur data
class Struktur:
    def __init__(self, nama_ketua):
        if nama_ketua:
            self.root = Anggota(nama_ketua, "Ketua Kelas")
        else:
            self.root = None

    def tampilkan_struktur(self, node=None, tingkat=0):
        if self.root is None:
            print("Struktur organisasi kosong.")
            return
            
        if node is None and tingkat == 0:
            node = self.root

        indentasi = "  " * tingkat + ("|_ " if tingkat > 0 else "")
        print(f"{indentasi}{node.nama} ({node.jabatan})")

        for bawahan in node.bawahan:
            self.tampilkan_struktur(bawahan, tingkat + 1)

    def cari_bawahan(self, node, nama_target):
        if node is None:
            return None
        if node.nama.lower() == nama_target.lower():
            return node
            
        for bawahan in node.bawahan:
            hasil = self.cari_bawahan(bawahan, nama_target)
            if hasil:
                return hasil
        return None

    def cari_parent(self, node, nama_target):
        if node is None:
            return None
        for bawahan in node.bawahan:
            if bawahan.nama.lower() == nama_target.lower():
                return node
            hasil = self.cari_parent(bawahan, nama_target)
            if hasil:
                return hasil
        return None

    def tambah_anggota(self, nama_atasan, nama_baru, jabatan_baru):
        atasan = self.cari_bawahan(self.root, nama_atasan)
        if atasan:
            anggota_baru = Anggota(nama_baru, jabatan_baru)
            atasan.bawahan.append(anggota_baru)
            print(f"Berhasil menambahkan {nama_baru} sebagai {jabatan_baru}.")
        else:
            print(f"Gagal: Atasan dengan nama '{nama_atasan}' tidak ditemukan!")

    def hapus_anggota(self, nama_target):
        if self.root is None:
            print("Struktur kosong.")
            return
            
        if self.root.nama.lower() == nama_target.lower():
            print("Peringatan: Tidak dapat menghapus Ketua Kelas dari sini!")
            return

        parent = self.cari_parent(self.root, nama_target)
        if parent:
            parent.bawahan = [b for b in parent.bawahan if b.nama.lower() != nama_target.lower()]
            print(f"Berhasil menghapus '{nama_target}' beserta seluruh bawahannya dari struktur.")
        else:
            print(f"Anggota dengan nama '{nama_target}' tidak ditemukan!")

    def cari_anggota(self, nama_target):
        hasil = self.cari_bawahan(self.root, nama_target)
        if hasil:
            print(f"\n===Data Anggota===")
            print(f"Nama    : {hasil.nama}")
            print(f"Jabatan : {hasil.jabatan}")
            if hasil.bawahan:
                print("Bawahan:")
                for b in hasil.bawahan:
                    print(f" - {b.nama} ({b.jabatan})")
            else:
                print("Status  : Tidak memiliki bawahan.")
        else:
            print("Anggota tidak ditemukan.")


#fungsi utama
def main():
    #contoh
    organisasi = Struktur("Andi")

    print("\n--- Struktur Organisasi Kelas ---")
    organisasi.tampilkan_struktur()
    while True:
        print(
            "========= Struktur Organisasi Kelas =========\n",
            "1. Tampilkan Struktur Organisasi\n",
            "2. Tambah Anggota\n",
            "3. Hapus Anggota\n",
            "4. Cari Anggota\n",
            "5. Simpan Struktur\n",
            "6. Load Struktur\n",
            "0. Keluar"
        )

        pilihan = input("Masukkan pilihan: ")

def simpan_file():
    ...

def buka_file():
    ...


if __name__ == "__main__":
    main()