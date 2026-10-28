from config.database import Database
from mysql.connector import Error

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_anggota(self, nama, alamat):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
                val = (nama, alamat)
                cursor.execute(query, val)
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                self.conn.rollback()
                print(f"Gagal menyimpan anggota: {e}")
                return False
        return False

    def update_anggota(self, id_anggota, nama, alamat):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                query = f"UPDATE {self.table_name} SET nama=%s, alamat=%s WHERE id_anggota=%s"
                cursor.execute(query, (nama, alamat, id_anggota))
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                self.conn.rollback()
                print(f"Gagal memperbarui anggota: {e}")
                return False
        return False

    def delete_anggota(self, id_anggota):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM peminjaman WHERE id_anggota=%s", (id_anggota,))
                cursor.execute(f"DELETE FROM {self.table_name} WHERE id_anggota=%s", (id_anggota,))
                self.conn.commit()
                cursor.close()
                return True
            except Error as e:
                self.conn.rollback()
                print(f"Gagal menghapus anggota: {e}")
                return False
        return False