from PyQt5 import QtCore, QtGui, QtWidgets
import FileManager
import class_editor
import os
import preprocessing
import glob

class GUI(preprocessing.Ui_Preprocessing):
    def setupBindings(self):
        # BINDINGS
        self.horizontalSlider.valueChanged.connect(self.sliderValueChanged)
        self.btnNewProject.clicked.connect(self.NewProject_Clicked)
        self.btnLoadProject.clicked.connect(self.SelectProject_Clicked)
        self.btnAddSelectData.clicked.connect(self.SelectData_Clicked)
        self.btnLoadAddData.clicked.connect(self.AddData_Clicked)
        self.btnGenerteImageSets.clicked.connect(self.GenerateImageSets_Clicked)
        self.btnGenerateRecords.clicked.connect(self.GenerateRecord_Clicked)
        self.btnEditClasses.clicked.connect(self.EditClasses_Clicked)
        self.btnResizeImages.clicked.connect(self.ResizeImages_Clicked)
        self.pushButton_2.clicked.connect(self.StartTraining_Clicked)
        self.pushButton_3.clicked.connect(self.StartEvaluation_Click)
        #MISC
        self.listDataPaths.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listDataPaths.customContextMenuRequested.connect(self.OpenMenu)
        self.chkProject.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.chkData.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.chkMap.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.chkImagesets.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.chkRecords.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.pushButton.hide()
        self.txtProjectName.hide()
        # OBJECTS
        self.fm = None
        self.window = None



    def sliderValueChanged(self, value):
        try:
            self.lblTrainPercentage.setText(str(value) + '%')
            self.lblEvalPercentage.setText(str(100 - value) + '%')
            if self.fm != None:
                if self.fm.all_image_files != None:
                    data_count = len(self.fm.all_image_files)
                    train_count = int(data_count * value / 100)
                    eval_count = data_count - train_count
                    self.lblEvalCount.setText(str(eval_count))
                    self.lblTrainCount.setText(str(train_count))
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def NewProject_Clicked(self):
        # self.txtLog.setText('works')
        try:
            # if self.txtProjectName.toPlainText() == '':
            #     self.txtLog.append('Please enter a project name!')
            #     return
            idg = QtWidgets.QInputDialog()
            (name, truth) = idg.getText(idg, "Project Name", "Please enter a name for the project:", QtWidgets.QLineEdit.Normal, "project_name")
            if not truth:
                return

            dialog = QtWidgets.QFileDialog()
            dialog.setFileMode(QtWidgets.QFileDialog.Directory)
            dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
            directory = dialog.getExistingDirectory(None, 'Choose Directory In Which To Create Project Folder',
                                                    os.path.curdir)
            if directory  and dialog.result() == QtWidgets.QFileDialog.AcceptOpen:
                directory = directory + '/' + name + '/'
                self.fm = FileManager.FileManager(directory)
                # self.txtProjectName.clear()
                project_name = self.shorten_project_name(directory)
                self.lblProject.setText(project_name)
                self.txtProjectName.clear()
                self.chkProject.setChecked(True)
                self.txtLog.append("Project created at " + directory + "\n")
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def SelectProject_Clicked(self):
        try:
            dialog = QtWidgets.QFileDialog()
            dialog.setFileMode(QtWidgets.QFileDialog.Directory)
            dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
            directory = dialog.getExistingDirectory(None, 'Choose Directory In Which To Create Project Folder',
                                                    os.path.curdir)
            if directory and (dialog.result() == QtWidgets.QFileDialog.AcceptOpen):
                directory = directory + '/'
                self.fm = FileManager.FileManager(directory)
                msg = self.fm.check_files()
                if msg != '':
                    self.txtLog.append(msg)
                project_name = self.shorten_project_name(directory)
                self.listDataPaths.clear()
                self.txtProjectName.clear()
                self.lblProject.setText(project_name)
                self.fm.fill_data()
                self.txtLog.append("Project loaded from " + directory)
                self.txtLog.append('You have jpg files: ' + str(len(self.fm.all_image_files)))
                self.txtLog.append('You have xml files: ' + str(len(self.fm.all_xml_files)))
                self.fm.check_imagesets()
                self.horizontalSlider.setValue(self.fm.imageset_percetange)
                self.chkProject.setChecked(True)
                self.chkData.setChecked(len(self.fm.all_image_files) > 0)
                self.chkMap.setChecked(os.path.exists(self.fm.project_path + "VOC2012/pascal_label_map.pbtxt"))
                self.chkImagesets.setChecked(len(glob.glob(self.fm.project_path + "VOC2012/ImageSets/*")) > 0)
                self.chkRecords.setChecked(len(glob.glob(self.fm.project_path + "*.record")) == 2)
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def SelectData_Clicked(self):
        try:
            dialog = QtWidgets.QFileDialog()
            dialog.setFileMode(QtWidgets.QFileDialog.Directory)
            dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
            directory = dialog.getExistingDirectory(None, 'Choose Directory That Contains Pictures/Labels',
                                                    os.path.curdir) + '/'
            if directory and dialog.result() == QtWidgets.QFileDialog.AcceptOpen:
                items = self.listDataPaths.findItems(directory, QtCore.Qt.MatchExactly)
                if len(items) == 0:
                    self.listDataPaths.addItem(directory)
            self.txtLog.append('Selected data.')
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def AddData_Clicked(self):
        try:
            if self.listDataPaths.count() > 0 and self.chkProject.isChecked():
                self.fm.check_project_dir(self.fm.project_path)
                data_paths = []
                for index in range(self.listDataPaths.count()):
                    data_paths.append(str(self.listDataPaths.item(index).text()))
                self.fm.import_files(data_paths, self.fm.project_path)
                self.listDataPaths.clear()
                self.chkData.setChecked(True)
                self.txtLog.append('Added the selected data to the project')
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def GenerateImageSets_Clicked(self):
        try:
            if self.chkProject and self.chkData:
                self.fm.check_project_dir(self.fm.project_path)
                msg = self.fm.check_files()
                if msg != '':
                    self.txtLog.append(msg)
                self.fm.edit_label_xml()
                self.txtLog.append(self.fm.generate_txt_files(self.horizontalSlider.value()))
                self.chkImagesets.setChecked(True)
                self.chkMap.setChecked(True)
                self.txtLog.append('Imageset files and label map have been generated.')
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    # def UpdatePaths_Clicked(self):
    #     try:
    #         self.fm.check_project_dir(self.fm.project_path)
    #         self.fm.check_files()
    #         self.fm.edit_label_xml()
    #         self.fm.edit_config_paths()
    #     except:
    #         self.txtLog.append('An unexpected error occurred!')
    #         raise

    def GenerateRecord_Clicked(self):
        try:
            if self.chkProject.isChecked() and self.chkData.isChecked() and self.chkImagesets.isChecked() and self.chkMap.isChecked():
                if self.fm.tensorflow_path == '':
                    dialog = QtWidgets.QFileDialog()
                    dialog.setFileMode(QtWidgets.QFileDialog.Directory)
                    dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
                    directory = dialog.getExistingDirectory(None, 'Choose Tensorflow Root Directory (Eg. /home/user/.local/lib/python3.5/site-packages/tensorflow',
                                                            os.path.curdir) + '/'
                    if not (directory and (dialog.result() == QtWidgets.QFileDialog.AcceptOpen)):
                        self.txtLog.append('tensorflow path not loaded')
                        return
                    self.fm.tensorflow_path = directory
                self.fm.run_tf_record_script()
                self.chkRecords.setChecked(True)
                self.txtLog.append('Record files generated have been generated.')
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def OpenMenu(self, position):
        try:
            menu = QtWidgets.QMenu()
            deleteAction = menu.addAction("Delete")
            action = menu.exec_(self.listDataPaths.mapToGlobal(position))
            if action == deleteAction:
                selected_items = self.listDataPaths.selectedIndexes()
                for item in selected_items:
                    self.listDataPaths.takeItem(item.row())
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def Class_Clicked(self, item):
        try:
            cls = item.text()
            data = self.fm.files_per_class[cls]
            self.editor.txtLog.clear()
            self.editor.txtLog.append('Number of images: ' + str(len(data.files)))
            self.editor.txtLog.append('Number of objects: ' + str(data.object_count))
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def RenameClass_Clicked(self):
        try:
            if len(self.editor.listWidget.selectedItems()) > 0:
                cls_name = self.editor.listWidget.selectedItems()[0].text()
                idg = QtWidgets.QInputDialog()
                (new_name, truth) = idg.getText(idg, "Rename", "New class name:", QtWidgets.QLineEdit.Normal, "class name")
                if truth:
                    self.fm.rename_class(cls_name,new_name)
                    self.fm.fill_data()
                    self.editor.listWidget.clear()
                    for key,value in self.fm.files_per_class.items():
                        self.editor.listWidget.addItem(key)
                    self.txtLog.append('WARNING: Classes have been edited! Imagesets and label map may no longer be valid!')
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def RemoveClass_Clicked(self):
        try:
            if len(self.editor.listWidget.selectedItems()) > 0:
                cls_name = self.editor.listWidget.selectedItems()[0].text()
                self.fm.remove_class(cls_name)
                self.fm.fill_data()
                self.editor.listWidget.clear()
                for key, value in self.fm.files_per_class.items():
                    self.editor.listWidget.addItem(key)
                self.txtLog.append('WARNING: Classes have been edited! Imagesets and label map may no longer be valid!')
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def EditClasses_Clicked(self):
        try:
            if self.chkProject.isChecked() and self.chkData.isChecked():
                self.editor = class_editor.Ui_ClassEditor()
                self.window = QtWidgets.QMainWindow()
                self.editor.setupUi(self.window)
                self.window.show()
                for key,value in self.fm.files_per_class.items():
                    self.editor.listWidget.addItem(key)
                self.editor.listWidget.itemClicked.connect(self.Class_Clicked)
                self.editor.button.clicked.connect(self.RenameClass_Clicked)
                self.editor.button_2.clicked.connect(self.RemoveClass_Clicked)
                self.editor.listWidget.clearSelection()
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def ResizeImages_Clicked(self):
        try:
            self.txtLog.append('Resizing...')
            self.fm.resize_images(10)
            self.fm.check_dimensions()
            self.txtLog.append('Images have been resized to 10% of original size.')
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def StartTraining_Clicked(self):
        try:
            dialog = QtWidgets.QFileDialog()
            dialog.setFileMode(QtWidgets.QFileDialog.Directory)
            dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
            directory = dialog.getExistingDirectory(None, 'Select directory of model you wish to use',
                                                    os.path.curdir)
            if directory and (dialog.result() == QtWidgets.QFileDialog.AcceptOpen):
                directory = directory + '/'
                self.fm.check_dimensions()
                self.fm.run_training(directory)
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def StartEvaluation_Click(self):
        try:
            dialog = QtWidgets.QFileDialog()
            dialog.setFileMode(QtWidgets.QFileDialog.Directory)
            dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly)
            directory = dialog.getExistingDirectory(None, 'Select directory of model you wish to use',
                                                    os.path.curdir)
            if directory and (dialog.result() == QtWidgets.QFileDialog.AcceptOpen):
                directory = directory + '/'
                self.fm.check_dimensions()
                self.fm.run_evaluation(directory)
        except:
            self.txtLog.append('An unexpected error occurred!')
            raise

    def shorten_project_name(self, directory):
        c = '/'
        array_with_indexes = [pos for pos, char in enumerate(directory) if char == c]
        slice_pos_in_array_begin = 1
        slice_index_begin = array_with_indexes[slice_pos_in_array_begin]
        slice_pos_in_array_end = len(array_with_indexes) - 3
        slice_index_end = array_with_indexes[slice_pos_in_array_end]
        project_name = directory[slice_index_end:]
        project_name = directory[:slice_index_begin+1] + "..." + project_name
        return project_name


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Preprocessing = QtWidgets.QMainWindow()
    ui = GUI()
    ui.setupUi(Preprocessing)
    ui.setupBindings()
    Preprocessing.show()
    sys.exit(app.exec_())