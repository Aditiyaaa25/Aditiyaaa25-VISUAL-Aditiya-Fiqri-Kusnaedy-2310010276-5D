# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from pelanggan import pelanggan
from transaksi import transaksi
from jenisbarang import jenisbarang
from detailpembayaran import detailpembayaran
from zakat import zakat



# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_main


class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("main.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanUtama=unggahfile.load(filenya,self)
        self.setMenuBar(self.halamanUtama.menuBar())
        # self.resize(self.halamanUtama.size())
        self.halamanUtama.actionPelanggan.triggered.connect(self.bukaPelanggan)
        self.halamanUtama.actionDetail_Pembayaran.triggered.connect(self.bukaDetailPembayaran)
        self.halamanUtama.actionTransaksi.triggered.connect(self.bukaTransaksi)
        self.halamanUtama.actionJenis_Barang.triggered.connect(self.bukaJenisBarang)
        # self.halamanUtama.actionzakat.tirggered.connect(self.bukaZakat)

    def bukaPelanggan(self):
        self.formPelanggan = pelanggan ()
        self.formPelanggan.show()

    def bukaDetailPembayaran(self):
        self.formDetailPembayaran = detailpembayaran()
        self.formDetailPembayaran.show()

    def bukaTransaksi(self):
        self.formTransaksi = transaksi ()
        self.formTransaksi.show()

    def bukaJenisBarang(self):
        self.formJenisBarang = jenisbarang ()
        self.formJenisBarang.show()

    def bukaZakat(self):
        self.formZakat = zakat ()
        self.formZakat.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplikasi = main()
    aplikasi.show()
    sys.exit(app.exec())
