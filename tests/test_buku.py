# Adelia Mutmaina_012
from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi hasil
    assert hasil is True

    # Memverifikasi query dijalankan
    mock_cursor.execute.assert_called_once()

    # Memverifikasi commit dipanggil
    model.conn.commit.assert_called_once()


def test_get_all_buku():
    # Membuat objek model tanpa menjalankan koneksi database asli
    model = BukuModel.__new__(BukuModel)
    model.conn = MagicMock()
    model.table_name = "buku"

    # Menyiapkan data buku tiruan
    data_buku = [
        {
            "id_buku": 1,
            "judul": "Laskar Pelangi",
            "penulis": "Andrea Hirata",
            "tahun_terbit": 2005
        },
        {
            "id_buku": 2,
            "judul": "Bumi",
            "penulis": "Tere Liye",
            "tahun_terbit": 2014
        }
    ]

    # Mengatur hasil query database tiruan
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = data_buku

    # Menjalankan fungsi get_all_buku()
    hasil = model.get_all_buku()

    # Memastikan hasil sesuai dengan data tiruan
    assert hasil == data_buku
    assert len(hasil) == 2

    # Memastikan query dijalankan dengan benar
    model.conn.cursor.assert_called_once_with(
        dictionary=True
    )
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM buku"
    )
    mock_cursor.close.assert_called_once()