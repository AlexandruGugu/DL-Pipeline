# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preprocessing2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Preprocessing(object):
    def setupUi(self, Preprocessing):
        Preprocessing.setObjectName("Preprocessing")
        Preprocessing.setWindowModality(QtCore.Qt.NonModal)
        Preprocessing.resize(620, 709)
        font = QtGui.QFont()
        font.setPointSize(9)
        Preprocessing.setFont(font)
        Preprocessing.setAutoFillBackground(False)
        Preprocessing.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(Preprocessing)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.btnGenerteImageSets = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGenerteImageSets.setFont(font)
        self.btnGenerteImageSets.setObjectName("btnGenerteImageSets")
        self.gridLayout.addWidget(self.btnGenerteImageSets, 8, 0, 1, 2)
        self.btnGenerateRecords = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGenerateRecords.setFont(font)
        self.btnGenerateRecords.setObjectName("btnGenerateRecords")
        self.gridLayout.addWidget(self.btnGenerateRecords, 9, 0, 1, 2)
        self.lblEval = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblEval.setFont(font)
        self.lblEval.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEval.setObjectName("lblEval")
        self.gridLayout.addWidget(self.lblEval, 5, 3, 1, 1)
        self.lblTrain = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTrain.setFont(font)
        self.lblTrain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTrain.setObjectName("lblTrain")
        self.gridLayout.addWidget(self.lblTrain, 5, 0, 1, 1)
        self.lblTrainCount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTrainCount.setFont(font)
        self.lblTrainCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTrainCount.setObjectName("lblTrainCount")
        self.gridLayout.addWidget(self.lblTrainCount, 7, 0, 1, 1)
        self.txtProjectName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtProjectName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txtProjectName.setObjectName("txtProjectName")
        self.gridLayout.addWidget(self.txtProjectName, 1, 0, 1, 2)
        self.btnNewProject = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnNewProject.setFont(font)
        self.btnNewProject.setObjectName("btnNewProject")
        self.gridLayout.addWidget(self.btnNewProject, 2, 0, 1, 2)
        self.listDataPaths = QtWidgets.QListWidget(self.centralwidget)
        self.listDataPaths.setMaximumSize(QtCore.QSize(16777215, 80))
        self.listDataPaths.setBaseSize(QtCore.QSize(450, 90))
        self.listDataPaths.setObjectName("listDataPaths")
        self.gridLayout.addWidget(self.listDataPaths, 4, 0, 1, 4)
        self.btnAddSelectData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnAddSelectData.setFont(font)
        self.btnAddSelectData.setObjectName("btnAddSelectData")
        self.gridLayout.addWidget(self.btnAddSelectData, 3, 0, 1, 2)
        self.lblTrainPercentage = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblTrainPercentage.setFont(font)
        self.lblTrainPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTrainPercentage.setObjectName("lblTrainPercentage")
        self.gridLayout.addWidget(self.lblTrainPercentage, 6, 0, 1, 1)
        self.lblEvalPercentage = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblEvalPercentage.setFont(font)
        self.lblEvalPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEvalPercentage.setObjectName("lblEvalPercentage")
        self.gridLayout.addWidget(self.lblEvalPercentage, 6, 3, 1, 1)
        self.lblEvalCount = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblEvalCount.setFont(font)
        self.lblEvalCount.setAlignment(QtCore.Qt.AlignCenter)
        self.lblEvalCount.setObjectName("lblEvalCount")
        self.gridLayout.addWidget(self.lblEvalCount, 7, 3, 1, 1)
        self.btnLoadProject = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnLoadProject.setFont(font)
        self.btnLoadProject.setObjectName("btnLoadProject")
        self.gridLayout.addWidget(self.btnLoadProject, 2, 2, 1, 2)
        self.lblProject = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblProject.setFont(font)
        self.lblProject.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblProject.setScaledContents(True)
        self.lblProject.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProject.setObjectName("lblProject")
        self.gridLayout.addWidget(self.lblProject, 0, 0, 1, 4)
        self.btnLoadAddData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnLoadAddData.setFont(font)
        self.btnLoadAddData.setObjectName("btnLoadAddData")
        self.gridLayout.addWidget(self.btnLoadAddData, 3, 2, 1, 2)
        self.btnResizeImages = QtWidgets.QPushButton(self.centralwidget)
        self.btnResizeImages.setObjectName("btnResizeImages")
        self.gridLayout.addWidget(self.btnResizeImages, 8, 2, 1, 2)
        self.btnEditClasses = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditClasses.setObjectName("btnEditClasses")
        self.gridLayout.addWidget(self.btnEditClasses, 9, 2, 1, 2)
        self.txtLog = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtLog.setFont(font)
        self.txtLog.setReadOnly(True)
        self.txtLog.setObjectName("txtLog")
        self.gridLayout.addWidget(self.txtLog, 11, 0, 1, 3)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 6, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chkProject = QtWidgets.QCheckBox(self.centralwidget)
        self.chkProject.setObjectName("chkProject")
        self.verticalLayout.addWidget(self.chkProject)
        self.chkData = QtWidgets.QCheckBox(self.centralwidget)
        self.chkData.setObjectName("chkData")
        self.verticalLayout.addWidget(self.chkData)
        self.chkMap = QtWidgets.QCheckBox(self.centralwidget)
        self.chkMap.setObjectName("chkMap")
        self.verticalLayout.addWidget(self.chkMap)
        self.chkImagesets = QtWidgets.QCheckBox(self.centralwidget)
        self.chkImagesets.setObjectName("chkImagesets")
        self.verticalLayout.addWidget(self.chkImagesets)
        self.chkRecords = QtWidgets.QCheckBox(self.centralwidget)
        self.chkRecords.setObjectName("chkRecords")
        self.verticalLayout.addWidget(self.chkRecords)
        self.gridLayout.addLayout(self.verticalLayout, 11, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 12, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 12, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 12, 2, 1, 1)
        self.lblProject.raise_()
        self.btnAddSelectData.raise_()
        self.btnNewProject.raise_()
        self.btnGenerateRecords.raise_()
        self.txtProjectName.raise_()
        self.btnLoadProject.raise_()
        self.horizontalSlider.raise_()
        self.lblTrainPercentage.raise_()
        self.txtLog.raise_()
        self.lblEval.raise_()
        self.lblEvalPercentage.raise_()
        self.lblTrain.raise_()
        self.lblEvalCount.raise_()
        self.lblTrainCount.raise_()
        self.btnLoadAddData.raise_()
        self.btnGenerteImageSets.raise_()
        self.listDataPaths.raise_()
        self.btnResizeImages.raise_()
        self.btnEditClasses.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        Preprocessing.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Preprocessing)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        Preprocessing.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Preprocessing)
        self.statusbar.setObjectName("statusbar")
        Preprocessing.setStatusBar(self.statusbar)
        self.actionDocumentation = QtWidgets.QAction(Preprocessing)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionLocal_Paths = QtWidgets.QAction(Preprocessing)
        self.actionLocal_Paths.setObjectName("actionLocal_Paths")
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuSettings.addAction(self.actionLocal_Paths)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Preprocessing)
        QtCore.QMetaObject.connectSlotsByName(Preprocessing)

    def retranslateUi(self, Preprocessing):
        _translate = QtCore.QCoreApplication.translate
        Preprocessing.setWindowTitle(_translate("Preprocessing", "PreProcessor"))
        self.btnGenerteImageSets.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Generates the ImageSet files for training and evaluation for each class, using the above selected percentages.</p></body></html>"))
        self.btnGenerteImageSets.setText(_translate("Preprocessing", "Generate ImageSets"))
        self.btnGenerateRecords.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Generates TF pascal records using the script provided in the tensorflow dataset tools. Requires tensorflow local installation with models.</p></body></html>"))
        self.btnGenerateRecords.setText(_translate("Preprocessing", "Generate TF Record"))
        self.lblEval.setText(_translate("Preprocessing", "Evaluation"))
        self.lblTrain.setText(_translate("Preprocessing", "Training"))
        self.lblTrainCount.setToolTip(_translate("Preprocessing", "Number of images."))
        self.lblTrainCount.setText(_translate("Preprocessing", "0"))
        self.txtProjectName.setPlaceholderText(_translate("Preprocessing", "Project_Name"))
        self.btnNewProject.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Creates project directory structure using VOC2012 format at the selected path with project root directory named after project name.</p></body></html>"))
        self.btnNewProject.setText(_translate("Preprocessing", "Create New Project"))
        self.btnAddSelectData.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Selects a directory containing images and/or labels to be added to the project when clicking \'Add Selected Data To Project\'. Multiple data sources can be selected and seen in the list below.</p></body></html>"))
        self.btnAddSelectData.setText(_translate("Preprocessing", "Select Data Path"))
        self.lblTrainPercentage.setText(_translate("Preprocessing", "0%"))
        self.lblEvalPercentage.setText(_translate("Preprocessing", "100%"))
        self.lblEvalCount.setToolTip(_translate("Preprocessing", "Number of images."))
        self.lblEvalCount.setText(_translate("Preprocessing", "0"))
        self.btnLoadProject.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Loading an existing project by selecting it\'s root directory. If VOC2012 folder structure does not exist at selected path, you can choose to generate it.</p></body></html>"))
        self.btnLoadProject.setText(_translate("Preprocessing", "Select Existing Project"))
        self.lblProject.setText(_translate("Preprocessing", "No Project Loaded"))
        self.btnLoadAddData.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Adds the images and labels found at the paths listed below. Upon adding to the project, the paths contained in the labels will be automatically editted for their new location.</p></body></html>"))
        self.btnLoadAddData.setText(_translate("Preprocessing", "Add Selected Data To Project"))
        self.btnResizeImages.setText(_translate("Preprocessing", "Resize Images"))
        self.btnEditClasses.setText(_translate("Preprocessing", "Edit Classes"))
        self.txtLog.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Log</p></body></html>"))
        self.horizontalSlider.setToolTip(_translate("Preprocessing", "<html><head/><body><p align=\"justify\">Determines how many of the images to use for training / evaluation when generating the imagesets.</p></body></html>"))
        self.chkProject.setText(_translate("Preprocessing", "Project Loaded"))
        self.chkData.setText(_translate("Preprocessing", "Data"))
        self.chkMap.setText(_translate("Preprocessing", "Label Map"))
        self.chkImagesets.setText(_translate("Preprocessing", "Imagesets"))
        self.chkRecords.setText(_translate("Preprocessing", "TF Records"))
        self.pushButton.setText(_translate("Preprocessing", "Import Model"))
        self.pushButton_2.setText(_translate("Preprocessing", "Start training"))
        self.pushButton_3.setText(_translate("Preprocessing", "Start evaluation"))
        self.menuHelp.setTitle(_translate("Preprocessing", "Help"))
        self.menuSettings.setTitle(_translate("Preprocessing", "Settings"))
        self.actionDocumentation.setText(_translate("Preprocessing", "Documentation"))
        self.actionLocal_Paths.setText(_translate("Preprocessing", "Set path to tensorflow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Preprocessing = QtWidgets.QMainWindow()
    ui = Ui_Preprocessing()
    ui.setupUi(Preprocessing)
    Preprocessing.show()
    sys.exit(app.exec_())