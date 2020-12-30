from labels import labels_graz, labels_aero
import numpy as np
import cv2
from PIL import Image  


def customTone(image, lut):
    """ 이미지에 Custom된 Look-Up-Table을 적용
    Keyword arguments:
    lut -- Red에 해당하는 arg, 1.0을 기준으로 클수록 강조됨.
    """
    rgb, alpha = image[:,:,:3], image[:,:,3:]

    r_channel = cv2.LUT(rgb[:,:,0], lut[:,0])
    g_channel = cv2.LUT(rgb[:,:,1], lut[:,1])
    b_channel = cv2.LUT(rgb[:,:,2], lut[:,2])
    applied =  np.stack([r_channel,g_channel,b_channel],axis=-1)

    result = np.concatenate([applied, alpha],axis=-1)
    return result

palette_in=[]
palette_out=[]
for l in labels_graz:
    palette_in.append(l.color)
    palette_out.append([l.id,l.id,l.id])

  
# opening a  image  
im = Image.open(r"/home/kubitz/Documents/fyp/UAV-Segmentation-Scripts/uavsegscripts/test.png") 

# use getpallete 
im2 = im.getpalette() 
print(im2) 


palette_in= np.array(palette_in).ravel()
palette_out= np.array(palette_out).ravel()

img = cv2.imread('/home/kubitz/Documents/fyp/UAV-Segmentation-Scripts/uavsegscripts/test.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lut = np.zeros(shape=(256,3))
for label in labels_graz:
    for channel in label.color:
        lut[label.color[channel]][channel] = label.id
    
r, g, b = cv2.split(img)

newR = cv2.LUT(r, lut)
newG = cv2.LUT(g, lut)
newB = cv2.LUT(b, lut)

new = cv2.merge((newR, newG, newB))
cv2.imwrite("Q4_Imagem4bits.jpg", new)



