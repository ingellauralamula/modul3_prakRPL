# Ingel_F015
import customtkinter as ctk
from tkinter import ttk

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Data Anggota")
        self.geometry("800x480")

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1) # Kolom Kiri (Form Input)
        self.grid_columnconfigure(1, weight=2) # Kolom Kanan (Tabel Data)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Input Anggota
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota")
        self.entry_nama.pack(pady=8, padx=15, fill="x")

        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat Anggota")
        self.entry_alamat.pack(pady=8, padx=15, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=(15, 5), padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data", fg_color="blue")
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data", fg_color="red")
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Tabel (Treeview)
        kolom = ("id_anggota", "nama_anggota", "alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=15)

        # Konfigurasi Header Tabel
        self.tabel.heading("id_anggota", text="ID Anggota")
        self.tabel.heading("nama_anggota", text="Nama Anggota")
        self.tabel.heading("alamat", text="Alamat")

        # Konfigurasi Lebar Kolom
        self.tabel.column("id_anggota", width=80, anchor="center")
        self.tabel.column("nama_anggota", width=160)
        self.tabel.column("alamat", width=200)

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()