# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class jenisbarang (QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("jenisbarang.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile = QUiLoader()
        self.halamanJenisBarang = unggahfile.load(filenya, self)
        # self.resize(self.halamanAnggota.size())
        self.aksi = crud()

        # ====== Tambahan alias agar fungsi Transaksi pakai fungsi Transaksi ======
        self.aksi.simpanJenisBarang = self.aksi.simpanJenisBarang
        self.aksi.ubahJenisBarang = self.aksi.ubahJenisBarang
        self.aksi.hapusJenisBarang = self.aksi.hapusJenisBarang
        self.aksi.dataJenisBarang = self.aksi.dataJenisBarang
        # =====================================================================

        self.tampilJenisBarang()
        self.halamanJenisBarang.btnHapus.clicked.connect(self.hapusJenisBarang)
        self.halamanJenisBarang.btnUbah.clicked.connect(self.ubahJenisBarang)
        self.halamanJenisBarang.btnSimpan.clicked.connect(self.simpanJenisBarang)

    def simpanJenisBarang(self):
        if not self.halamanJenisBarang.editJenis.text().strip():
            QMessageBox.information(None, "Informasi", "Jenis Barang Belum di isi")
            self.halamanJenisBarang.editJenis.setFocus()
        elif not self.halamanJenisBarang.editNamaBarang.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Barang Belum di isi")
            self.halamanJenisBarang.editNamaBarang.setFocus()
        elif not self.halamanJenisBarang.editSatuan.text().strip():
            QMessageBox.information(None, "Informasi", "Satuan Belum di isi")
            self.halamanJenisBarang.editSatuan.setFocus()
        else:
            validasi = QMessageBox.information(None, "Informasi", "Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi == QMessageBox.Yes:
                tempJenis = self.halamanJenisBarang.editJenis.text()
                tempNamaBarang = self.halamanJenisBarang.editNamaBarang.text()
                tempSatuan = self.halamanJenisBarang.editSatuan.text()
                # Tetap panggil fungsi aslinya (sudah diarahkan ke simpan JENIS BARANG)
                self.aksi.simpanJenisBarang(tempJenis, tempNamaBarang, tempSatuan)
                QMessageBox.information(None, "Informasi", "Data Berhasil di simpan")
                self.tampilJenisBarang()
            else:
                pass

    def ubahJenisBarang(self):
        tempJenis = self.halamanJenisBarang.editJenis.text()
        tempNamaBarang = self.halamanJenisBarang.editNamaBarang.text()
        tempSatuan = self.halamanJenisBarang.editSatuan.text()
        self.aksi.ubahJenisBarang(tempJenis, tempNamaBarang, tempSatuan)
        QMessageBox.information(None, "Informasi", "Data Berhasil di ubah")
        self.tampilJenisBarang()

    def hapusJenisBarang(self):
        tempJenis = self.halamanJenisBarang.editJenis.text()
        self.aksi.hapusJenisBarang(tempJenis)
        QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
        self.tampilJenisBarang()

    def tampilJenisBarang(self):
        self.halamanJenisBarang.tabelJenisBarang.setRowCount(0)
        data = self.aksi.dataJenisBarang()
        for i, r in enumerate(data):
            self.halamanJenisBarang.tabelJenisBarang.insertRow(i)
            self.halamanJenisBarang.tabelJenisBarang.setItem(i, 0, QTableWidgetItem(str(r["jnsbrg_id"])))
            self.halamanJenisBarang.tabelJenisBarang.setItem(i, 1, QTableWidgetItem(str(r["nama_barang"])))
            self.halamanJenisBarang.tabelJenisBarang.setItem(i, 2, QTableWidgetItem(str(r["satuan"])))
