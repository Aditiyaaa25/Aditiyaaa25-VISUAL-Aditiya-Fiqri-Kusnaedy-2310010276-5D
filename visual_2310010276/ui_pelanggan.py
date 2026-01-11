# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pelanggan.ui'
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
        Form.resize(918, 685)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(220, 120, 521, 170))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPelangganLabel = QLabel(self.formLayoutWidget)
        self.iDPelangganLabel.setObjectName(u"iDPelangganLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPelangganLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaPelangganLabel = QLabel(self.formLayoutWidget)
        self.namaPelangganLabel.setObjectName(u"namaPelangganLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaPelangganLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.editAlamat = QLineEdit(self.formLayoutWidget)
        self.editAlamat.setObjectName(u"editAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editAlamat)

        self.teleponLabel = QLabel(self.formLayoutWidget)
        self.teleponLabel.setObjectName(u"teleponLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.teleponLabel)

        self.editTelepon = QLineEdit(self.formLayoutWidget)
        self.editTelepon.setObjectName(u"editTelepon")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTelepon)

        self.passwordLabel = QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.passwordLabel)

        self.editPassword = QLineEdit(self.formLayoutWidget)
        self.editPassword.setObjectName(u"editPassword")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editPassword)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(200, 300, 141, 29))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(380, 300, 141, 29))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(600, 300, 141, 29))
        self.tabelPelanggan = QTableWidget(Form)
        if (self.tabelPelanggan.columnCount() < 4):
            self.tabelPelanggan.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPelanggan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelPelanggan.setObjectName(u"tabelPelanggan")
        self.tabelPelanggan.setGeometry(QRect(210, 340, 511, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDPelangganLabel.setText(QCoreApplication.translate("Form", u"ID Pelanggan", None))
        self.namaPelangganLabel.setText(QCoreApplication.translate("Form", u"Nama Pelanggan", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.teleponLabel.setText(QCoreApplication.translate("Form", u"Telepon", None))
        self.passwordLabel.setText(QCoreApplication.translate("Form", u"Password", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelPelanggan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Pelanggan", None));
        ___qtablewidgetitem1 = self.tabelPelanggan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Pelanggan", None));
        ___qtablewidgetitem2 = self.tabelPelanggan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem3 = self.tabelPelanggan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Telepon", None));
    # retranslateUi

