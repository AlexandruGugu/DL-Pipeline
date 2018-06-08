import xml.etree.ElementTree as ET
import os
import glob
import random
import configparser
import collections
from collections import Counter
import numpy as np
#import imageio as imio
import shutil
class LabelClass():
    def __init__(self):
        self.txt_lines = []
        self.object_count = 0
        self.files = []
        self.files_with_class = []
        self.files_without_class = []


class FileManager():

    images_extensions = ['jpg', 'jpeg', 'JPG', 'JPEG']
    labels_extensions = ['xml']
    dirs_linux = ['VOC2012', 'models']
    subdirs_linux = [ 'VOC2012/JPEGImages', 'VOC2012/Annotations', 'VOC2012/ImageSets']
    config_vars = ['fine_tune_checkpoint', 'label_map_path', 'input_path']


    def __init__(self, project_path):
        self.project_path = project_path
        self.check_project_dir(project_path)

        self.tensorflow_path = ''

        self.all_bad_images = []
        self.all_bad_labels = []
        self.files_per_class = {}


        #All files in folder
        self.all_files_in_import_folders = []
        self.all_files_in_image_folder=glob.glob(project_path +'VOC2012/JPEGImages/*')
        self.all_files_in_labels_folder=glob.glob(project_path + 'VOC2012/Annotations/*')


        #All needed files in folder
        self.all_image_files = []
        self.all_xml_files = []
        for ext in FileManager.images_extensions:
            self.all_image_files.extend(glob.glob(project_path + 'VOC2012/JPEGImages/*.' + ext))
        self.edit_img_extension()
        for ext in FileManager.labels_extensions:
            self.all_xml_files.extend(glob.glob(project_path + 'VOC2012/Annotations/*.' + ext))



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
            self.all_files_in_import_folders.extend(glob.glob(path + '*'))
            for ext in FileManager.labels_extensions:
                xml_files.extend(glob.glob(path + "*." + ext))
            for ext in FileManager.images_extensions:
                img_files.extend(glob.glob(path + "*." + ext))
        for filename in img_files:
            file_id = filename.split("/")[-1]
            shutil.copy(filename, project_path+"VOC2012/JPEGImages/"+file_id.split(".")[0]+".jpg")
        for filename in xml_files:
            file_id = filename.split("/")[-1]
            shutil.copy(filename, project_path + "VOC2012/Annotations/" + file_id)

        # All needed files in folder
        self.all_image_files = []
        self.all_xml_files = []
        for ext in FileManager.images_extensions:
            self.all_image_files.extend(glob.glob(project_path + 'VOC2012/JPEGImages/*.' + ext))
        for ext in FileManager.labels_extensions:
            self.all_xml_files.extend(glob.glob(project_path + 'VOC2012/Annotations/*.' + ext))
        self.edit_label_xml()
        self.check_files()

    def check_files(self):
        #check for wrong files in import source folders
        for index, filename in enumerate(self.all_files_in_import_folders):
            if (filename.split('.')[-1] not in FileManager.images_extensions) and (filename.split('.')[-1] not in  FileManager.labels_extensions):
                print('This file has wrong extension: {} '.format(filename))
                os.rename(filename, self.project_path + '/bad_files/' + filename.split('/')[-1])
        self.all_files_in_import_folders = []
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
                self.all_bad_images.append(self.all_image_files.pop(self.all_image_files.index(self.project_path + "VOC2012/JPEGImages/" + jpg_id + ".jpg")))
        for index,xml_id in enumerate(xml_files_ids):
            if xml_id not in jpg_files_ids:
                print('This xml file has no picture file: ' + xml_id)
                self.all_bad_labels.append(self.all_xml_files.pop(self.all_xml_files.index(self.project_path + "VOC2012/Annotations/" + xml_id + ".xml")))


        # move bad files to new folder
        if not os.path.exists(self.project_path+'/bad_files'):
            os.makedirs(self.project_path+'/bad_files')
        for filename in self.all_bad_images:
            os.rename(filename, self.project_path+'/bad_files/'+filename.split('/')[-1])
        for filename in self.all_bad_labels:
            os.rename(filename, self.project_path + '/bad_files/' + filename.split('/')[-1])

    def edit_img_extension(self):
        for filename in self.all_image_files:
            if filename.split('.')[-1] != 'jpg':
                os.rename(filename, filename.split('.')[0] + '.jpg')


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
            image_jpg = str(image_id).split(".")[0] + ".jpg"
            root.find("./filename[1]").text = image_jpg
            new_path = self.project_path+'VOC2012/JPEGImages/'
            root.find("./path[1]").text = str(new_path) + image_jpg
            # overwrite file
            tree.write(filename)

    def generate_txt_files(self, percentage):
        xml_files = []
        img_files = []
        self.files_per_class = {}
        notification_message = ''

        if not os.path.exists(self.project_path + 'VOC2012/ImageSets/Main'):
            os.makedirs(self.project_path + 'VOC2012/ImageSets/Main')

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
                if name.text not in self.files_per_class.keys():
                    self.files_per_class[name.text] = LabelClass()
                if file_id not in self.files_per_class[name.text].files:
                    self.files_per_class[name.text].files.append(file_id)
                    self.files_per_class[name.text].object_count += 1

        #parsing xml again to generate ImageSet txt file data
        for filename in xml_files:
            file_id = filename.split("/")[-1].split(".")[0]
            for key, value in self.files_per_class.items():
                line = ''
                if file_id in value.files:
                    line = file_id + ' 1'
                    self.files_per_class[key].files_with_class.append(line)
                else:
                    line = file_id + ' -1'
                    self.files_per_class[key].files_without_class.append(line)
                self.files_per_class[key].txt_lines.append(line)
        #generate imageset txt files for classes with all the lines in random order
        with open(self.project_path + 'VOC2012/pascal_label_map.pbtxt', 'w') as f:
            f.write('')
        counter = 0
        self.files_per_class = collections.OrderedDict(sorted(self.files_per_class.items()))
        for key, value in self.files_per_class.items():
            data = [(random.random(), line) for line in value.files_with_class]
            data.sort()
            train_count = int(len(data) * percentage / 100)
            total_train_count = train_count
            train_files_array = []
            eval_count = len(data) - train_count
            total_eval_count = eval_count
            eval_files_array = []
            true_count_val = 0
            true_count_train = 0
            for index in range(0,eval_count):
                eval_files_array.append(data[index][1])
                if data[index][1][-2] != '-':
                    true_count_val += 1
            for index in range(eval_count, len(data)):
                train_files_array.append(data[index][1])
                if data[index][1][-2] != '-':
                    true_count_train += 1

            data = [(random.random(), line) for line in value.files_without_class]
            data.sort()
            train_count = int(len(data) * percentage / 100)
            total_train_count = total_train_count + train_count
            eval_count = len(data) - train_count
            total_eval_count = total_eval_count + eval_count
            for index in range(0,eval_count):
                eval_files_array.append(data[index][1])
                if data[index][1][-2] != '-':
                    true_count_val += 1
            for index in range(eval_count, len(data)):
                train_files_array.append(data[index][1])
                if data[index][1][-2] != '-':
                    true_count_train += 1
            data = [(random.random(), line) for line in train_files_array]
            data.sort()
            with open(self.project_path+'VOC2012/ImageSets/Main/'+str(key) + '_train.txt', 'w') as f:
                for index in range(0, len(data)):
                    f.write(data[index][1] + '\n')
            data = [(random.random(), line) for line in eval_files_array]
            data.sort()
            with open(self.project_path+'VOC2012/ImageSets/Main/'+str(key) + '_val.txt', 'w') as f:
                for index in range(0, len(data)):
                    f.write(data[index][1] + '\n')
            notification_message = notification_message + '---' + key + '---\n'
            notification_message = notification_message + 'Total number of objects: ' + str(value.object_count) + '\n'
            notification_message = notification_message + 'Training images : ' + str(total_train_count) + '/' + str(total_train_count + total_eval_count)  + '(' + str(true_count_train) + ' pictures with object)\n'
            notification_message = notification_message + 'Evaluation images: ' + str(total_eval_count) + '/' + str(total_train_count + total_eval_count)  + '(' + str(true_count_val) + ' pictures with object)\n\n'
            #notification_message = notification_message + "Class " + key + " contains " + str(value.object_count) + " objects.\n"
            #notification_message = notification_message + "ImageSet file for class " + key + " training was generated with " + str(train_count) + " images.\n"
            #notification_message = notification_message + "ImageSet file for class " + key + " evaluation was generated with " + str(eval_count) + " images.\n"


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

    def edit_script(self, script_path):
        new_text = ''
        with open(script_path, 'r') as f:
            text = f.read()
            print(text)
            find_before = """examples_path = os.path.join(data_dir, year, 'ImageSets', 'Main',
                                 '"""
            find_after = '\' + FLAGS.set + \'.txt\')'
            index_start = text.find(find_before) + len(find_before)
            index_end = text.find(find_after,index_start-1)
            new_text = str(text[:index_start]) + str(list(self.files_per_class.keys())[0]) + '_' + str(text[index_end:])
        with open(script_path, 'w') as f:
            f.write(new_text)


    def run_tf_record_script(self):
        print(self.tensorflow_path)
        if os.path.exists(self.tensorflow_path + 'models/research/object_detection/dataset_tools'):
            script_path = self.tensorflow_path + 'models/research/object_detection/dataset_tools/create_pascal_tf_record.py'
            self.edit_script(script_path)
            data_dir = self.project_path
            lbl_map_path = self.project_path + '/VOC2012/pascal_label_map.pbtxt'
            os.system('export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim')
            export_command = 'export PYTHONPATH='+ self.tensorflow_path +'models/research/'
            os.system(export_command)
            os.system('python3 ' + script_path + ' --data_dir=' + data_dir +' --year=VOC2012 --output_path='+data_dir+'project_train.record --label_map_path='+ lbl_map_path)
            os.system('python3 ' + script_path + ' --data_dir=' + data_dir + ' --year=VOC2012 --set=val --output_path=' + data_dir + 'project_val.record --label_map_path=' + lbl_map_path)
        else:
            print('ERROR: Path to dataset_tools does not exist ')

    def rename_class(self, old_name, new_name):
        for filename in self.all_xml_files:
            tree = ET.parse(filename)
            root = tree.getroot()
            for name in root.iter('name'):
                if name.text == old_name:
                    name.text = new_name
            tree.write(filename)
        self.generate_txt_files()


    def remove_class(self, class_name):
        for filename in self.all_xml_files:
            tree = ET.parse(filename)
            root = tree.getroot()
            for obj in root.iter('object'):
                if obj.find("./name[1]").text == class_name:
                    root.remove(obj)
            tree.write(filename)
        self.generate_txt_files()


    def check_dimensions(self):

        problem_files = []
        # change pixels
        for filename in self.all_xml_files:
            file_id = filename.split("/")[-1].split(".")[0]
            # parse xml file
            tree = ET.parse(filename)
            root = tree.getroot()
            WIDTH = 0
            HEIGHT = 0
            # set up new folder name
            for name in root.iter('width'):
                WIDTH = int(name.text)
            for name in root.iter('height'):
                HEIGHT = int(name.text)
            for name in root.iter('xmin'):
                if (int(name.text) <= 0):
                    name.text = str(0)
            for name in root.iter('xmax'):
                if (int(name.text) >= int(WIDTH)):
                    name.text = str(int(WIDTH) - 1)
            for name in root.iter('ymin'):
                if (int(name.text) <= 0):
                    name.text = str(0)
            for name in root.iter('ymax'):
                if (int(name.text) >= HEIGHT):
                    name.text = str(int(HEIGHT) - 1)
            tree.write(filename)


    def resize_images(self, percentage):
        from PIL import Image
        #resize images
        for infile in self.all_image_files:
            file, ext = os.path.splitext(infile)
            im = Image.open(infile)
            new_size = [int(im.size[0] / 100 * percentage), int(im.size[1] / 100 * percentage)]
            print(new_size)
            im.thumbnail(new_size, Image.ANTIALIAS)
            im.save(file + ext, "JPEG")

        # resize labels
        for filename in self.all_xml_files:
            # parse xml file
            tree = ET.parse(filename)
            root = tree.getroot()
            for name in root.iter('width'):
                name.text = str(new_size[0])
            for name in root.iter('height'):
                name.text = str(new_size[1])
            for name in root.iter('xmin'):
                # print(int(int(name.text)/5))
                name.text = str(int(int(name.text) / 100 * percentage))
            for name in root.iter('xmax'):
                # print(int(int(name.text)/5))
                name.text = str(int(int(name.text) / 100 * percentage))
            for name in root.iter('ymin'):
                # print(int(int(name.text)/5))
                name.text = str(int(int(name.text) / 100 * percentage))
            for name in root.iter('ymax'):
                # print(int(int(name.text)/5))
                name.text = str(int(int(name.text) / 100 * percentage))
            tree.write(filename)

    def edit_config_paths(self):
        lines = []
        subfolders = [f.path for f in os.scandir(self.project_path + 'models/') if f.is_dir()]
        for folder in subfolders:
            with open(folder + 'pipeline.config', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if 'fine_tune_checkpoint:' in line:
                        line = '  fine_tune_checkpoint: "' + self.project_path + 'models' + line.split('models')[-1]
                    if 'label_map_path:' in line:
                        line =  '  label_map_path: "' + self.project_path + 'VOC2012/pascal_label_map.pbtxt"'
                    if 'input_path:' in line:
                        if '_val' in line:
                            line = '    input_path: "' + self.project_path + 'project_val.record'
                        else:
                            line = '    input_path: "' + self.project_path + 'project_train.record'
            with open(folder + 'pipeline.config', 'w') as f:
                f.writelines(lines)
