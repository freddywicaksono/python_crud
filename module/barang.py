import pymysql


class Barang:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", database="dbpy", charset='utf8mb4')

    def read(self, id):
        con = Barang.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM barang order by nama_barang asc")
            else:
                cursor.execute(
                    "SELECT * FROM barang where id_barang = %s order by nama_barang asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Barang.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO barang(nama_barang,harga,stok) VALUES(%s, %s, %s)",
                           (data['nama_barang'], data['harga'], data['stok'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Barang.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE barang set nama_barang = %s, harga = %s, stok = %s where id_barang = %s",
                           (data['nama_barang'], data['harga'], data['stok'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Barang.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM barang where id_barang = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()