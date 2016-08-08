# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from resources import resource_path

class Ui_AutoUploadTMG(object):
    def setupUi(self, AutoUploadTMG):
        AutoUploadTMG.setObjectName("AutoUploadTMG")
        AutoUploadTMG.resize(441, 776)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        AutoUploadTMG.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icon_64.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AutoUploadTMG.setWindowIcon(icon)
        AutoUploadTMG.setAutoFillBackground(False)
        AutoUploadTMG.setStyleSheet("")
        AutoUploadTMG.setIconSize(QtCore.QSize(64, 64))
        AutoUploadTMG.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(AutoUploadTMG)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.param_area = QtWidgets.QGroupBox(self.centralwidget)
        self.param_area.setStyleSheet("")
        self.param_area.setObjectName("param_area")
        self.gridLayout = QtWidgets.QGridLayout(self.param_area)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.param_area)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.param_area)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SHL_prefix = QtWidgets.QLineEdit(self.param_area)
        self.SHL_prefix.setStyleSheet("color: rgb(17, 74, 141);")
        self.SHL_prefix.setAlignment(QtCore.Qt.AlignCenter)
        self.SHL_prefix.setObjectName("SHL_prefix")
        self.horizontalLayout.addWidget(self.SHL_prefix)
        self.shallalist_check = QtWidgets.QCheckBox(self.param_area)
        self.shallalist_check.setStyleSheet("")
        self.shallalist_check.setObjectName("shallalist_check")
        self.horizontalLayout.addWidget(self.shallalist_check)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DGNC_prefix = QtWidgets.QLineEdit(self.param_area)
        self.DGNC_prefix.setStyleSheet("color: rgb(17, 74, 141);")
        self.DGNC_prefix.setAlignment(QtCore.Qt.AlignCenter)
        self.DGNC_prefix.setObjectName("DGNC_prefix")
        self.horizontalLayout_2.addWidget(self.DGNC_prefix)
        self.digincore_check = QtWidgets.QCheckBox(self.param_area)
        self.digincore_check.setStyleSheet("")
        self.digincore_check.setObjectName("digincore_check")
        self.horizontalLayout_2.addWidget(self.digincore_check)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.param_area)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.choice_ruleName = QtWidgets.QComboBox(self.param_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choice_ruleName.sizePolicy().hasHeightForWidth())
        self.choice_ruleName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.choice_ruleName.setFont(font)
        self.choice_ruleName.setAccessibleName("")
        self.choice_ruleName.setStyleSheet("color: rgb(17, 74, 141);\n"
"selection-color: rgb(17, 74, 141);\n"
"gridline-color: rgb(17, 74, 141);")
        self.choice_ruleName.setEditable(True)
        self.choice_ruleName.setCurrentText("")
        self.choice_ruleName.setModelColumn(0)
        self.choice_ruleName.setObjectName("choice_ruleName")
        self.horizontalLayout_3.addWidget(self.choice_ruleName)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.param_area)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.part_size = QtWidgets.QSpinBox(self.param_area)
        self.part_size.setStyleSheet("color: rgb(17, 74, 141);")
        self.part_size.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhPreferNumbers)
        self.part_size.setAlignment(QtCore.Qt.AlignCenter)
        self.part_size.setMinimum(5000)
        self.part_size.setMaximum(600000)
        self.part_size.setProperty("value", 500000)
        self.part_size.setDisplayIntegerBase(10)
        self.part_size.setObjectName("part_size")
        self.horizontalLayout_4.addWidget(self.part_size)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.param_area)
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.exceptionsDomains = QtWidgets.QPlainTextEdit(self.param_area)
        self.exceptionsDomains.setStyleSheet("color: rgb(17, 74, 141);")
        self.exceptionsDomains.setObjectName("exceptionsDomains")
        self.verticalLayout.addWidget(self.exceptionsDomains)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.param_area, 0, 0, 1, 1)
        self.current_status = QtWidgets.QGroupBox(self.centralwidget)
        self.current_status.setStyleSheet("")
        self.current_status.setObjectName("current_status")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.current_status)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.current_status)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.domainNameSetsMemory = QtWidgets.QListWidget(self.current_status)
        self.domainNameSetsMemory.setStyleSheet("color: rgb(17, 74, 141);")
        self.domainNameSetsMemory.setObjectName("domainNameSetsMemory")
        self.verticalLayout_3.addWidget(self.domainNameSetsMemory)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.current_status)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.domainNameSetsTMG = QtWidgets.QListWidget(self.current_status)
        self.domainNameSetsTMG.setStyleSheet("color: rgb(17, 74, 141);")
        self.domainNameSetsTMG.setObjectName("domainNameSetsTMG")
        self.verticalLayout_2.addWidget(self.domainNameSetsTMG)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.current_status)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.operations = QtWidgets.QListWidget(self.current_status)
        self.operations.setStyleSheet("color: rgb(17, 74, 141);")
        self.operations.setObjectName("operations")
        self.verticalLayout_4.addWidget(self.operations)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.procedure_name = QtWidgets.QLabel(self.current_status)
        self.procedure_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.procedure_name.setObjectName("procedure_name")
        self.verticalLayout_6.addWidget(self.procedure_name)
        self.label_2 = QtWidgets.QLabel(self.current_status)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.progressBar_download = QtWidgets.QProgressBar(self.current_status)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(17, 74, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 74, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(17, 74, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.progressBar_download.setPalette(palette)
        self.progressBar_download.setStyleSheet("selection-color: rgb(17, 74, 141);")
        self.progressBar_download.setMaximum(100)
        self.progressBar_download.setProperty("value", 24)
        self.progressBar_download.setObjectName("progressBar_download")
        self.verticalLayout_7.addWidget(self.progressBar_download)
        self.progressBar = QtWidgets.QProgressBar(self.current_status)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_7.addWidget(self.progressBar)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.current_status, 1, 0, 1, 1)
        AutoUploadTMG.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(AutoUploadTMG)
        self.statusBar.setObjectName("statusBar")
        AutoUploadTMG.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(AutoUploadTMG)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 441, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        AutoUploadTMG.setMenuBar(self.menuBar)
        self.action_import = QtWidgets.QAction(AutoUploadTMG)
        self.action_import.setObjectName("action_import")
        self.action_refresh = QtWidgets.QAction(AutoUploadTMG)
        self.action_refresh.setObjectName("action_refresh")
        self.action_clean = QtWidgets.QAction(AutoUploadTMG)
        self.action_clean.setObjectName("action_clean")
        self.menu.addAction(self.action_import)
        self.menu.addAction(self.action_refresh)
        self.menu.addAction(self.action_clean)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(AutoUploadTMG)
        self.domainNameSetsMemory.setCurrentRow(-1)
        self.action_clean.triggered.connect(AutoUploadTMG.start_thread_clean)
        self.choice_ruleName.activated['QString'].connect(AutoUploadTMG.start_refresh_information)
        self.action_import.triggered.connect(AutoUploadTMG.start_thread_import)
        self.action_refresh.triggered.connect(AutoUploadTMG.start_refresh_information)
        self.shallalist_check.stateChanged['int'].connect(AutoUploadTMG.can_choice_action)
        self.digincore_check.stateChanged['int'].connect(AutoUploadTMG.can_choice_action)
        QtCore.QMetaObject.connectSlotsByName(AutoUploadTMG)

    def retranslateUi(self, AutoUploadTMG):
        _translate = QtCore.QCoreApplication.translate
        AutoUploadTMG.setWindowTitle(_translate("AutoUploadTMG", "AutoUploadTMG"))
        self.param_area.setTitle(_translate("AutoUploadTMG", "Параметры"))
        self.label_3.setToolTip(_translate("AutoUploadTMG", "<p>Указанные префиксы будут стоять в начале списков с доменными именами. Удаление списков осуществляеться по начальному префиксу.</p>"))
        self.label_3.setText(_translate("AutoUploadTMG", "Префикс"))
        self.SHL_prefix.setText(_translate("AutoUploadTMG", "SHL"))
        self.shallalist_check.setToolTip(_translate("AutoUploadTMG", "<p>Обновление листов из shallalist.de</p>"))
        self.shallalist_check.setText(_translate("AutoUploadTMG", "SHALLALIST"))
        self.DGNC_prefix.setText(_translate("AutoUploadTMG", "DGNC"))
        self.digincore_check.setToolTip(_translate("AutoUploadTMG", "<p>Обновление листов из digincore.org</p>"))
        self.digincore_check.setText(_translate("AutoUploadTMG", "DIGINCORE"))
        self.label_5.setToolTip(_translate("AutoUploadTMG", "<p>Имя правила, куда будут добалены новые списки.</p>"))
        self.label_5.setText(_translate("AutoUploadTMG", "Имя правила"))
        self.label.setToolTip(_translate("AutoUploadTMG", "<p>Желаемое количество доменных имён в каждом списке.</p>"))
        self.label.setText(_translate("AutoUploadTMG", "Количество адресов"))
        self.label_11.setToolTip(_translate("AutoUploadTMG", "<p>Доменные имена, которые при парсинге будут исключены из списков чёрных листов.</p>"))
        self.label_11.setText(_translate("AutoUploadTMG", "Исключения для доменных имён"))
        self.current_status.setTitle(_translate("AutoUploadTMG", "Текущий статус"))
        self.label_6.setToolTip(_translate("AutoUploadTMG", "<p>Созданные в памяти XML файлы, ожидающие импорта в TMG.</p>"))
        self.label_6.setText(_translate("AutoUploadTMG", "Состояние памяти"))
        self.domainNameSetsMemory.setSortingEnabled(True)
        self.label_7.setToolTip(_translate("AutoUploadTMG", "<p>Списки доменных имён, которые принадлежат правилу.</p>"))
        self.label_7.setText(_translate("AutoUploadTMG", "Состояние правила в TMG"))
        self.label_8.setToolTip(_translate("AutoUploadTMG", "<p>Лог операций.</p>"))
        self.label_8.setText(_translate("AutoUploadTMG", "Операции"))
        self.procedure_name.setText(_translate("AutoUploadTMG", "Скачивание файла"))
        self.label_2.setText(_translate("AutoUploadTMG", "Импорт в TMG"))
        self.progressBar_download.setToolTip(_translate("AutoUploadTMG", "<p>Процесс скачивания архива из ресурса.</p>"))
        self.progressBar.setToolTip(_translate("AutoUploadTMG", "<p>Состояние выполняемого процесса.</p>"))
        self.menu.setTitle(_translate("AutoUploadTMG", "Операции"))
        self.action_import.setText(_translate("AutoUploadTMG", "Импортировать в Forefront TMG"))
        self.action_import.setToolTip(_translate("AutoUploadTMG", "<p>Выполняем удаление старых листов, скачивание архива из интернета, парсинг файлов с чёрными листами, создание XML и импорт в TMG</p>"))
        self.action_refresh.setText(_translate("AutoUploadTMG", "Обновить"))
        self.action_refresh.setToolTip(_translate("AutoUploadTMG", "<p>Подкачка содержащихся в указанном правиле списков, очистка поля Операции</p>"))
        self.action_clean.setText(_translate("AutoUploadTMG", "Удалить из Forefront TMG"))
        self.action_clean.setToolTip(_translate("AutoUploadTMG", "<p>Удаление по указанному префиксу списоков из указанного правила и наборов доменных имён</p>"))

