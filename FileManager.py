import xml.etree.ElementTree as ET
import os
import glob
import random
import configparser
from collections import Counter
import numpy as np
#import imageio as imio
import shutil
class LabelClass():
    def __init__(self):
        self.txt_lines = []
        self.object_count = 0
        self.files = []
class FileManager():

    images_extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
    labels_extensions = ['xml']
    dirs_linux = ['VOC2012', 'models']
    subdirs_linux = [ 'VOC2012/JPEGImages', 'VOC2012/Annotations', 'VOC2012/ImageSets']
    config_vars = ['fine_tune_checkpoint', 'label_map_path', 'input_path']

    def __init__(self, project_path):
        self.project_path = project_path
        self.check_project_dir(project_path)


        self.all_bad_images = []
        self.all_bad_labels = []
        self.imageset_data = []

        #All files in folder
        self.all_files_in_image_folder=glob.glob('VOC2012/JPEGImages/*')
        self.all_files_in_labels_folder=glob.glob('VOC2012/Annotations/*')

        #All needed files in folder
        self.all_image_files = []
        self.all_xml_files = []
        for ext in FileManager.images_extensions:
            self.all_image_files.extend(glob.glob(project_path + 'VOC2012/JPEGImages/*.' + ext))
        for ext in FileManager.labels_extensions:
            self.all_xml_files.extend(glob.glob(project_path + 'VOC2012/Annotations/*.' + ext))
        #self.all_image_files=[glob.glob(e) for p in data_paths for e in [p+'/JPEGImages/*.jpg', p+'/JPEGImages/*.JPG', p+'/JPEGImages/*JPEG', p+'/JPEGImages/*jpeg']]
        #self.all_xml_files=[glob.glob(p+'/Annotations/*.xml') for p in data_paths]

    def check_project_dir(self, project_path):
        #checks if VOC2012 directory structure exists at given path and creates it if it doesn't exist
        if not(os.path.exists(project_path)):
            os.makedirs(project_path)
        for dir in FileManager.dirs_linux:
            if not(os.path.exists(project_path+dir)):
                os.makedirs(project_path+dir)
        for dir in FileManager.subdirs_linux:
            if not(os.path.exists(project_path+dir)):
                os.makedirs(project_path+dir)

    def import_files(self, data_paths, project_path):
        img_files = []
        xml_files = []
        for path in data_paths:
            for ext in FileManager.labels_extensions:
                xml_files.extend(glob.glob(path + "*." + ext))
            for ext in FileManager.images_extensions:
                img_files.extend(glob.glob(path + "*." + ext))
        for filename in img_files:
            file_id = filename.split("/")[-1]
            shutil.copy(filename, project_path+"VOC2012/JPEGImages/"+file_id)
        for filename in xml_files:
            file_id = filename.split("/")[-1]
            shutil.copy(filename, project_path + "VOC2012/Annotations/" + file_id)
        self.all_files_in_image_folder = glob.glob('VOC2012/JPEGImages/*')
        self.all_files_in_labels_folder = glob.glob('VOC2012/Annotations/*')

        # All needed files in folder
        self.all_image_files = []
        self.all_xml_files = []
        for ext in FileManager.images_extensions:
            self.all_image_files.extend(glob.glob(project_path + 'VOC2012/JPEGImages/*.' + ext))
        for ext in FileManager.labels_extensions:
            self.all_xml_files.extend(glob.glob(project_path + 'VOC2012/Annotations/*.' + ext))
        self.edit_label_xml()

    def check_files(self):
        # check pictures extensions
        for index, filename in enumerate(self.all_files_in_image_folder):
            if filename.split('.')[-1] not in FileManager.images_extensions:
                print('This file has wrong extension: {} '.format(filename))
                self.all_bad_images.append(self.all_files_in_image_folder.pop(index))
        #for filename in self.all_bad_images:
         #   self.all_files_in_image_folder.remove(self.all_files_in_image_folder.)

        # check labels for extensions
        for index, filename in enumerate(self.all_files_in_labels_folder):
            if filename.split('.')[-1] not in  FileManager.labels_extensions:
                print('This file has wrong extension: {} '.format(filename))
                self.all_bad_labels.append(self.all_files_in_labels_folder.pop(index))
        #for filename in self.all_bad_labels:
            #self.all_files_in_labels_folder.remove(filename)

        jpg_files_ids = [filename.split('/')[-1].split('.')[0] for filename in self.all_image_files]
        xml_files_ids = [filename.split('/')[-1].split('.')[0] for filename in self.all_xml_files]
        # for jpg_filename in all_jpg_files:
        for index,jpg_id in enumerate(jpg_files_ids):
            if jpg_id not in xml_files_ids:
                print('This picture has no label file: ' + jpg_id)
                self.all_bad_images.append(self.all_image_files.pop(index))
        for index,xml_id in enumerate(xml_files_ids):
            if xml_id not in jpg_files_ids:
                print('This xml file has no picture file: ' + xml_id)
                self.all_bad_labels.append(self.all_bad_labels.pop(index))

        # move bad files to new folder
        if not os.path.exists(self.project_path+'/bad_files'):
            os.makedirs(self.project_path+'/bad_files')
        for filename in self.all_bad_images and self.all_bad_labels:
            os.rename(filename, self.project_path+'/bad_files/'+filename.split('/')[-1])



    def edit_label_xml(self):
        # change path and folder name for annotations
        xml_files = glob.glob(self.project_path+'VOC2012/Annotations/*.xml')
        for filename in xml_files:
            file_id = filename.split("/")[-1]
            # parse xml file
            tree = ET.parse(filename)
            root = tree.getroot()
            # set up new folder name
            new_folder = 'VOC2012'
            root.find("./folder[1]").text = str(new_folder)
            # set up new path
            image_id = root.find("./filename[1]").text
            new_path = self.project_path+'VOC2012/JPEGImages/'
            root.find("./path[1]").text = str(new_path + image_id)
            # overwrite file
            tree.write(filename)

    def generate_txt_files(self, percentage):
        xml_files = []
        img_files = []
        files_per_class = {}
        notification_message = ''
        for ext in FileManager.labels_extensions:
            xml_files.extend(glob.glob(self.project_path+"VOC2012/Annotations/*."+ext))
        for ext in FileManager.images_extensions:
            img_files.extend(glob.glob(self.project_path+"VOC2012/JPEGImages/*."+ext))
        #parsing xml
        for filename in xml_files:
            file_id = filename.split("/")[-1].split(".")[0]
            tree = ET.parse(filename)
            root = tree.getroot()
            #creating a dictionary containing Labeling object for every class and gatering data
            for name in root.iter('name'):
                if name.text not in files_per_class.keys():
                    files_per_class[name.text] = LabelClass()
                if file_id not in files_per_class[name.text].files:
                    files_per_class[name.text].files.append(file_id)
                files_per_class[name.text].object_count += 1

        #parsing xml again to generate ImageSet txt file data
        for filename in xml_files:
            file_id = filename.split("/")[-1].split(".")[0]
            for key, value in files_per_class.items():
                # print("this is class " + key)
                if file_id in value.files:
                    line = file_id + ' 1'
                else:
                    line = file_id + ' -1'
                files_per_class[key].txt_lines.append(line)
        #generate imageset txt files for classes with all the lines in random order
        with open(self.project_path + 'VOC2012/pascal_label_map.pbtxt', 'w') as f:
            f.write('')
        counter = 0
        for key, value in files_per_class.items():



            data = [(random.random(), line) for line in value.txt_lines]
            data.sort()
            train_count = int(len(data) * percentage / 100)
            eval_count = len(data) - train_count
            # with open(self.project_path+'VOC2012/ImageSets/'+str(key) + '.txt', 'w') as f:
            #     for _,line in data:
            #         f.write(line + '\n')

            with open(self.project_path+'VOC2012/ImageSets/Main/'+str(key) + '_val.txt', 'w') as f:
                for index in range(0,eval_count):
                    f.write(data[index][1] + '\n')
            with open(self.project_path+'VOC2012/ImageSets/Main/'+str(key) + '_train.txt', 'w') as f:
                for index in range(eval_count, len(data)):
                    f.write(data[index][1] + '\n')

            notification_message = notification_message + "Class " + key + " contains " + str(value.object_count) + " objects.\n"
            notification_message = notification_message + "ImageSet file for class " + key + " training was generated with " + str(train_count) + " images.\n"
            notification_message = notification_message + "ImageSet file for class " + key + " evaluation was generated with " + str(eval_count) + " images.\n"


            # label map generation
            counter+=1
            with open(self.project_path + 'VOC2012/pascal_label_map.pbtxt', 'a') as f:
                f.write("item {\n  id: "+str(counter) + "\n  name: '"+key+"'\n}\n")
        return notification_message
    def edit_config_files(self):
        for filename in glob.glob(self.project_path + 'models/*.config'):
            cp = configparser.ConfigParser()
            cp.read(filename)
            cp.sections()

    def edit_script(self):
        pass

    def run_tf_record_script(self):
        if os.path.exists('/home/deeplearning/tensorflow/models/research/object_detection/dataset_tools'):
            script_path = '/home/deeplearning/tensorflow/models/research/object_detection/dataset_tools/create_pascal_tf_record.py'
            data_dir = self.project_path
            lbl_map_path = self.project_path + '/VOC2012/pascal_label_map.pbtxt'
            os.system('python3 ' + script_path + ' --data_dir=' + data_dir +' --year=VOC2012 --output_path='+data_dir+'project_train.record --label_map_path='+ lbl_map_path)
            os.system('python3 ' + script_path + '--data_dir=' + data_dir + ' --year=VOC2012 --set=val --output_path=' + data_dir + 'project_val.record --label_map_path=' + lbl_map_path)
        else:
            print('ERROR: Path to dataset_tools does not exist ')