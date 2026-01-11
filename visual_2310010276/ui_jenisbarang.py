# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jenisbarang.ui'
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
        Form.resize(854, 573)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(190, 99, 391, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.jenisBarangLabel = QLabel(self.formLayoutWidget)
        self.jenisBarangLabel.setObjectName(u"jenisBarangLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.jenisBarangLabel)

        self.editJenis = QLineEdit(self.formLayoutWidget)
        self.editJenis.setObjectName(u"editJenis")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editJenis)

        self.namaBarangLabel = QLabel(self.formLayoutWidget)
        self.namaBarangLabel.setObjectName(u"namaBarangLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaBarangLabel)

        self.editNamaBarang = QLineEdit(self.formLayoutWidget)
        self.editNamaBarang.setObjectName(u"editNamaBarang")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNamaBarang)

        self.satuanLabel = QLabel(self.formLayoutWidget)
        self.satuanLabel.setObjectName(u"satuanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.satuanLabel)

        self.editSatuan = QLineEdit(self.formLayoutWidget)
        self.editSatuan.setObjectName(u"editSatuan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editSatuan)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(190, 220, 91, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(330, 220, 91, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(490, 220, 91, 29))
        self.tabelJenisBarang = QTableWidget(Form)
        if (self.tabelJenisBarang.columnCount() < 3):
            self.tabelJenisBarang.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelJenisBarang.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelJenisBarang.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelJenisBarang.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabelJenisBarang.setObjectName(u"tabelJenisBarang")
        self.tabelJenisBarang.setGeometry(QRect(190, 260, 381, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.jenisBarangLabel.setText(QCoreApplication.translate("Form", u"ID Barang", None))
        self.namaBarangLabel.setText(QCoreApplication.translate("Form", u"Nama Barang", None))
        self.satuanLabel.setText(QCoreApplication.translate("Form", u"Satuan", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelJenisBarang.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID BARANG", None));
        ___qtablewidgetitem1 = self.tabelJenisBarang.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Jenis Barang", None));
        ___qtablewidgetitem2 = self.tabelJenisBarang.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Satuan", None));
    # retranslateUi

