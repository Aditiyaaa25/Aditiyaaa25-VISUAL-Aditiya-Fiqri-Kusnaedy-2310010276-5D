# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class detailpembayaran (QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("detailpembayaran.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile = QUiLoader()
        self.halamanDetailPembayaran = unggahfile.load(filenya, self)
        # self.resize(self.halamanAnggota.size())
        self.aksi = crud()

        # ====== Tambahan alias agar fungsi Transaksi pakai fungsi Transaksi ======
        self.aksi.simpanDetailPembayaran = self.aksi.simpanPembayaran
        self.aksi.ubahDetailPembayaran = self.aksi.ubahPembayaran
        self.aksi.hapusDetailPembayaran = self.aksi.hapusPembayaran
        self.aksi.dataDetailPembayaran = self.aksi.dataPembayaran
        # =====================================================================

        self.tampilDetailPembayaran()
        self.halamanDetailPembayaran.btnHapus.clicked.connect(self.hapusDetailPembayaran)
        self.halamanDetailPembayaran.btnUbah.clicked.connect(self.ubahDetailPembayaran)
        self.halamanDetailPembayaran.btnSimpan.clicked.connect(self.simpanDetailPembayaran)

    def simpanDetailPembayaran(self):
        if not self.halamanDetailPembayaran.editPembayaran.text().strip():
            QMessageBox.information(None, "Informasi", "ID Pembayaran Belum di isi")
            self.halamanDetailPembayaran.editPembayaran.setFocus()
        elif not self.halamanDetailPembayaran.editTransaksi.text().strip():
            QMessageBox.information(None, "Informasi", "ID Transaksi Belum di isi")
            self.halamanDetailPembayaran.editTransaksi.setFocus()
        elif not self.halamanDetailPembayaran.editJBayar.text().strip():
            QMessageBox.information(None, "Informasi", "Jumlah Bayar Belum di isi")
            self.halamanDetailPembayaran.editJBayar.setFocus()
        elif not self.halamanDetailPembayaran.editTBayar.text().strip():
            QMessageBox.information(None, "Informasi", "Tanggal Bayar Belum di isi")
            self.halamanDetailPembayaran.editTBayar.setFocus()
        else:
            validasi = QMessageBox.information(None, "Informasi", "Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi == QMessageBox.Yes:
                tempPembayaran = self.halamanDetailPembayaran.editPembayaran.text()
                tempTransaksi = self.halamanDetailPembayaran.editTransaksi.text()
                tempJBayar = self.halamanDetailPembayaran.editJBayar.text()
                tempTBayar = self.halamanDetailPembayaran.editTBayar.text()
                # Tetap panggil fungsi aslinya (sudah diarahkan ke simpan DETAIL PEMBAYARAN)
                self.aksi.simpanDetailPembayaran(tempPembayaran, tempTransaksi, tempJBayar, tempTBayar)
                QMessageBox.information(None, "Informasi", "Data Berhasil di simpan")
                self.tampilDetailPembayaran()
            else:
                pass

    def ubahDetailPembayaran(self):
        tempPembayaran = self.halamanDetailPembayaran.editPembayaran.text()
        tempTransaksi = self.halamanDetailPembayaran.editTransaksi.text()
        tempJBayar = self.halamanDetailPembayaran.editJBayar.text()
        tempTBayar = self.halamanDetailPembayaran.editTBayar.text()
        self.aksi.ubahDetailPembayaran(tempPembayaran, tempTransaksi, tempJBayar, tempTBayar)
        QMessageBox.information(None, "Informasi", "Data Berhasil di ubah")
        self.tampilDetailPembayaran()

    def hapusDetailPembayaran(self):
        tempPembayaran = self.halamanDetailPembayaran.editPembayaran.text()
        self.aksi.hapusDetailPembayaran(tempPembayaran)
        QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
        self.tampilDetailPembayaran()

    def tampilDetailPembayaran(self):
        self.halamanDetailPembayaran.tabelPembayaran.setRowCount(0)
        data = self.aksi.dataDetailPembayaran()
        for i, r in enumerate(data):
            self.halamanDetailPembayaran.tabelPembayaran.insertRow(i)
            self.halamanDetailPembayaran.tabelPembayaran.setItem(i, 0, QTableWidgetItem(str(r["pembayaran_id"])))
            self.halamanDetailPembayaran.tabelPembayaran.setItem(i, 1, QTableWidgetItem(str(r["transaksi_id"])))
            self.halamanDetailPembayaran.tabelPembayaran.setItem(i, 2, QTableWidgetItem(str(r["jml_bayar"])))
            self.halamanDetailPembayaran.tabelPembayaran.setItem(i, 3, QTableWidgetItem(str(r["tgl_bayar"])))
