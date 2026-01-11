# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class transaksi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("transaksi.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile = QUiLoader()
        self.halamanTransaksi = unggahfile.load(filenya, self)
        # self.resize(self.halamanAnggota.size())
        self.aksi = crud()

        # ====== Tambahan alias agar fungsi Transaksi pakai fungsi Transaksi ======
        self.aksi.simpanTransaksi = self.aksi.simpanTransaksi
        self.aksi.ubahTransaksi = self.aksi.ubahTransaksi
        self.aksi.hapusTransaksi = self.aksi.hapusTransaksi
        self.aksi.dataTransaksi = self.aksi.dataTransaksi
        # =====================================================================

        self.tampilTransaksi()
        self.halamanTransaksi.btnHapus.clicked.connect(self.hapusTransaksi)
        self.halamanTransaksi.btnUbah.clicked.connect(self.ubahTransaksi)
        self.halamanTransaksi.btnSimpan.clicked.connect(self.simpanTransaksi)

    def simpanTransaksi(self):
        if not self.halamanTransaksi.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Transaksi Belum di isi")
            self.halamanTransaksi.editID.setFocus()
        elif not self.halamanTransaksi.editPelanggan.text().strip():
            QMessageBox.information(None, "Informasi", "ID Pelanggan Belum di isi")
            self.halamanTransaksi.editPelanggan.setFocus()
        elif not self.halamanTransaksi.editUser.text().strip():
            QMessageBox.information(None, "Informasi", "ID User Belum di isi")
            self.halamanTransaksi.editUser.setFocus()
        elif not self.halamanTransaksi.editTanggal.text().strip():
            QMessageBox.information(None, "Informasi", "Tanggal Terima Belum di isi")
            self.halamanTransaksi.editTanggal.setFocus()
        else:
            validasi = QMessageBox.information(None, "Informasi", "Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi == QMessageBox.Yes:
                tempID = self.halamanTransaksi.editID.text()
                tempPelanggan = self.halamanTransaksi.editPelanggan.text()
                tempUser = self.halamanTransaksi.editUser.text()
                tempTanggal = self.halamanTransaksi.editTanggal.text()
                # Tetap panggil fungsi aslinya (sudah diarahkan ke simpan Transaksi)
                self.aksi.simpanTransaksi(tempID, tempPelanggan, tempUser, tempTanggal)
                QMessageBox.information(None, "Informasi", "Data Berhasil di simpan")
                self.tampilTransaksi()
            else:
                pass

    def ubahTransaksi(self):
        tempID = self.halamanTransaksi.editID.text()
        tempPelanggan = self.halamanTransaksi.editPelanggan.text()
        tempUser = self.halamanTransaksi.editUser.text()
        tempTanggal= self.halamanTransaksi.editTanggal.text()
        self.aksi.ubahTransaksi(tempID, tempPelanggan, tempUser, tempTanggal)
        QMessageBox.information(None, "Informasi", "Data Berhasil di ubah")
        self.tampilTransaksi()

    def hapusTransaksi(self):
        tempID = self.halamanTransaksi.editID.text()
        self.aksi.hapusTransaksi(tempID)
        QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
        self.tampilTransaksi()

    def tampilTransaksi(self):
        self.halamanTransaksi.tabelTransaksi.setRowCount(0)
        data = self.aksi.dataTransaksi()
        for i, r in enumerate(data):
            self.halamanTransaksi.tabelTransaksi.insertRow(i)
            self.halamanTransaksi.tabelTransaksi.setItem(i, 0, QTableWidgetItem(str(r["transaksi_id"])))
            self.halamanTransaksi.tabelTransaksi.setItem(i, 1, QTableWidgetItem(str(r["pelanggan_id"])))
            self.halamanTransaksi.tabelTransaksi.setItem(i, 2, QTableWidgetItem(str(r["user_id"])))
            self.halamanTransaksi.tabelTransaksi.setItem(i, 3, QTableWidgetItem(str(r["tgl_terima"])))
