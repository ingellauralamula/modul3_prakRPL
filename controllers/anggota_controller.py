
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

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

        # Memuat data anggota saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data anggota dari Model
        data_anggota = self.model.get_all_anggota()

        # Menampilkan data ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def simpan_data(self):
        # Mengambil data dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Memeriksa form kosong
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan!"
            )

    def hapus_data(self):
        # Mengambil baris yang dipilih
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin dihapus!"
            )
            return

        # Mengambil ID anggota
        item = self.view.tabel.item(selected[0])
        id_anggota = item["values"][0]

        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Yakin ingin menghapus anggota ini?"
        )

        if not konfirmasi:
            return

        # Menghapus data melalui Model
        berhasil = self.model.delete_anggota(id_anggota)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal dihapus!"
            )

    def perbarui_data(self):
        # Mengambil baris yang dipilih
        selected = self.view.tabel.selection()

        if not selected:
            messagebox.showwarning(
                "Peringatan",
                "Pilih anggota yang ingin diperbarui!"
            )
            return

        # Mengambil ID anggota
        item = self.view.tabel.item(selected[0])
        id_anggota = item["values"][0]

        # Mengambil data baru dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        # Memperbarui data melalui Model
        berhasil = self.model.update_anggota(
            id_anggota, nama, alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal diperbarui!"
            )

    def bersihkan_form(self):
        # Mengosongkan form
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    def run(self):
        # Menjalankan aplikasi
        self.view.mainloop()
