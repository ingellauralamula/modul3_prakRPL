import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Menghubungkan tombol dengan fungsi Controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_update.configure(
            command=self.perbarui_data
        )
        self.view.btn_delete.configure(
            command=self.hapus_data
        )

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model
        data_buku = self.model.get_all_buku()

        # Menampilkan data ke tabel
        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def simpan_data(self):
        # Mengambil input dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Validasi input
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_buku(
            judul, penulis, tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )

            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Terjadi kesalahan saat menyimpan data."
            )

    def hapus_data(self):
        # Mengambil baris yang dipilih
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin dihapus!"
            )
            return

        # Mengambil ID buku
        item = self.view.tabel.item(selected[0])
        id_buku = item["values"][0]

        # Meminta konfirmasi
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus data buku ini?"
        )

        if not konfirmasi:
            return

        # Menghapus data melalui Model
        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data buku gagal dihapus!"
            )

    def perbarui_data(self):
        # Mengambil baris yang dipilih
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data buku yang ingin diperbarui!"
            )
            return

        # Mengambil ID buku
        item = self.view.tabel.item(selected[0])
        id_buku = item["values"][0]

        # Mengambil data baru dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Validasi input
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        # Memperbarui data melalui Model
        berhasil = self.model.update_buku(
            id_buku, judul, penulis, tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data buku gagal diperbarui!"
            )

    def bersihkan_form(self):
        # Mengosongkan semua kolom input
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

    def run(self):
        # Menjalankan aplikasi
        self.view.mainloop()
