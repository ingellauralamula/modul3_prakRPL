# Aplikasi Sistem Perpustakaan

## Deskripsi Aplikasi

Aplikasi Sistem Perpustakaan adalah aplikasi desktop berbasis Python yang digunakan untuk mengelola data perpustakaan, meliputi autentikasi pengguna (login), pengelolaan data buku, dan pengelolaan data anggota. Antarmuka dibangun dengan **CustomTkinter**, data disimpan di **MySQL**, dan kode disusun dengan pola arsitektur **MVC (Model-View-Controller)**. Kualitas kode dijaga melalui **GitHub Actions** (flake8 dan pytest).

## Struktur Direktori MVC

```
modul 3 praktikum/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml      # CI: flake8 + pytest
├── config/
│   └── database.py              # Konfigurasi koneksi MySQL
├── models/                      # MODEL: logika data & query database
│   ├── anggota_model.py
│   ├── buku_model.py
│   └── user_model.py
├── views/                       # VIEW: tampilan antarmuka (CustomTkinter)
│   ├── anggota_view.py
│   ├── buku_view.py
│   └── login_view.py
├── controllers/                 # CONTROLLER: penghubung model dan view
│   ├── anggota_controller.py
│   ├── auth_controller.py
│   └── buku_controller.py
├── tests/                       # Unit test (pytest)
├── dist/                        # Hasil build .exe (PyInstaller)
├── main.py                      # Titik masuk aplikasi
├── requirements.txt             # Daftar dependensi
└── README.md
```

## Panduan Instalasi & Konfigurasi Database MySQL

### 1. Prasyarat
- Python 3.11 atau lebih baru
- MySQL Server (atau XAMPP/Laragon)
- Git

### 2. Clone repositori
```bash
git clone https://github.com/ingellauralamula/modul3_prakRPL.git
cd modul3_prakRPL
```

### 3. Buat virtual environment dan instal dependensi
```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

### 4. Buat database dan tabel MySQL
Jalankan MySQL, lalu eksekusi perintah berikut (lewat phpMyAdmin tab SQL atau MySQL CLI):
```sql
CREATE DATABASE IF NOT EXISTS perpustakaan;
USE perpustakaan;

CREATE TABLE users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(64) NOT NULL,   -- hash SHA-256
    role VARCHAR(20) NOT NULL
);

CREATE TABLE buku (
    id_buku INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(150) NOT NULL,
    penulis VARCHAR(100) NOT NULL,
    tahun_terbit INT NOT NULL
);

CREATE TABLE anggota (
    id_anggota INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    alamat VARCHAR(255)
);
```

### 5. Atur koneksi database
Buka `config/database.py` lalu sesuaikan atribut pada class `Database`:
```python
self.host = "localhost"
self.db_name = "perpustakaan"
self.username = "root"
self.password = ""   # isi jika MySQL Anda memakai password
```

## Akun Login

| Peran | Username | Password | Hak Akses |
|-------|----------|----------|-----------|
| Petugas | `petugas` | `admin123` | admin |
| Mahasiswa | `mahasiswa` | `user123` | anggota |

## Cara Menjalankan Aplikasi

### Dari kode sumber
```bash
python main.py
```

### Dari file executable
Unduh `AplikasiPerpustakaan.exe` pada halaman **Releases** repositori ini (versi v1.0.0), lalu jalankan dengan klik dua kali. Pastikan MySQL sudah aktif dan database sudah dikonfigurasi.

### Menjalankan pengujian
```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
python -m pytest -v
```

## Teknologi
Python, CustomTkinter, MySQL (mysql-connector-python), pytest, flake8, PyInstaller, GitHub Actions.

## Pengembang
Ingel Laura Lamula