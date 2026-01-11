# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
       self.koneksiDB=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pbo_2310010276'
       )

    # ----------------PELANGGAN----------------
    def simpanPelanggan(self, ID_PELANGGAN, NAMA_PELANGGAN, ALAMAT, TELEPON, PASSWORD):
        alamat=self.koneksiDB.cursor()
        alamat.execute("insert into pelanggan (pelanggan_id, nama_pelanggan, alamat, telepon, password) VALUE(%s,%s,%s,%s,%s)",
        (ID_PELANGGAN, NAMA_PELANGGAN, ALAMAT, TELEPON, PASSWORD))
        self.koneksiDB.commit()
        alamat.close()

    def ubahPelanggan(self, ID_PELANGGAN, NAMA_PELANGGAN, ALAMAT, TELEPON, PASSWORD):
        alamat=self.koneksiDB.cursor()
        alamat.execute("update pelanggan set nama_pelanggan=%s, alamat=%s, telepon=%s, password=%s where pelanggan_id=%s",
        (NAMA_PELANGGAN, ALAMAT, TELEPON, PASSWORD, ID_PELANGGAN))
        self.koneksiDB.commit()
        alamat.close()

    def dataPelanggan(self):
        alamat=self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT*FROM pelanggan order by pelanggan_id asc")
        return alamat.fetchall()


    def hapusPelanggan(self, ID_PELANGGAN):
        alamat=self.koneksiDB.cursor()
        alamat.execute("delete from pelanggan where pelanggan_id=%s", (ID_PELANGGAN,))
        self.koneksiDB.commit()
        alamat.close()

    #------------------------Transaksi--------------------------
    def simpanTransaksi(self, ID_TRANSAKSI, ID_PELANGGAN, ID_USER, TGL_TERIMA):
        alamat = self.koneksiDB.cursor()
        alamat.execute(
        "INSERT INTO transaksi (transaksi_id, pelanggan_id, user_id, tgl_terima) VALUES(%s, %s, %s, %s)",
        (ID_TRANSAKSI, ID_PELANGGAN, ID_USER, TGL_TERIMA))
        self.koneksiDB.commit()
        alamat.close()

    def ubahTransaksi(self, ID_TRANSAKSI, ID_PELANGGAN, ID_USER, TGL_TERIMA):
        alamat = self.koneksiDB.cursor()
        alamat.execute("UPDATE transaksi set pelanggan_id=%s, user_id=%s, tgl_terima=%s WHERE transaksi_id=%s",
        (ID_PELANGGAN, ID_USER, TGL_TERIMA, ID_TRANSAKSI))
        self.koneksiDB.commit()
        alamat.close()

    def dataTransaksi(self):
        alamat = self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT * FROM transaksi order by transaksi_id asc")
        hasil = alamat.fetchall()
        alamat.close()
        return hasil

    def hapusTransaksi(self, ID_TRANSAKSI):
        alamat = self.koneksiDB.cursor()
        alamat.execute("DELETE FROM transaksi WHERE transaksi_id=%s", (ID_TRANSAKSI,))
        self.koneksiDB.commit()
        alamat.close()

    #-------------------JENIS BARANG---------------------
    def simpanJenisBarang(self, ID_BARANG, NAMA_BARANG, SATUAN):
        alamat = self.koneksiDB.cursor()
        alamat.execute(
        "INSERT INTO jenis_barang(jnsbrg_id, nama_barang, satuan) VALUES(%s, %s, %s)",
        (ID_BARANG, NAMA_BARANG, SATUAN))
        self.koneksiDB.commit()
        alamat.close()

    def ubahJenisBarang(self, ID_BARANG, NAMA_BARANG, SATUAN):
        alamat = self.koneksiDB.cursor()
        alamat.execute(
        "UPDATE jenis_barang SET nama_barang=%s, satuan=%s WHERE jnsbrg_id=%s",
        (NAMA_BARANG, SATUAN, ID_BARANG))
        self.koneksiDB.commit()
        alamat.close()

    def dataJenisBarang(self):
        alamat = self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT * FROM jenis_barang ORDER BY jnsbrg_id ASC")
        hasil = alamat.fetchall()
        alamat.close()
        return hasil

    def hapusJenisBarang(self, ID_BARANG):
        alamat = self.koneksiDB.cursor()
        alamat.execute("DELETE FROM jenis_barang WHERE jnsbrg_id=%s", (ID_BARANG,))
        self.koneksiDB.commit()
        alamat.close()

    #--------------------DETAIL PEMBAYARAN-------------------
    def simpanPembayaran(self,ID_PEMBAYARAN, TRANSAKSI_ID, JUMLAH_BAYAR, TANGGAL_BAYAR):
        alamat=self.koneksiDB.cursor()
        alamat.execute("insert into detail_pembayaran(pembayaran_id, transaksi_id, jml_bayar, tgl_bayar) VALUE(%s,%s, %s, %s)",
        (ID_PEMBAYARAN, TRANSAKSI_ID, JUMLAH_BAYAR, TANGGAL_BAYAR))
        self.koneksiDB.commit()
        alamat.close()

    def ubahPembayaran(self, ID_PEMBAYARAN, TRANSAKSI_ID, JUMLAH_BAYAR, TANGGAL_BAYAR):
        alamat=self.koneksiDB.cursor()
        alamat.execute("update detail_pembayaran set transaksi_id=%s, jml_bayar=%s, tgl_bayar=%s where pembayaran_id=%s",
        (TRANSAKSI_ID, JUMLAH_BAYAR, TANGGAL_BAYAR, ID_PEMBAYARAN))
        self.koneksiDB.commit()
        alamat.close()

    def dataPembayaran(self):
        alamat=self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT*FROM detail_pembayaran order by pembayaran_id asc")
        return alamat.fetchall()


    def hapusPembayaran(self, ID_PEMBAYARAN):
        alamat=self.koneksiDB.cursor()
        alamat.execute("delete from detail_pembayaran where pembayaran_id=%s", (ID_PEMBAYARAN,))
        self.koneksiDB.commit()
        alamat.close()


    #--------------------ZAKAT-------------------

    def ubahZakat(self, NIK, NAMA, HARTA, TOTAL):
        alamat=self.koneksiDB.cursor()
        alamat.execute("update zakat set nama=%s, harta=%s, total=%s where nik=%s",
        (TRANSAKSI_ID, JUMLAH_BAYAR, TANGGAL_BAYAR, ID_PEMBAYARAN))
        self.koneksiDB.commit()
        alamat.close()

    def dataZakat(self):
        alamat=self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT*FROM zakat order by nik asc")
        return alamat.fetchall()



