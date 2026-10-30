# ingel_f015
import customtkinter as ctk
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role.lower()
        self.model = BukuModel()
        self.view = BukuView()
        self.selected_id = None

        # Mengatur judul sesuai hak akses
        if self.user_role in ("admin", "petugas"):
            self.view.title("Sistem Manajemen Perpustakaan - Mode: PETUGAS")
        else:
            self.view.title("Sistem Manajemen Perpustakaan - Mode: ANGGOTA")

        # Menghubungkan tombol Logout dan pilihan buku
        self.view.btn_logout.configure(command=self.logout)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_buku)

        # Memeriksa hak akses petugas
        if self.user_role in ("admin", "petugas"):
            self.view.btn_simpan.configure(command=self.simpan_data)
            self.view.btn_update.configure(command=self.perbarui_data)
            self.view.btn_hapus.configure(command=self.hapus_data)
        else:
            # Menonaktifkan kolom input untuk anggota
            for entry in (self.view.entry_judul, self.view.entry_penulis,
                          self.view.entry_tahun):
                entry.configure(state="disabled")

            # Menyembunyikan tombol CRUD
            self.view.btn_simpan.pack_forget()
            self.view.btn_update.pack_forget()
            self.view.btn_hapus.pack_forget()

            # Tombol akses terkunci
            daftar_tombol = [
                ("Akses Terkunci (Khusus Petugas)", "green"),
                ("Akses Terkunci (Khusus Petugas)", "blue"),
                ("Akses Terkunci (Khusus Petugas)", "red")
            ]
            for teks, warna in daftar_tombol:
                tombol = ctk.CTkButton(
                    self.view.frame_kiri, text=teks,
                    fg_color=warna, state="disabled"
                )
                tombol.pack(pady=4, padx=12, fill="x")

        # Memuat data buku
        self.muat_data_tabel()

    def logout(self):
        # Konfirmasi Logout
        konfirmasi = messagebox.askyesno(
            "Konfirmasi Logout", "Apakah kamu yakin ingin logout?"
        )
        if not konfirmasi:
            return

        # Menutup jendela perpustakaan
        self.view.destroy()

        # Membuka kembali halaman login
        from controllers.auth_controller import AuthController
        login = AuthController()
        login.run()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data buku dari database
        data_buku = self.model.get_all_buku()
        if data_buku:
            for buku in data_buku:
                self.view.tabel.insert("", "end", values=(
                    buku["id_buku"], buku["judul"],
                    buku["penulis"], buku["tahun_terbit"]
                ))

    def pilih_buku(self, event=None):
        pilihan = self.view.tabel.selection()
        if not pilihan:
            self.selected_id = None
            return

        data = self.view.tabel.item(pilihan[0], "values")
        self.selected_id = data[0]

        # Anggota hanya boleh melihat data
        if self.user_role not in ("admin", "petugas"):
            return

        # Mengisi form buku yang dipilih
        for entry, nilai in zip(
            (self.view.entry_judul, self.view.entry_penulis,
             self.view.entry_tahun), data[1:]
        ):
            entry.delete(0, "end")
            entry.insert(0, nilai)

    def simpan_data(self):
        if self.user_role not in ("admin", "petugas"):
            messagebox.showerror(
                "Akses Ditolak", "Hanya petugas yang boleh menambah buku!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
        if not tahun.isdigit():
            messagebox.showwarning("Peringatan", "Tahun terbit harus berupa angka!")
            return

        try:
            berhasil = self.model.create_buku(judul, penulis, int(tahun))
            if berhasil:
                messagebox.showinfo("Sukses", "Buku berhasil disimpan!")
                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Gagal", "Buku gagal disimpan.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def perbarui_data(self):
        if self.user_role not in ("admin", "petugas"):
            messagebox.showerror(
                "Akses Ditolak", "Hanya petugas yang boleh memperbarui buku!"
            )
            return
        if self.selected_id is None:
            messagebox.showwarning(
                "Peringatan", "Pilih buku pada tabel terlebih dahulu!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
        if not tahun.isdigit():
            messagebox.showwarning("Peringatan", "Tahun terbit harus berupa angka!")
            return

        try:
            berhasil = self.model.update_buku(
                self.selected_id, judul, penulis, int(tahun)
            )
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Gagal", "Data buku gagal diperbarui.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def hapus_data(self):
        if self.user_role not in ("admin", "petugas"):
            messagebox.showerror(
                "Akses Ditolak", "Hanya petugas yang boleh menghapus buku!"
            )
            return
        if self.selected_id is None:
            messagebox.showwarning(
                "Peringatan", "Pilih buku pada tabel terlebih dahulu!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi", "Apakah kamu yakin ingin menghapus buku ini?"
        )
        if not konfirmasi:
            return

        try:
            berhasil = self.model.delete_buku(self.selected_id)
            if berhasil:
                messagebox.showinfo("Sukses", "Buku berhasil dihapus!")
                self.kosongkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Gagal", "Buku gagal dihapus.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def kosongkan_form(self):
        self.selected_id = None

        # Mengaktifkan form sementara untuk mengosongkan isinya
        for entry in (self.view.entry_judul, self.view.entry_penulis,
                      self.view.entry_tahun):
            entry.configure(state="normal")
            entry.delete(0, "end")

        # Kunci kembali form jika pengguna adalah anggota
        if self.user_role not in ("admin", "petugas"):
            for entry in (self.view.entry_judul, self.view.entry_penulis,
                          self.view.entry_tahun):
                entry.configure(state="disabled")

        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    def run(self):
        self.view.mainloop()
