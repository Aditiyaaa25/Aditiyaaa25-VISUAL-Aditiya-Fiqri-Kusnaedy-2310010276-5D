# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class pelanggan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("pelanggan.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile = QUiLoader()
        self.halamanPelanggan = unggahfile.load(filenya, self)
        # self.resize(self.halamanAnggota.size())
        self.aksi = crud()

        # ====== Tambahan alias agar fungsi pelanggan pakai fungsi pelanggan ======
        self.aksi.simpanPelanggan = self.aksi.simpanPelanggan
        self.aksi.ubahPelanggan = self.aksi.ubahPelanggan
        self.aksi.hapusPelanggan = self.aksi.hapusPelanggan
        self.aksi.dataPelanggan = self.aksi.dataPelanggan
        # =====================================================================

        self.tampilPelanggan()
        self.halamanPelanggan.btnHapus.clicked.connect(self.hapusPelanggan)
        self.halamanPelanggan.btnUbah.clicked.connect(self.ubahPelanggan)
        self.halamanPelanggan.btnSimpan.clicked.connect(self.simpanPelanggan)

    def simpanPelanggan(self):
        if not self.halamanPelanggan.editID.text().strip():
            QMessageBox.information(None, "Informasi", "ID Pelanggan Belum di isi")
            self.halamanPelanggan.editID.setFocus()
        elif not self.halamanPelanggan.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Pelanggan Belum di isi")
            self.halamanPelanggan.editNama.setFocus()
        elif not self.halamanPelanggan.editAlamat.text().strip():
            QMessageBox.information(None, "Informasi", "Alamat Belum di isi")
            self.halamanPelanggan.editAlamat.setFocus()
        elif not self.halamanPelanggan.editTelepon.text().strip():
            QMessageBox.information(None, "Informasi", "Nomor Telepon Belum di isi")
            self.halamanPelanggan.editTelepon.setFocus()
        elif not self.halamanPelanggan.editPassword.text().strip():
            QMessageBox.information(None, "Informasi", "Password Belum di isi")
            self.halamanPelanggan.editPassword.setFocus()
        else:
            validasi = QMessageBox.information(None, "Informasi", "Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi == QMessageBox.Yes:
                tempID = self.halamanPelanggan.editID.text()
                tempNama = self.halamanPelanggan.editNama.text()
                tempAlamat = self.halamanPelanggan.editAlamat.text()
                tempTelepon = self.halamanPelanggan.editTelepon.text()
                tempPassword = self.halamanPelanggan.editPassword.text()
                # Tetap panggil fungsi aslinya (sudah diarahkan ke simpanPelanggan)
                self.aksi.simpanPelanggan(tempID, tempNama, tempAlamat, tempTelepon, tempPassword)
                QMessageBox.information(None, "Informasi", "Data Berhasil di simpan")
                self.tampilPelanggan()
            else:
                pass

    def ubahPelanggan(self):
        tempID = self.halamanPelanggan.editID.text()
        tempNama = self.halamanPelanggan.editNama.text()
        tempAlamat = self.halamanPelanggan.editAlamat.text()
        tempTelepon = self.halamanPelanggan.editTelepon.text()
        tempPassword = self.halamanPelanggan.editPassword.text()
        self.aksi.ubahPelanggan(tempID, tempNama, tempAlamat, tempTelepon, tempPassword)
        QMessageBox.information(None, "Informasi", "Data Berhasil di ubah")
        self.tampilPelanggan()

    def hapusPelanggan(self):
        tempID = self.halamanPelanggan.editID.text()
        self.aksi.hapusPelanggan(tempID)
        QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
        self.tampilPelanggan()

    def tampilPelanggan(self):
        self.halamanPelanggan.tabelPelanggan.setRowCount(0)
        data = self.aksi.dataPelanggan()
        for i, r in enumerate(data):
            self.halamanPelanggan.tabelPelanggan.insertRow(i)
            self.halamanPelanggan.tabelPelanggan.setItem(i, 0, QTableWidgetItem(str(r["pelanggan_id"])))
            self.halamanPelanggan.tabelPelanggan.setItem(i, 1, QTableWidgetItem(str(r["nama_pelanggan"])))
            self.halamanPelanggan.tabelPelanggan.setItem(i, 2, QTableWidgetItem(str(r["alamat"])))
            self.halamanPelanggan.tabelPelanggan.setItem(i, 3, QTableWidgetItem(str(r["telepon"])))
