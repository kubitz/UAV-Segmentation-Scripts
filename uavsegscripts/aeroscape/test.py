from typing import Tuple
from cv2 import data
import numpy as np
from PIL import Image
import os
import glob
from labels import datasets
from pathlib import Path
from tqdm import tqdm
import random
from pathlib import Path
def get_palette(dataset_name):
    """Takes a dataset label format. Returns a palette based on the color specified

    Args:
        dataset_name
    Returns:
        list of ints: palette
    """
    palette=[]
    labels_dataset=datasets[dataset_name].labels
    for label in labels_dataset:
        palette.extend(label.color)
    # Zero-pad the palette to 256 RGB colours, i.e. 768 values and apply to image    
    palette += (768-len(palette))*[255]    
    return palette

def get_id_palette(dataset_name, mode='label_id'):
    """Takes a datset label format. Returns a palette based on the label_id/trainId specified

    Args:
        dataset name
    Returns:
        list of ints: palette
    """
    palette=[]
    labels_dataset=datasets[dataset_name].labels
    if mode=='label_id':
        for label in labels_dataset:
            palette.extend((label.id,label.id,label.id))
    elif mode=='train_id':
         for label in labels_dataset:
            palette.extend((label.trainId,label.trainId,label.trainId))       
    else:
        raise ValueError('Invalid Mode')
    # Zero-pad the palette to 256 RGB colours, i.e. 768 values and apply to image
    palette += (768-len(palette))*[255]
    return palette

def remap_img_colors(img,inPalette,outPalette):
    """Remaps colors of an rgb image from one color to another

    Args:
        img (pillow image): image to be converted in the pillow format
        inPalette (list of ints): input set of colors to be modified. 
        outPalette ([type]): Output set of colors for the output image
    
    Return:
        img_out (Pillow image): re-mapped image

    Note:
        The palette should be zero padded to 256RGB colours, i.e. be 768 ints long.
    """
    img_out = quantize2given_palette(img,inPalette)
    img_out.putpalette(outPalette)
    return img_out

def rgb_labels2cityscape(img,dataset_name, mode='label_id'):
    """Converts an image labelled by colors to an image labelled by either label id or train ids (like the cityscape dataset)

    Args:
        img (pillow RGB img): input image labelled by colors
        dataset_name: see labels.py
        mode (str, optional): Specifies if the output image will be labelled based on the label ids or trainIds.
        Defaults to 'label_id'.

    Returns:
        pillow image: re-labelled image
    """
    inPalette=get_palette(dataset_name)
    outPalette=get_id_palette(dataset_name, mode=mode)
    img=remap_img_colors(img,inPalette,outPalette)
    return img


def quantize2given_palette(im, palette):
    """Quantize image to a given palette.

    The input image is expected to be a PIL Image.
    The palette is expected to be a list of no more than 256 R,G,B values."""

    e = len(palette)
    assert e>0,    "Palette unexpectedly short"
    assert e<=768, "Palette unexpectedly long"
    assert e%3==0, "Palette not multiple of 3, so not RGB"

    # Make tiny, 1x1 new palette image
    p = Image.new("P", (1,1))
    p.putpalette(palette)

    # Now quantize input image to the same palette as our little image
    return im.convert("RGB").quantize(palette=p)


def id2trainid(img, dataset_name):
    """Converts image ground-truth labelled with ids to image ground truth labelled with trainIds
    
    Args:
        img (pillow img): input image labelled by label ids (rgb with three identical channels)
        dataset_name: see labels.py
        mode (str, optional): Specifies if the output image will be labelled based on the label ids or trainIds.
        Defaults to 'label_id'.

    Returns:
        pillow image: re-labelled image    
    """
    id_palette=get_id_palette(dataset_name,mode="label_id")
    trainId_palette=get_id_palette(dataset_name,mode="train_id")
    img=remap_img_colors(img,id_palette,trainId_palette)
    return img


