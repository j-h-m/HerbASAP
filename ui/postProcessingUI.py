# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/postProcessingUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 635)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(6, 3, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.folderMonitorTab = QtWidgets.QWidget()
        self.folderMonitorTab.setObjectName("folderMonitorTab")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.folderMonitorTab)
        self.gridLayout_22.setContentsMargins(3, 9, 3, 3)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_diagnostics = QtWidgets.QFrame(self.folderMonitorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_diagnostics.sizePolicy().hasHeightForWidth())
        self.frame_diagnostics.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_diagnostics.setFont(font)
        self.frame_diagnostics.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_diagnostics.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_diagnostics.setObjectName("frame_diagnostics")
        self.formLayout = QtWidgets.QFormLayout(self.frame_diagnostics)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(3, 9, 3, 3)
        self.formLayout.setObjectName("formLayout")
        self.label_35 = QtWidgets.QLabel(self.frame_diagnostics)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.label_processtime = QtWidgets.QLabel(self.frame_diagnostics)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_processtime.setFont(font)
        self.label_processtime.setText("")
        self.label_processtime.setObjectName("label_processtime")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_processtime)
        self.label_22 = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.label_barcodes = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_barcodes.setText("")
        self.label_barcodes.setObjectName("label_barcodes")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_barcodes)
        self.label_18 = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.label_isBlurry = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_isBlurry.setText("")
        self.label_isBlurry.setObjectName("label_isBlurry")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_isBlurry)
        self.label_21 = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_lapnorm = QtWidgets.QLabel(self.frame_diagnostics)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_lapnorm.setFont(font)
        self.label_lapnorm.setText("")
        self.label_lapnorm.setObjectName("label_lapnorm")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_lapnorm)
        self.label_17 = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_17.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_17)
        self.label_24 = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_runtime = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_runtime.setText("")
        self.label_runtime.setObjectName("label_runtime")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_runtime)
        self.label_whitergb = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_whitergb.setText("")
        self.label_whitergb.setObjectName("label_whitergb")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.label_whitergb)
        self.label_20 = QtWidgets.QLabel(self.frame_diagnostics)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.verticalLayout_4.addWidget(self.frame_diagnostics)
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem, 0, 3, 1, 1)
        self.toolButton_delPreviousImage = QtWidgets.QToolButton(self.folderMonitorTab)
        self.toolButton_delPreviousImage.setEnabled(False)
        self.toolButton_delPreviousImage.setAutoFillBackground(False)
        self.toolButton_delPreviousImage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/trash-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_delPreviousImage.setIcon(icon)
        self.toolButton_delPreviousImage.setObjectName("toolButton_delPreviousImage")
        self.gridLayout_16.addWidget(self.toolButton_delPreviousImage, 1, 3, 1, 1)
        self.label_cc_image = QtWidgets.QLabel(self.folderMonitorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cc_image.sizePolicy().hasHeightForWidth())
        self.label_cc_image.setSizePolicy(sizePolicy)
        self.label_cc_image.setMinimumSize(QtCore.QSize(0, 50))
        self.label_cc_image.setText("")
        self.label_cc_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cc_image.setObjectName("label_cc_image")
        self.gridLayout_16.addWidget(self.label_cc_image, 0, 2, 2, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_16)
        self.formGroupBox_sessionMetadata = QtWidgets.QGroupBox(self.folderMonitorTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formGroupBox_sessionMetadata.sizePolicy().hasHeightForWidth())
        self.formGroupBox_sessionMetadata.setSizePolicy(sizePolicy)
        self.formGroupBox_sessionMetadata.setFocusPolicy(QtCore.Qt.TabFocus)
        self.formGroupBox_sessionMetadata.setFlat(False)
        self.formGroupBox_sessionMetadata.setCheckable(True)
        self.formGroupBox_sessionMetadata.setChecked(True)
        self.formGroupBox_sessionMetadata.setObjectName("formGroupBox_sessionMetadata")
        self.formLayout_metaData = QtWidgets.QFormLayout(self.formGroupBox_sessionMetadata)
        self.formLayout_metaData.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_metaData.setContentsMargins(3, 3, 3, 3)
        self.formLayout_metaData.setObjectName("formLayout_metaData")
        self.label_16 = QtWidgets.QLabel(self.formGroupBox_sessionMetadata)
        self.label_16.setObjectName("label_16")
        self.formLayout_metaData.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_taxonName = QtWidgets.QLineEdit(self.formGroupBox_sessionMetadata)
        self.lineEdit_taxonName.setObjectName("lineEdit_taxonName")
        self.formLayout_metaData.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_taxonName)
        self.label_19 = QtWidgets.QLabel(self.formGroupBox_sessionMetadata)
        self.label_19.setObjectName("label_19")
        self.formLayout_metaData.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_collectorName = QtWidgets.QLineEdit(self.formGroupBox_sessionMetadata)
        self.lineEdit_collectorName.setObjectName("lineEdit_collectorName")
        self.formLayout_metaData.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_collectorName)
        self.verticalLayout_4.addWidget(self.formGroupBox_sessionMetadata)
        self.gridTabWidget_sessionMonitor = QtWidgets.QTabWidget(self.folderMonitorTab)
        self.gridTabWidget_sessionMonitor.setAutoFillBackground(False)
        self.gridTabWidget_sessionMonitor.setTabPosition(QtWidgets.QTabWidget.North)
        self.gridTabWidget_sessionMonitor.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.gridTabWidget_sessionMonitor.setElideMode(QtCore.Qt.ElideNone)
        self.gridTabWidget_sessionMonitor.setDocumentMode(False)
        self.gridTabWidget_sessionMonitor.setObjectName("gridTabWidget_sessionMonitor")
        self.gridTabWidget_sessionSelect = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridTabWidget_sessionSelect.sizePolicy().hasHeightForWidth())
        self.gridTabWidget_sessionSelect.setSizePolicy(sizePolicy)
        self.gridTabWidget_sessionSelect.setObjectName("gridTabWidget_sessionSelect")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.gridTabWidget_sessionSelect)
        self.gridLayout_23.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.comboBox_technician = QtWidgets.QComboBox(self.gridTabWidget_sessionSelect)
        self.comboBox_technician.setObjectName("comboBox_technician")
        self.horizontalLayout_6.addWidget(self.comboBox_technician)
        self.toolButton_editTechnicians = QtWidgets.QToolButton(self.gridTabWidget_sessionSelect)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_editTechnicians.setIcon(icon1)
        self.toolButton_editTechnicians.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_editTechnicians.setAutoRaise(False)
        self.toolButton_editTechnicians.setObjectName("toolButton_editTechnicians")
        self.horizontalLayout_6.addWidget(self.toolButton_editTechnicians)
        self.horizontalLayout_6.setStretch(1, 2)
        self.gridLayout_23.addLayout(self.horizontalLayout_6, 0, 0, 1, 5)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_rate = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_rate.setFont(font)
        self.label_rate.setScaledContents(True)
        self.label_rate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rate.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_rate.setObjectName("label_rate")
        self.gridLayout_20.addWidget(self.label_rate, 1, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_20.addWidget(self.label_32, 0, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_20.addWidget(self.label_29, 0, 2, 1, 1)
        self.label_runTime = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_runTime.setFont(font)
        self.label_runTime.setScaledContents(True)
        self.label_runTime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_runTime.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_runTime.setObjectName("label_runTime")
        self.gridLayout_20.addWidget(self.label_runTime, 1, 2, 1, 1)
        self.label_imgCount = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_imgCount.setFont(font)
        self.label_imgCount.setScaledContents(True)
        self.label_imgCount.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imgCount.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_imgCount.setObjectName("label_imgCount")
        self.gridLayout_20.addWidget(self.label_imgCount, 1, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_20.addWidget(self.label_31, 0, 1, 1, 1)
        self.gridLayout_20.setColumnStretch(0, 1)
        self.gridLayout_23.addLayout(self.gridLayout_20, 1, 0, 1, 5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_toggleMonitoring = QtWidgets.QPushButton(self.gridTabWidget_sessionSelect)
        self.pushButton_toggleMonitoring.setObjectName("pushButton_toggleMonitoring")
        self.verticalLayout_6.addWidget(self.pushButton_toggleMonitoring)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.gridLayout_23.addLayout(self.verticalLayout_6, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_23.addItem(spacerItem2, 2, 1, 1, 1)
        self.label_speedAnimal = QtWidgets.QLabel(self.gridTabWidget_sessionSelect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_speedAnimal.sizePolicy().hasHeightForWidth())
        self.label_speedAnimal.setSizePolicy(sizePolicy)
        self.label_speedAnimal.setText("")
        self.label_speedAnimal.setScaledContents(False)
        self.label_speedAnimal.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speedAnimal.setObjectName("label_speedAnimal")
        self.gridLayout_23.addWidget(self.label_speedAnimal, 2, 2, 1, 1)
        self.gridTabWidget_sessionMonitor.addTab(self.gridTabWidget_sessionSelect, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_21.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_21.addItem(spacerItem3, 0, 1, 1, 1)
        self.pushButton_processMulti = QtWidgets.QPushButton(self.tab)
        self.pushButton_processMulti.setObjectName("pushButton_processMulti")
        self.gridLayout_21.addWidget(self.pushButton_processMulti, 1, 1, 1, 1)
        self.pushButton_processSingle = QtWidgets.QPushButton(self.tab)
        self.pushButton_processSingle.setObjectName("pushButton_processSingle")
        self.gridLayout_21.addWidget(self.pushButton_processSingle, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridTabWidget_sessionMonitor.addTab(self.tab, "")
        self.verticalLayout_4.addWidget(self.gridTabWidget_sessionMonitor)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.label_imPreview = QtWidgets.QLabel(self.folderMonitorTab)
        self.label_imPreview.setMinimumSize(QtCore.QSize(100, 1))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_imPreview.setFont(font)
        self.label_imPreview.setText("")
        self.label_imPreview.setScaledContents(False)
        self.label_imPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.label_imPreview.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_imPreview.setObjectName("label_imPreview")
        self.horizontalLayout_5.addWidget(self.label_imPreview)
        self.horizontalLayout_5.setStretch(1, 1)
        self.gridLayout_22.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.folderMonitorTab, "")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingsTab)
        self.gridLayout_2.setContentsMargins(3, 9, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.settingsTab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_profiles = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_profiles.setObjectName("comboBox_profiles")
        self.gridLayout_3.addWidget(self.comboBox_profiles, 0, 1, 1, 2)
        self.pushButton_deleteCurrentProfile = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_deleteCurrentProfile.setObjectName("pushButton_deleteCurrentProfile")
        self.gridLayout_3.addWidget(self.pushButton_deleteCurrentProfile, 1, 2, 1, 1)
        self.pushButton_createNewProfile = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_createNewProfile.setObjectName("pushButton_createNewProfile")
        self.gridLayout_3.addWidget(self.pushButton_createNewProfile, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_editCurrentProfile = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_editCurrentProfile.setObjectName("pushButton_editCurrentProfile")
        self.gridLayout_3.addWidget(self.pushButton_editCurrentProfile, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 2)
        self.groupBox_themes = QtWidgets.QGroupBox(self.settingsTab)
        self.groupBox_themes.setObjectName("groupBox_themes")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_themes)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.value_DarkTheme = QtWidgets.QRadioButton(self.groupBox_themes)
        self.value_DarkTheme.setChecked(False)
        self.value_DarkTheme.setObjectName("value_DarkTheme")
        self.verticalLayout_5.addWidget(self.value_DarkTheme)
        self.value_LightTheme = QtWidgets.QRadioButton(self.groupBox_themes)
        self.value_LightTheme.setChecked(True)
        self.value_LightTheme.setObjectName("value_LightTheme")
        self.verticalLayout_5.addWidget(self.value_LightTheme)
        self.label_23 = QtWidgets.QLabel(self.groupBox_themes)
        self.label_23.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.gridLayout_2.addWidget(self.groupBox_themes, 3, 0, 1, 2)
        self.tabWidget.addTab(self.settingsTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.gridTabWidget_sessionMonitor.setCurrentIndex(0)
        self.comboBox_technician.currentTextChanged['QString'].connect(MainWindow.update_metadata)
        self.pushButton_processSingle.clicked.connect(MainWindow.process_image_selection)
        self.lineEdit_collectorName.textChanged['QString'].connect(MainWindow.update_metadata)
        self.pushButton_processMulti.clicked.connect(MainWindow.process_image_directory)
        self.lineEdit_taxonName.textEdited['QString'].connect(MainWindow.update_metadata)
        self.pushButton_editCurrentProfile.clicked.connect(MainWindow.edit_current_profile)
        self.pushButton_deleteCurrentProfile.clicked.connect(MainWindow.delete_current_profile)
        self.pushButton_createNewProfile.clicked.connect(MainWindow.create_profile)
        self.comboBox_profiles.currentTextChanged['QString'].connect(MainWindow.update_currently_selected_profile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HerbASAP"))
        self.label_35.setText(_translate("MainWindow", "Process time:"))
        self.label_22.setText(_translate("MainWindow", "Barcodes:"))
        self.label_18.setText(_translate("MainWindow", "Is blurry:"))
        self.label_21.setText(_translate("MainWindow", "Norm. Laplacian:"))
        self.label_17.setText(_translate("MainWindow", "(higher is better)"))
        self.label_24.setText(_translate("MainWindow", "CC runtime:"))
        self.label_20.setText(_translate("MainWindow", "CC white rgb:"))
        self.formGroupBox_sessionMetadata.setTitle(_translate("MainWindow", "Apply Session Metadata"))
        self.label_16.setText(_translate("MainWindow", "Taxon:"))
        self.label_19.setText(_translate("MainWindow", "Collector:"))
        self.label_14.setText(_translate("MainWindow", "Technician:"))
        self.toolButton_editTechnicians.setText(_translate("MainWindow", "..."))
        self.label_rate.setText(_translate("MainWindow", "0.00"))
        self.label_32.setText(_translate("MainWindow", "Rate (per min)"))
        self.label_29.setText(_translate("MainWindow", "Session Minutes"))
        self.label_runTime.setText(_translate("MainWindow", "0.00"))
        self.label_imgCount.setText(_translate("MainWindow", "0"))
        self.label_31.setText(_translate("MainWindow", "Image Count"))
        self.pushButton_toggleMonitoring.setText(_translate("MainWindow", "Begin Monitoring Folder"))
        self.gridTabWidget_sessionMonitor.setTabText(self.gridTabWidget_sessionMonitor.indexOf(self.gridTabWidget_sessionSelect), _translate("MainWindow", "Monitor Folder"))
        self.pushButton_processMulti.setText(_translate("MainWindow", "Process Entire Directory"))
        self.pushButton_processSingle.setText(_translate("MainWindow", "Process Select Image(s)"))
        self.gridTabWidget_sessionMonitor.setTabText(self.gridTabWidget_sessionMonitor.indexOf(self.tab), _translate("MainWindow", "Select Image(s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.folderMonitorTab), _translate("MainWindow", "Process Images"))
        self.groupBox.setTitle(_translate("MainWindow", "Settings Profiles"))
        self.pushButton_deleteCurrentProfile.setText(_translate("MainWindow", "Delete current profile"))
        self.pushButton_createNewProfile.setText(_translate("MainWindow", "Create new Profile"))
        self.label_2.setText(_translate("MainWindow", "Current Profile:"))
        self.pushButton_editCurrentProfile.setText(_translate("MainWindow", "Edit current profile"))
        self.groupBox_themes.setTitle(_translate("MainWindow", "UI Theme"))
        self.value_DarkTheme.setText(_translate("MainWindow", "Dark theme"))
        self.value_LightTheme.setText(_translate("MainWindow", "Default System Settings"))
        self.label_23.setText(_translate("MainWindow", "(changes will be applied the next time the program opens)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), _translate("MainWindow", "Settings"))
from . import assets_rc
