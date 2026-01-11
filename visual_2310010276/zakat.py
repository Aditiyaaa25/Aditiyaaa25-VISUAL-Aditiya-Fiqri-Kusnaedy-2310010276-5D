import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class zakat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile("zakat.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile = QUiLoader()
        self.halamanTransaksi = unggahfile.load(filenya, self)
        # self.resize(self.halamanAnggota.size())
        self.aksi = crud()

        # ====== Tambahan alias agar fungsi Transaksi pakai fungsi Transaksi ======
        # self.aksi.simpanTransaksi = self.aksi.simpanTransaksi
        self.aksi.ubahZakat = self.aksi.ubahZakat
        # self.aksi.hapusTransaksi = self.aksi.hapusTransaksi
        self.aksi.dataZakat = self.aksi.dataZakat
        # =====================================================================

        self.tampilZakat()
        # self.halamanTransaksi.btnHapus.clicked.connect(self.hapusTransaksi)
        self.halamanTransaksi.btnUbah.clicked.connect(self.ubahZakat)
        # self.halamanTransaksi.btnSimpan.clicked.connect(self.simpanTransaksi)

    def ubahZakat(self):
        tempNIK = self.halamanZakat.editNIK.text()
        tempNama = self.halamanZakat.editNama.text()
        tempHarta = self.halamanZakat.editHarta.text()
        tempTotal = self.halamanZakat.editTotal.text()
        self.aksi.ubahZakat(tempNIK, tempNama, tempHarta, tempTotal)
        QMessageBox.information(None, "Informasi", "Data Berhasil di ubah")
        self.tampilZakat()

    # def hapusTransaksi(self):
    #     tempID = self.halamanTransaksi.editID.text()
    #     self.aksi.hapusTransaksi(tempID)
    #     QMessageBox.information(None, "Informasi", "Data Berhasil di Hapus")
    #     self.tampilTransaksi()

    def tampilZakat(self):
        self.halamanZakat.tabelZakat.setRowCount(0)
        data = self.aksi.dataZakat()
        for i, r in enumerate(data):
            self.halamanZakat.tabelZakat.insertRow(i)
            self.halamanZakat.tabelZakat.setItem(i, 0, QTableWidgetItem(str(r["nik"])))
            self.halamanZakat.tabelZakat.setItem(i, 1, QTableWidgetItem(str(r["nama"])))
            self.halamanZakat.tabelZakat.setItem(i, 2, QTableWidgetItem(str(r["harta"])))
            self.halamanZakat.tabelZakat.setItem(i, 3, QTableWidgetItem(str(r["Total"])))