def getDirectory(fileName):
    """Returns the directory name for the given filename
    e.g.
    fileName = "/foo/bar/foobar.txt"
    return value is "bar"
    Not much error checking though
    """
    dirName = os.path.dirname(fileName)
    return os.path.basename(dirName)


def ensurePath(path):
    """Make sure that the given path exists"""
    if not path:
        return
    if not os.path.isdir(path):
        os.makedirs(path)


def create_default_file_struct(base_dir,dataset_name):
# Create a default directory to store the new dataset format
    # DEFAULT TARGET DATASET FORMAT
    # └── dataset name
    #     ├── gt
    #     │   ├── test
    #     │   ├── train
    #     │   └── val
    #     ├── images
    #     │   ├── test
    #     │   ├── train
    #     │   └── val
    #     └── image_sets
    #         ├── test.txt
    #         ├── trn.txt
    #         └── val.txt
    base_dir_dataset=os.path.join(base_dir,dataset_name+"_standardized")
    for folder in ['gt','images']:
        for subfolder in ['val','train','test']:
            dir= os.path.join(base_dir_dataset,folder,subfolder)
            Path(dir).mkdir(parents=True, exist_ok=True)
    Path(os.path.join(base_dir_dataset,'image_sets')).mkdir(parents=True, exist_ok=True)


def get_label_img(base_dir_dataset,dataset_name, use_default_split=True):

    if dataset_name=="graz":
    # GRAZ LANDING DATASET DEFAULT FILE STRUCTURE
    # └── semantic_drone_dataset
    #     ├── code
    #     └── training_set
    #         ├── gt
    #         │   ├── bounding_box
    #         │   │   ├── bounding_boxes
    #         │   │   │   └── person
    #         │   │   ├── label_me_xml
    #         │   │   ├── masks
    #         │   │   │   └── person
    #         │   │   └── masks_instances
    #         │   │       └── person
    #         │   └── semantic
    #         │       ├── label_images (this is the directory we use for conversions)
    #         │       └── label_me_xml
    #         └── images
    # NOTE THAT IT THIS DATASET DOES NOT SPECIFY A TRAIN/VAL/TEST SET
        
        gt_dir=os.path.join(base_dir_dataset,"training_set","gt","semantic")
        img_dir=os.path.join(base_dir_dataset,"training_set","images")
        gts=list_files_in_dir(gt_dir,ext=".png")
        imgs=list_files_in_dir(img_dir,ext=".jpg") 
    
    elif dataset_name=="aeroscapes":
    # AEROSCAPE DATASET DEFAULT FILE STRUCTURE
    # ├── ImageSets
    # │   ├── trn.txt
    # │   └── val.txt
    # ├── JPEGImages
    # ├── SegmentationClass
    # └── Visualizations
    # Using default data split defined by dataset
        gt_dir=os.path.join(base_dir_dataset,"Visualizations")
        img_dir=os.path.join(base_dir_dataset,'JPEGImages')
        gts_dir=list_files_in_dir(gt_dir,ext=".png")
        imgs_dir=list_files_in_dir(img_dir,ext=".jpg")
        
        if use_default_split:
            splits=[]
            for split in ['trn.txt','val.txt']:
                split_dir=os.path.join(base_dir_dataset,"ImageSets",split)
                with open(split_dir) as f:
                    split=f.read().splitlines()
                    splits.append(split)            
            imgs=[[],[],[]]  
            gts= [[],[],[]] 
            for idx,gt in enumerate(gts_dir):
                base_name=Path(gt).stem
                if base_name in splits[0]:
                    imgs[0].append(imgs_dir[idx])
                    imgs[1].append(imgs_dir[idx])
                else:
                    gts[0].append(gt)
                    gts[1].append(gt)
        else:
            gts=gts_dir
            imgs=imgs_dir
    
    elif dataset_name=="uavid":
    # UAVID DATASET DEFAULT FILE STRUCTURE
    # └── uavid_v1.5_official_release_image
    #     ├── uavid_test
    #     │   ├── seq21
    #     │   :   └── Images
    #     │   └── seq42
    #     │       └── Images
    #     ├── uavid_train
    #     │   ├── seq1
    #     │   │   ├── Images
    #     │   :   └── Labels
    #     │   └── seq9
    #     │       ├── Images
    #     │       └── Labels
    #     └── uavid_val
    #         ├── seq16
    #         │   ├── Images
    #         :   └── Labels
    #         └── seq37
    #             ├── Images
    #             └── Labels
    # Test images do not have labels, hence they are discarded.
    # Sorry about this terrible implementation :( Gotta get stuff done. 

        dir_val=os.path.join(base_dir_dataset,"uavid_val")
        dir_train=os.path.join(base_dir_dataset,"uavid_train")
        
        files_val=list_files_in_dir(dir_val,ext=".png")
        files_train=list_files_in_dir(dir_train,ext=".png")
        files_all=files_train+files_val
        imgs_dir=[]
        gts_dir=[]
        
        for file in files_all:
            p=Path(file)
            if p.parents[0].name=='Images':
                imgs_dir.append(file)
            elif p.parents[0].name=='Labels':
                gts_dir.append(file)
            else:
                raise NameError("Dataset does not follow required structure")
        
        if use_default_split:
            imgs=[[],[],[]]  
            gts= [[],[],[]]         
            for idx,img in enumerate(imgs_dir):
                p=Path(img)
                if p.parents[2].name=='uavid_train':
                    imgs[0].append(img)
                    gts[0].append(gts_dir[idx])

                elif p.parents[2].name=='uavid_val':
                    imgs[1].append(img)
                    gts[1].append(gts_dir[idx])
                else:
                    raise NameError("Dataset does not follow required structure")
        else:
            imgs=imgs_dir
            gts=gts_dir

    elif dataset_name=="cityscape":
        #Dataset support not implemented yet. 
        gts,imgs=[]
    else:
        raise ValueError("invalid dataset name")

    if len(gts)!=len(imgs):
        raise ValueError("Missing gt/img data")
    return imgs,gts




