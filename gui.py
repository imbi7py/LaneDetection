# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 709)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.g_folder = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_folder.sizePolicy().hasHeightForWidth())
        self.g_folder.setSizePolicy(sizePolicy)
        self.g_folder.setObjectName("g_folder")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.g_folder)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.folderLine = QtWidgets.QLineEdit(self.g_folder)
        self.folderLine.setObjectName("folderLine")
        self.horizontalLayout.addWidget(self.folderLine)
        self.browseButton = QtWidgets.QPushButton(self.g_folder)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout.addWidget(self.browseButton)
        self.verticalLayout_3.addWidget(self.g_folder)
        self.imageDisp = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageDisp.sizePolicy().hasHeightForWidth())
        self.imageDisp.setSizePolicy(sizePolicy)
        self.imageDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.imageDisp.setObjectName("imageDisp")
        self.verticalLayout_3.addWidget(self.imageDisp)
        self.imageControls = QtWidgets.QGroupBox(self.groupBox)
        self.imageControls.setEnabled(False)
        self.imageControls.setObjectName("imageControls")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.imageControls)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.imageControls)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.imageControls)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.spinBox = QtWidgets.QSpinBox(self.imageControls)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.label = QtWidgets.QLabel(self.imageControls)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self.imageControls)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.pushButton_4 = QtWidgets.QPushButton(self.imageControls)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayout_3.addWidget(self.imageControls)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.Status = QtWidgets.QLabel(self.groupBox_3)
        self.Status.setObjectName("Status")
        self.horizontalLayout_5.addWidget(self.Status)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.file_struct = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_struct.sizePolicy().hasHeightForWidth())
        self.file_struct.setSizePolicy(sizePolicy)
        self.file_struct.setObjectName("file_struct")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.file_struct)
        self.verticalLayout.setObjectName("verticalLayout")
        self.g_f_gps = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_gps.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_gps.sizePolicy().hasHeightForWidth())
        self.g_f_gps.setSizePolicy(sizePolicy)
        self.g_f_gps.setCheckable(True)
        self.g_f_gps.setTristate(False)
        self.g_f_gps.setObjectName("g_f_gps")
        self.verticalLayout.addWidget(self.g_f_gps)
        self.g_f_lms_front = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_lms_front.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_lms_front.sizePolicy().hasHeightForWidth())
        self.g_f_lms_front.setSizePolicy(sizePolicy)
        self.g_f_lms_front.setCheckable(True)
        self.g_f_lms_front.setTristate(False)
        self.g_f_lms_front.setObjectName("g_f_lms_front")
        self.verticalLayout.addWidget(self.g_f_lms_front)
        self.g_f_models = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_models.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_models.sizePolicy().hasHeightForWidth())
        self.g_f_models.setSizePolicy(sizePolicy)
        self.g_f_models.setCheckable(True)
        self.g_f_models.setTristate(False)
        self.g_f_models.setObjectName("g_f_models")
        self.verticalLayout.addWidget(self.g_f_models)
        self.g_f_processed = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_processed.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_processed.sizePolicy().hasHeightForWidth())
        self.g_f_processed.setSizePolicy(sizePolicy)
        self.g_f_processed.setCheckable(True)
        self.g_f_processed.setTristate(False)
        self.g_f_processed.setObjectName("g_f_processed")
        self.verticalLayout.addWidget(self.g_f_processed)
        self.g_f_stereo = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_stereo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_stereo.sizePolicy().hasHeightForWidth())
        self.g_f_stereo.setSizePolicy(sizePolicy)
        self.g_f_stereo.setCheckable(True)
        self.g_f_stereo.setTristate(False)
        self.g_f_stereo.setObjectName("g_f_stereo")
        self.verticalLayout.addWidget(self.g_f_stereo)
        self.g_f_left = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_left.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_left.sizePolicy().hasHeightForWidth())
        self.g_f_left.setSizePolicy(sizePolicy)
        self.g_f_left.setCheckable(True)
        self.g_f_left.setTristate(False)
        self.g_f_left.setObjectName("g_f_left")
        self.verticalLayout.addWidget(self.g_f_left)
        self.g_f_centre = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_centre.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_centre.sizePolicy().hasHeightForWidth())
        self.g_f_centre.setSizePolicy(sizePolicy)
        self.g_f_centre.setCheckable(True)
        self.g_f_centre.setTristate(False)
        self.g_f_centre.setObjectName("g_f_centre")
        self.verticalLayout.addWidget(self.g_f_centre)
        self.g_f_right = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_right.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_right.sizePolicy().hasHeightForWidth())
        self.g_f_right.setSizePolicy(sizePolicy)
        self.g_f_right.setCheckable(True)
        self.g_f_right.setTristate(False)
        self.g_f_right.setObjectName("g_f_right")
        self.verticalLayout.addWidget(self.g_f_right)
        self.g_f_lmsTime = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_lmsTime.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_lmsTime.sizePolicy().hasHeightForWidth())
        self.g_f_lmsTime.setSizePolicy(sizePolicy)
        self.g_f_lmsTime.setCheckable(True)
        self.g_f_lmsTime.setTristate(False)
        self.g_f_lmsTime.setObjectName("g_f_lmsTime")
        self.verticalLayout.addWidget(self.g_f_lmsTime)
        self.g_f_stereoTime = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_stereoTime.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g_f_stereoTime.sizePolicy().hasHeightForWidth())
        self.g_f_stereoTime.setSizePolicy(sizePolicy)
        self.g_f_stereoTime.setCheckable(True)
        self.g_f_stereoTime.setTristate(False)
        self.g_f_stereoTime.setObjectName("g_f_stereoTime")
        self.verticalLayout.addWidget(self.g_f_stereoTime)
        self.g_f_good = QtWidgets.QCheckBox(self.file_struct)
        self.g_f_good.setEnabled(False)
        self.g_f_good.setCheckable(True)
        self.g_f_good.setTristate(False)
        self.g_f_good.setObjectName("g_f_good")
        self.verticalLayout.addWidget(self.g_f_good)
        self.verticalLayout_4.addWidget(self.file_struct)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.g_folder.setTitle(_translate("MainWindow", "Dataset Folder"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.imageDisp.setText(_translate("MainWindow", "No image loaded yet"))
        self.imageControls.setTitle(_translate("MainWindow", "Image Controls"))
        self.pushButton_2.setText(_translate("MainWindow", "Previous"))
        self.pushButton_3.setText(_translate("MainWindow", "Run"))
        self.label.setText(_translate("MainWindow", "Run delay (ms)"))
        self.checkBox.setText(_translate("MainWindow", "View Original"))
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Information"))
        self.label_2.setText(_translate("MainWindow", "Currently processing: "))
        self.Status.setText(_translate("MainWindow", "Nothing"))
        self.progressBar.setFormat(_translate("MainWindow", "%p/%m"))
        self.file_struct.setTitle(_translate("MainWindow", "File structure check"))
        self.g_f_gps.setText(_translate("MainWindow", "gps"))
        self.g_f_lms_front.setText(_translate("MainWindow", "lms_front"))
        self.g_f_models.setText(_translate("MainWindow", "Models"))
        self.g_f_processed.setText(_translate("MainWindow", "processed"))
        self.g_f_stereo.setText(_translate("MainWindow", "stereo"))
        self.g_f_left.setText(_translate("MainWindow", "→ Left"))
        self.g_f_centre.setText(_translate("MainWindow", "→ Centre"))
        self.g_f_right.setText(_translate("MainWindow", "→ Right"))
        self.g_f_lmsTime.setText(_translate("MainWindow", "lms_front.timestamps"))
        self.g_f_stereoTime.setText(_translate("MainWindow", "stereo.timestamps"))
        self.g_f_good.setText(_translate("MainWindow", "Folder structure good!"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image List"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Thing 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Thing 2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
