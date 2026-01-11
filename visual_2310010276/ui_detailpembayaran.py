# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailpembayaran.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 625)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(140, 100, 511, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPembayaranLabel = QLabel(self.formLayoutWidget)
        self.iDPembayaranLabel.setObjectName(u"iDPembayaranLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPembayaranLabel)

        self.editPembayaran = QLineEdit(self.formLayoutWidget)
        self.editPembayaran.setObjectName(u"editPembayaran")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editPembayaran)

        self.iDTransaksiLabel = QLabel(self.formLayoutWidget)
        self.iDTransaksiLabel.setObjectName(u"iDTransaksiLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.iDTransaksiLabel)

        self.editTransaksi = QLineEdit(self.formLayoutWidget)
        self.editTransaksi.setObjectName(u"editTransaksi")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editTransaksi)

        self.jumlahBayarLabel = QLabel(self.formLayoutWidget)
        self.jumlahBayarLabel.setObjectName(u"jumlahBayarLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.jumlahBayarLabel)

        self.tanggalBayarLabel = QLabel(self.formLayoutWidget)
        self.tanggalBayarLabel.setObjectName(u"tanggalBayarLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggalBayarLabel)

        self.editTBayar = QLineEdit(self.formLayoutWidget)
        self.editTBayar.setObjectName(u"editTBayar")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTBayar)

        self.editJBayar = QLineEdit(self.formLayoutWidget)
        self.editJBayar.setObjectName(u"editJBayar")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editJBayar)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(150, 260, 101, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(350, 260, 101, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(550, 260, 101, 29))
        self.tabelPembayaran = QTableWidget(Form)
        if (self.tabelPembayaran.columnCount() < 4):
            self.tabelPembayaran.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPembayaran.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelPembayaran.setObjectName(u"tabelPembayaran")
        self.tabelPembayaran.setGeometry(QRect(140, 300, 531, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPembayaranLabel.setText(QCoreApplication.translate("Form", u"ID Pembayaran", None))
        self.iDTransaksiLabel.setText(QCoreApplication.translate("Form", u"ID Transaksi", None))
        self.jumlahBayarLabel.setText(QCoreApplication.translate("Form", u"Jumlah Bayar", None))
        self.tanggalBayarLabel.setText(QCoreApplication.translate("Form", u"Tanggal Bayar", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelPembayaran.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID PEMBAYARAN", None));
        ___qtablewidgetitem1 = self.tabelPembayaran.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID TRANSAKSI", None));
        ___qtablewidgetitem2 = self.tabelPembayaran.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"JUMLAH BAYAR", None));
        ___qtablewidgetitem3 = self.tabelPembayaran.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"TANGGAL BAYAR", None));
    # retranslateUi

