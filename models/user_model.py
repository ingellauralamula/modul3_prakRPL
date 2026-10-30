# ingel_F015
import hashlib
from config.database import Database


class UserModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Mengubah password menjadi hash SHA-256
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def register_user(self, username, password, role):
        # Memeriksa koneksi database
        if not self.conn:
            return False

        try:
            # Mengubah password menjadi hash sebelum disimpan
            password_hash = self.hash_password(password)
            cursor = self.conn.cursor()
            query = (f"INSERT INTO {self.table_name} "
                     "(username, password, role) VALUES (%s, %s, %s)")
            cursor.execute(query, (username, password_hash, role))
            self.conn.commit()
            return True

        except Exception as e:
            # Membatalkan perubahan jika terjadi kesalahan
            self.conn.rollback()
            print(f"Gagal mendaftarkan pengguna: {e}")
            return False

        finally:
            if cursor:
                cursor.close()

    def autentikasi(self, username, password):
        # Memeriksa login pengguna
        if not self.conn:
            return None

        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)
            query = (f"SELECT id_user, username, role FROM {self.table_name} "
                     "WHERE username = %s AND password = %s")
            cursor.execute(query, (username, password_hash))
            return cursor.fetchone()

        except Exception as e:
            print(f"Gagal melakukan autentikasi: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
