
# ingel_f015
import customtkinter as ctk
from tkinter import ttk


class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("850x500")

        # Konfigurasi grid utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ============================================
        # FRAME KIRI: FORMULIR INPUT BUKU
        # ============================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Buku",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Input judul buku
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Judul Buku"
        )
        self.entry_judul.pack(
            pady=10, padx=15, fill="x"
        )

        # Input nama penulis
        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Penulis"
        )
        self.entry_penulis.pack(
            pady=10, padx=15, fill="x"
        )

        # Input tahun terbit
        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Tahun Terbit (Misal: 2024)"
        )
        self.entry_tahun.pack(
            pady=10, padx=15, fill="x"
        )

        # ============================================
        # TOMBOL CRUD
        # ============================================

        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green"
        )
        self.btn_simpan.pack(
            pady=(15, 5), padx=15, fill="x"
        )

        self.btn_update = ctk.CTkButton(
            self.frame_kiri,
            text="Perbarui Data",
            fg_color="blue"
        )
        self.btn_update.pack(
            pady=5, padx=15, fill="x"
        )

        self.btn_hapus = ctk.CTkButton(
            self.frame_kiri,
            text="Hapus Data",
            fg_color="red",
            hover_color="darkred"
        )
        self.btn_hapus.pack(
            pady=5, padx=15, fill="x"
        )

        # ============================================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # ============================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0, column=1,
            padx=10, pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Koleksi Buku",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        # Kolom tabel
        kolom = (
            "id_buku",
            "judul",
            "penulis",
            "tahun_terbit"
        )

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=15
        )

        # Header tabel
        self.tabel.heading("id_buku", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun_terbit", text="Tahun")

        # Lebar kolom
        self.tabel.column(
            "id_buku", width=40, anchor="center"
        )
        self.tabel.column("judul", width=180)
        self.tabel.column("penulis", width=120)
        self.tabel.column(
            "tahun_terbit", width=80, anchor="center"
        )

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # ============================================
        # TOMBOL LOGOUT
        # ============================================
        self.btn_logout = ctk.CTkButton(
            self.frame_kanan,
            text="Logout",
            fg_color="#C62828",
            hover_color="#8E0000"
        )
        self.btn_logout.pack(
            pady=(5, 15),
            padx=15,
            anchor="e"
        )

if __name__ == "__main__":
    app = BukuView()
    app.mainloop()