def get_data_split(imgs,gts,divide=[0.7,0.15,0.15], random=False):
    """ Split list in three/two sets depending on the size of the input list
        if the len(divide)==2, splits in train/test, otherwise train/test/val
        the format of the input is [train,val,test] or [train,test]
    """
    if sum(divide)!=1:
        raise ValueError("input split must sum up to 1")
    if random:
        gts_imgs = list(zip(imgs,gts))
        random.shuffle(gts_imgs)
        imgs,gts=zip(*gts_imgs)
    else:
        gts.sort()
        imgs.sort()
    if len(divide)==2:
        num_train=int(len(imgs)*divide[0])
        num_val=0
    elif len(divide)==3:
        num_train=int(len(imgs)*divide[0])
        num_val=int(len(imgs)*divide[1])
    else:
        raise ValueError("invalid input divide list")
    imgs_split=[imgs[:num_train],imgs[num_train:num_train+num_val],imgs[num_train+num_val:]]
    gts_split=[gts[:num_train],gts[num_train:num_train+num_val],gts[num_train+num_val:]]
    return imgs_split,gts_split



def convert_gts2cityscapes(base_dir_dataset, dataset_name, lbl_split, mode="train_id",size=(2048,1024)):
    split_names=['train','val','test']
    print("Converting Ground Truth images...")
    for idx,split in enumerate(lbl_split):
        split_dir=os.path.join(
            base_dir_dataset,
            dataset_name+"_standardized",
            "gt",
            split_names[idx])
        
        for file in tqdm(split,desc=split_names[idx]):
            im = Image.open(file)
            im=im.resize(size, Image.NEAREST)
            im=rgb_labels2cityscape(im,dataset_name,mode=mode)
            im.save(os.path.join(split_dir,os.path.basename(file)))

