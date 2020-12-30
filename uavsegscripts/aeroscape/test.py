import numpy as np
from PIL import Image

from labels import labels_graz, labels_aero

def get_palette(dataset):
    """Takes a datset label format. Returns a palette based on the color specified

    Args:
        dataset (label): label for dataset. See labels.py for more details

    Returns:
        list of ints: palette
    """
    palette=[]
    for label in dataset:
        palette.extend(label.color)
    return palette

def get_id_palette(dataset, mode='label_id'):
    """Takes a datset label format. Returns a palette based on the label_id/trainId specified

    Args:
        dataset (label): label for dataset. See labels.py for more details

    Returns:
        list of ints: palette
    """
    palette=[]
    if mode=='label_id':
        for label in dataset:
            palette.extend((label.id,label.id,label.id))
    elif mode=='train_id':
         for label in dataset:
            palette.extend((label.trainId,label.trainId,label.trainId))       
    else:
        raise ValueError('Invalid Mode')
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
    img_out = QuantizeToGivenPalette(img,inPalette)
    img_out.putpalette(outPalette)
    return img_out

def rgbLabels2Cityscape(img,dataset, mode='label_id'):
    """Converts an image labelled by colors to an image labelled by either label id or train ids (like the cityscape dataset)

    Args:
        img (pillow RGB img): input image labelled by colors
        dataset (list of named tuples): labels for dataset. See labels.py for details. 
        mode (str, optional): Specifies if the output image will be labelled based on the label ids or trainIds.
        Defaults to 'label_id'.

    Returns:
        pillow image: re-labelled image
    """
    inPalette=get_palette(labels)
    outPalette=get_id_palette(labels, mode=mode)
    outPalette += (768-len(outPalette))*[0]
    img=remap_img_colors(img,inPalette,outPalette)
    return img


def QuantizeToGivenPalette(im, palette):
    """Quantize image to a given palette.

    The input image is expected to be a PIL Image.
    The palette is expected to be a list of no more than 256 R,G,B values."""

    e = len(palette)
    assert e>0,    "Palette unexpectedly short"
    assert e<=768, "Palette unexpectedly long"
    assert e%3==0, "Palette not multiple of 3, so not RGB"

    # Make tiny, 1x1 new palette image
    p = Image.new("P", (1,1))

    # Zero-pad the palette to 256 RGB colours, i.e. 768 values and apply to image
    palette += (768-e)*[0]
    p.putpalette(palette)

    # Now quantize input image to the same palette as our little image
    return im.convert("RGB").quantize(palette=p)


def reset_trainId(dataset):
    """Resets all the trainIds to different numbers

    """


# Open input image and palettise to "inPalette" so each pixel is replaced by palette index
# ... so all black pixels become 0, all red pixels become 1, all green pixels become 2...
im = Image.open(r"/home/kubitz/Documents/fyp/UAV-Segmentation-Scripts/uavsegscripts/test.png") 
r=rgbLabels2Cityscape(im,labels_graz)
r.save('/home/kubitz/Documents/fyp/UAV-Segmentation-Scripts/uavsegscripts/result.png')

