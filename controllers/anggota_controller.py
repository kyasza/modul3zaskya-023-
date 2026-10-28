import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Saat baris tabel diklik, form terisi otomatis
        self.view.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_tabel)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data baru ke dalam tabel View
        # "or ''" supaya data kosong (NULL) tampil kosong, bukan "None"
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'] or "", anggota['alamat'] or ""))

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def ambil_id_terpilih(self):
        """Ambil id_anggota dari baris tabel yang diklik. Jika tidak ada, kembalikan None."""
        pilihan = self.view.tabel.selection()
        if not pilihan:
            return None
        return self.view.tabel.item(pilihan[0])['values'][0]

    def isi_form_dari_tabel(self, event=None):
        pilihan = self.view.tabel.selection()
        if not pilihan:
            return
        nilai = self.view.tabel.item(pilihan[0])['values']
        self.bersihkan_form()
        self.view.entry_nama.insert(0, nilai[1])
        self.view.entry_alamat.insert(0, nilai[2])

    def simpan_data(self):
        # Mengambil teks dari kotak input di View
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        # Validasi Form Kosong
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def perbarui_data(self):
        id_anggota = self.ambil_id_terpilih()
        if id_anggota is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris yang mau diperbarui!")
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_anggota(id_anggota, nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        id_anggota = self.ambil_id_terpilih()
        if id_anggota is None:
            messagebox.showwarning("Peringatan", "Pilih dulu baris yang mau dihapus!")
            return

        if not messagebox.askyesno("Konfirmasi", "Yakin mau menghapus data ini?"):
            return

        if self.model.delete_anggota(id_anggota):
            messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()