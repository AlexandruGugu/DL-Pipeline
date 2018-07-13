# DL-Pipeline
This tool provides multiple funcionalities to make life easier when preparing data for tensorflow object detection API.

### Functionalities
- creating VOC2012 directory structure
- importing (copying) files to VOC2012 directory structure
- checking for 'bad' files
  - extensions
  - missing image/label files
- moving bad files
- generating project files
  - pascal label map
  - imageset files (with selected proportion of training/validation)
- checking for out of bounds labels
- resizing images
- renaming of classses inside of labels
- running tensorflow record generation script
- starting tensorflow training/evaluation

### Requirements
- PyQT5
- Functioning Tensorflow object detection API installation

## How to use the application
## Step 1a - Creating a new project directory
A new project can be started by clicking on the [Create New Project] button. After clicking the button a popup will appear asking you to introduce a name for the project. This name will be the name of the root folder of the project. After introducing a name, another window will pop up to select the directory in which the project folder structure should be created. Once the location has been confirmed, a VOC2012 folder structure will be created.

## Step 1b - Selecting an existing project
  In case you already have existing projects wtih the VOC2012 structure, you can select the existing project using the [Existing Project] button. Upon clicking the button, a popup will appear prompting you to select the root directory of the project. WARNING: In case the selected location does not have a VOC2012 structure or has a incomplete one, the missing folders will be created.
Once the project is selected you will be able to see the state the project is in by checking the checkboxes at the bottom right corner of the application and take the next desired actions.

## Step 2 - Selecting and adding data (images and labels)
  In order to select data to be added to the project you need to click the [Select Data Path] button, upon which you will be prompted to select a directory containing images and/or labels that you wish to add to the project. Upon confirmation of the selection, the path to the data will be added to the list below the button. Multiple paths can be selected by repeatedly clicking [Select Data Path] and in the case of a wrong selection you can right click and delete the entries in the list. Once you are done selecting the data want to add to the project, all you have to do is click [Add Selected Data To Project] and all the images and labels contained in the selcted folders will be imported to the project.
WARNING: Data contained in subfolders of selected folders will not be imported.

## Step 3 - Imagesets and Labelmap
  Before generating imageset files and the labelmap, you first need to use the slider bar to select how you want your data to be split between training and evaluation. Once you have set the appropriate percentages, you can click [Generate Imagesets] button which will generate all the needed files, including the labelmap.

## (Optional) Step 4 - Editting
### a) Labels
  In some cases there may be mistakes within the naming used in the labels. To check and fix these problems you can click on [Edit Classes], which will open up a new window in which you can see the classes that exist in your project, the number of images containing the class and the number of instances of the class within those images. In case of a class being mistakenly named (for example you could have cats label as both 'Cat' and 'Kat') you can select the mistyped class and click [Rename] to rename it or [Remove] to remove it.
WARNING: Removing a class will delete the class objects from within the label files and you may end up with label files that contain no objects.
### b) Images
  In some cases you may want to resize the images. To do this you can click on [Resize Images]. This will adjust both the size of the images and the values contianed in the label files.

## Stetp 4 - Generating Tensorflow Records
  When you are ready to generate the TF records, you can click on [Generate TF Records] and you will be prompted to select the location of your tensorflow installation (the root folder, Eg. /home/user/.local/lib/python3.5/site-packages/tensorflow). Once the selection is confirmed, the application will call the required scripts and generate the record files. 
WARNING: This functionality assumes that your tensorflow is correctly installed along with object detection api and still contains the original record generation scripts.
