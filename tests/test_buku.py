from unittest.mock import MagicMock
from models.buku_model import BukuModel


def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

    
def test_get_all_buku():
    # Menginisialisasi Model
    model = BukuModel()

    # Membuat koneksi database tiruan
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menyiapkan data buku tiruan
    data_buku = [
        {
            "id_buku": 1,
            "judul": "Buku Testing",
            "penulis": "Penulis QA",
            "tahun_terbit": 2026
        }
    ]

    mock_cursor.fetchall.return_value = data_buku

    # Mengambil data buku
    hasil = model.get_all_buku()

    # Memeriksa hasil pengujian
    assert hasil == data_buku
    mock_cursor.execute.assert_called_once()
    mock_cursor.close.assert_called_once()
