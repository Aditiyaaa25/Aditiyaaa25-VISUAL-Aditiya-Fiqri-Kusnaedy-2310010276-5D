# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionPelanggan = QAction(main)
        self.actionPelanggan.setObjectName(u"actionPelanggan")
        self.actionDetail_Pembayaran = QAction(main)
        self.actionDetail_Pembayaran.setObjectName(u"actionDetail_Pembayaran")
        self.actionTransaksi = QAction(main)
        self.actionTransaksi.setObjectName(u"actionTransaksi")
        self.actionJenis_Barang = QAction(main)
        self.actionJenis_Barang.setObjectName(u"actionJenis_Barang")
        self.actionZakat = QAction(main)
        self.actionZakat.setObjectName(u"actionZakat")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuJasa_Loundry = QMenu(self.menubar)
        self.menuJasa_Loundry.setObjectName(u"menuJasa_Loundry")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuJasa_Loundry.menuAction())
        self.menuJasa_Loundry.addAction(self.actionPelanggan)
        self.menuJasa_Loundry.addAction(self.actionDetail_Pembayaran)
        self.menuJasa_Loundry.addAction(self.actionTransaksi)
        self.menuJasa_Loundry.addAction(self.actionJenis_Barang)
        self.menuJasa_Loundry.addAction(self.actionZakat)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionPelanggan.setText(QCoreApplication.translate("main", u"Pelanggan", None))
        self.actionDetail_Pembayaran.setText(QCoreApplication.translate("main", u"Detail Pembayaran", None))
        self.actionTransaksi.setText(QCoreApplication.translate("main", u"Transaksi", None))
        self.actionJenis_Barang.setText(QCoreApplication.translate("main", u"Jenis Barang", None))
        self.actionZakat.setText(QCoreApplication.translate("main", u"Zakat", None))
        self.menuJasa_Loundry.setTitle(QCoreApplication.translate("main", u"Jasa Loundry", None))
    # retranslateUi

