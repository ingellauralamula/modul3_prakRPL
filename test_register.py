from models.user_model import UserModel

user = UserModel()

hasil = user.register_user(
    "uji_mahasiswa",
    "user123",
    "anggota"
)

if hasil:
    print("Registrasi pengguna berhasil!")
else:
    print("Registrasi gagal. Periksa pesan error di terminal.")
