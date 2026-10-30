# ingel_f015
import tkinter.messagebox as messagebox

from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        # Membuat tampilan login
        self.view = LoginView()

        # Menghubungkan tombol login
        self.view.btn_login.configure(
            command=self.proses_login
        )

    def proses_login(self):
        # Mengambil username dan password
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get().strip()

        # Memeriksa input kosong
        if not username or not password:
            messagebox.showwarning(
                "Peringatan",
                "Username dan password harus diisi!",
                parent=self.view
            )
            return

        # Memeriksa akun petugas
        if username == "petugas" and password == "admin123":
            user_role = "admin"

        # Memeriksa akun mahasiswa
        elif username == "mahasiswa" and password == "user123":
            user_role = "anggota"

        else:
            messagebox.showerror(
                "Login Gagal",
                "Username atau password salah!",
                parent=self.view
            )
            return

        try:
            # Menutup halaman login
            self.view.destroy()

            # Membuka halaman perpustakaan sesuai role
            self.app_utama = BukuController(
                user_role=user_role
            )

            self.app_utama.run()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Gagal membuka aplikasi: {e}"
            )

    def run(self):
        # Menampilkan halaman login
        self.view.mainloop()
