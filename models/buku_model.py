from config.database import Database


class BukuModel:
    def __init__(self):
        # Menghubungkan Model dengan database
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        # Mengambil semua data buku
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        # Menambahkan data buku
        if self.conn:
            cursor = self.conn.cursor()
            query = f"""
                INSERT INTO {self.table_name}
                (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """
            val = (judul, penulis, tahun_terbit)

            try:
                cursor.execute(query, val)
                self.conn.commit()
                return True
            except Exception as e:
                print("Gagal menyimpan data:", e)
                self.conn.rollback()
                return False
            finally:
                cursor.close()
        return False

    def delete_buku(self, id_buku):
        # Menghapus buku berdasarkan ID
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                DELETE FROM {self.table_name}
                WHERE id_buku = %s
            """

            try:
                cursor.execute(query, (id_buku,))
                self.conn.commit()

                # Memastikan ada data yang terhapus
                return cursor.rowcount > 0

            except Exception as e:
                print("Gagal menghapus data:", e)
                self.conn.rollback()
                return False
            finally:
                cursor.close()
        return False

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        # Memperbarui data buku berdasarkan ID
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                UPDATE {self.table_name}
                SET judul = %s,
                    penulis = %s,
                    tahun_terbit = %s
                WHERE id_buku = %s
            """

            val = (judul, penulis, tahun_terbit, id_buku)

            try:
                cursor.execute(query, val)
                self.conn.commit()

                # Memastikan ada baris yang berubah
                return cursor.rowcount > 0

            except Exception as e:
                print("Gagal memperbarui data:", e)
                self.conn.rollback()
                return False
            finally:
                cursor.close()
        return False
