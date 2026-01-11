# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transaksi.ui'
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
        Form.resize(772, 628)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(160, 100, 511, 135))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDTransaksiLabel = QLabel(self.formLayoutWidget)
        self.iDTransaksiLabel.setObjectName(u"iDTransaksiLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDTransaksiLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.iDPelangganLabel = QLabel(self.formLayoutWidget)
        self.iDPelangganLabel.setObjectName(u"iDPelangganLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.iDPelangganLabel)

        self.editPelanggan = QLineEdit(self.formLayoutWidget)
        self.editPelanggan.setObjectName(u"editPelanggan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editPelanggan)

        self.iDUserLabel = QLabel(self.formLayoutWidget)
        self.iDUserLabel.setObjectName(u"iDUserLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.iDUserLabel)

        self.editUser = QLineEdit(self.formLayoutWidget)
        self.editUser.setObjectName(u"editUser")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editUser)

        self.tanggalTerimaLabel = QLabel(self.formLayoutWidget)
        self.tanggalTerimaLabel.setObjectName(u"tanggalTerimaLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggalTerimaLabel)

        self.editTanggal = QLineEdit(self.formLayoutWidget)
        self.editTanggal.setObjectName(u"editTanggal")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTanggal)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(160, 250, 131, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(350, 250, 131, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(540, 250, 131, 29))
        self.tabelTransaksi = QTableWidget(Form)
        if (self.tabelTransaksi.columnCount() < 4):
            self.tabelTransaksi.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelTransaksi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelTransaksi.setObjectName(u"tabelTransaksi")
        self.tabelTransaksi.setGeometry(QRect(160, 300, 511, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDTransaksiLabel.setText(QCoreApplication.translate("Form", u"ID Transaksi", None))
        self.iDPelangganLabel.setText(QCoreApplication.translate("Form", u"ID Pelanggan", None))
        self.iDUserLabel.setText(QCoreApplication.translate("Form", u"ID User", None))
        self.tanggalTerimaLabel.setText(QCoreApplication.translate("Form", u"Tanggal Terima", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelTransaksi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID TRANSAKSI", None));
        ___qtablewidgetitem1 = self.tabelTransaksi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID PELANGGAN", None));
        ___qtablewidgetitem2 = self.tabelTransaksi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ID USER", None));
        ___qtablewidgetitem3 = self.tabelTransaksi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tanggal Terima", None));
    # retranslateUi

