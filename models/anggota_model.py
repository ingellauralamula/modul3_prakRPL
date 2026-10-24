
# Ingel_F015

from config.database import Database


class AnggotaModel:
    def __init__(self):
        # Menghubungkan Model dengan database
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        # Mengambil semua data anggota
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            try:
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                return cursor.fetchall()
            except Exception as e:
                print("Gagal mengambil data anggota:", e)
                return []
            finally:
                cursor.close()
        return []

    def create_anggota(self, nama_anggota, alamat):
        # Menambahkan data anggota
        if self.conn:
            cursor = self.conn.cursor()
            try:
                query = f"""
                    INSERT INTO {self.table_name} (nama, alamat)
                    VALUES (%s, %s)
                """
                cursor.execute(query, (nama_anggota, alamat))
                self.conn.commit()
                return True
            except Exception as e:
                print("Gagal menyimpan anggota:", e)
                self.conn.rollback()
                return False
            finally:
                cursor.close()
        return False

    def delete_anggota(self, id_anggota):
        # Menghapus anggota berdasarkan ID
        if self.conn:
            cursor = self.conn.cursor()
            try:
                query = f"""
                    DELETE FROM {self.table_name}
                    WHERE id_anggota = %s
                """
                cursor.execute(query, (id_anggota,))
                self.conn.commit()
                return cursor.rowcount > 0
            except Exception as e:
                print("Gagal menghapus anggota:", e)
                self.conn.rollback()
                return False
            finally:
                cursor.close()
        return False

    def update_anggota(self, id_anggota, nama_anggota, alamat):
        # Memperbarui data anggota berdasarkan ID
        if self.conn:
            cursor = self.conn.cursor()
            try:
                query = f"""
                    UPDATE {self.table_name}
                    SET nama = %s, alamat = %s
                    WHERE id_anggota = %s
                """
                cursor.execute(
                    query,
                    (nama_anggota, alamat, id_anggota)
                )
                self.conn.commit()
                return cursor.rowcount > 0
            except Exception as e:
                print("Gagal memperbarui anggota:", e)
                self.conn.rollback()
                return False
            finally:
                cursor.close()
        return False