def is_split(list_files):
    """ Check if list images/ground truth are already split into train/val/test sets
        Returns True if the dataset is split in sets, False otherwise.
    """
    return any(isinstance(i, list) for i in list_files)
    
def prepare_dataset(base_dir_dataset,dataset_name,mode="train_id", size=(2048,1024)):
    imgs,lbs=get_label_img(base_dir_dataset,dataset_name)
    create_default_file_struct(base_dir_dataset, dataset_name)
    if not is_split(imgs):
        img_split,lbl_split=get_data_split(imgs,lbs)
    else:
        img_split=imgs
        lbl_split=lbs
    convert_gts2cityscapes(base_dir_dataset, dataset_name,lbl_split, mode, size)
    convert_imgs2cityscape(base_dir_dataset,dataset_name,img_split)
    save_sets_to_txt(base_dir_dataset,dataset_name)



def list_files_in_dir(directory,ext=""):
    """recursively list all files in a directory with a particular exention
    e.g. directory= /home/user/datasets, ext=".jpeg"
    """
    files = glob.glob(directory + '/**/*'+ext, recursive=True)
    files.sort()
    return files

def convert_imgs2cityscape(base_dir_dataset,dataset_name, img_split,size=(2048,1024)):
    split_names=['train','val','test']
    print("Resizing and copying source images...")
    for idx,split in enumerate(img_split):
        split_dir=os.path.join(
            base_dir_dataset,
            dataset_name+"_standardized",
            "images",
            split_names[idx])
        for file in tqdm(split,desc=split_names[idx]):
            im = Image.open(file)
            im=im.resize(size)
            im.save(os.path.join(split_dir,os.path.basename(file)))
        
def save_sets_to_txt(base_dir_dataset, dataset_name):
    """Save sets split in txt file with the ground truth
       e.g. /images/img_1.png,/gt/img_lbl_1.png
    """
    print("Saving data splits...")
    dir_dataset=os.path.join(
        base_dir_dataset,
        dataset_name+"_standardized"
    )
    path_all_files=[]
    for subfolder in ['train','val','test']:
        paths=[]
        for folder in ['gt','images']:
            dir= os.path.join(dir_dataset,folder,subfolder)
            list_files=list_files_in_dir(dir)
            list_files.sort()
            paths.append(list_files)
        paths=list(map(list, zip(*paths)))
        path_all_files.append(paths)
        
    for idx,set in enumerate(["trn.txt","val.txt","test.txt"]):
        with open(os.path.join(dir_dataset,"image_sets",set), 'w') as f:
            for img in path_all_files[idx]:
                f.write("{}, {}\n".format(img[0],img[1]))



path_dataset="/home/kubitz/Documents/fyp/dataset/graz_landing/semantic_drone_dataset"
path_aeroscapes="/home/kubitz/Documents/fyp/dataset/aeroscapes"
path_uavid="/home/kubitz/Documents/fyp/dataset/uavid_v1.5_official_release_image"
x=get_label_img(path_uavid,'uavid')
# Open input image and palettise to "inPalette" so each pixel is replaced by palette index
# ... so all black pixels become 0, all red pixels become 1, all green pixels become 2...
im = Image.open(r"/home/kubitz/Documents/fyp/UAV-Segmentation-Scripts/uavsegscripts/test.png") 
r = rgb_labels2cityscape(im,'graz',mode="label_id")
r.save('/home/kubitz/Documents/fyp/UAV-Segmentation-Scripts/uavsegscripts/resultTrain.png')
prepare_dataset("/home/kubitz/Documents/fyp/dataset/graz_landing/semantic_drone_dataset","graz")
create_default_file_struct("/home/kubitz/Documents/fyp/dataset/","graz")
ls= list_files_in_dir("/home/kubitz/Documents/fyp/dataset/graz_landing/semantic_drone_dataset/training_set/gt")
