import pymysql


class Supplier:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", database="dbpy", charset='utf8mb4')

    def read(self, id):
        con = Supplier.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM supplier order by nama_sup asc")
            else:
                cursor.execute(
                    "SELECT * FROM supplier where idsup = %s order by nama_sup asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Supplier.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO supplier(kode_sup,nama_sup,email,telepon,kontak_person) VALUES(%s, %s, %s, %s, %s)",
                           (data['kode_sup'], data['nama_sup'], data['email'], data['telepon'], data['kontak_person'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Supplier.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE supplier set kode_sup = %s, nama_sup = %s, email = %s, telepon = %s, kontak_person = %s where idsup = %s",
                           (data['kode_sup'], data['nama_sup'], data['email'], data['telepon'], data['kontak_person'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Supplier.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM supplier where idsup = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()