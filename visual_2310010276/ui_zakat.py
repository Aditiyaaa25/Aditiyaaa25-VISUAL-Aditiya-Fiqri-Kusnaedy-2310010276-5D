# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'zakat.ui'
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
        Form.resize(651, 549)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(90, 80, 491, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nIKLabel = QLabel(self.formLayoutWidget)
        self.nIKLabel.setObjectName(u"nIKLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nIKLabel)

        self.editNIK = QLineEdit(self.formLayoutWidget)
        self.editNIK.setObjectName(u"editNIK")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editNIK)

        self.nAMALabel = QLabel(self.formLayoutWidget)
        self.nAMALabel.setObjectName(u"nAMALabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nAMALabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.hARTALabel = QLabel(self.formLayoutWidget)
        self.hARTALabel.setObjectName(u"hARTALabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.hARTALabel)

        self.editHarta = QLineEdit(self.formLayoutWidget)
        self.editHarta.setObjectName(u"editHarta")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editHarta)

        self.totalLabel = QLabel(self.formLayoutWidget)
        self.totalLabel.setObjectName(u"totalLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.totalLabel)

        self.editTotal = QLineEdit(self.formLayoutWidget)
        self.editTotal.setObjectName(u"editTotal")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTotal)

        self.tabelZakat = QTableWidget(Form)
        if (self.tabelZakat.columnCount() < 4):
            self.tabelZakat.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelZakat.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelZakat.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelZakat.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelZakat.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelZakat.setObjectName(u"tabelZakat")
        self.tabelZakat.setGeometry(QRect(80, 290, 511, 192))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(490, 240, 90, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.nIKLabel.setText(QCoreApplication.translate("Form", u"NIK", None))
        self.nAMALabel.setText(QCoreApplication.translate("Form", u"NAMA", None))
        self.hARTALabel.setText(QCoreApplication.translate("Form", u"HARTA", None))
        self.totalLabel.setText(QCoreApplication.translate("Form", u"Total", None))
        ___qtablewidgetitem = self.tabelZakat.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem1 = self.tabelZakat.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"NIK", None));
        ___qtablewidgetitem2 = self.tabelZakat.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"NAMA", None));
        ___qtablewidgetitem3 = self.tabelZakat.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"TOTAL", None));
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
    # retranslateUi

