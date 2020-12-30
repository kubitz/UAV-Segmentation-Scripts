from collections import namedtuple
from enum import IntEnum

class Category(IntEnum):
    void=0
    flat=1
    vehicle=3
    construction=4
    obstacle=5
    human=6
    vegetation=7
    water=8


Label = namedtuple( 'Label' , [

    'name'        , # The identifier of this label, e.g. 'car', 'person', ... .
                    # We use them to uniquely name a class

    'id'          , # An integer ID that is associated with this label.
                    # The IDs are used to represent the label in ground truth images
                    # An ID of -1 means that this label does not have an ID and thus
                    # is ignored when creating ground truth images (e.g. license plate).
                    # Do not modify these IDs, since exactly these IDs are expected by the
                    # evaluation server.

    'trainId'     , # Feel free to modify these IDs as suitable for your method. Then create
                    # ground truth images with train IDs, using the tools provided in the
                    # 'preparation' folder. However, make sure to validate or submit results
                    # to our evaluation server using the regular IDs above!
                    # For trainIds, multiple labels might have the same ID. Then, these labels
                    # are mapped to the same class in the ground truth images. For the inverse
                    # mapping, we use the label that is defined first in the list below.
                    # For example, mapping all void-type classes to the same ID in training,
                    # might make sense for some approaches.
                    # Max value is 255!

    'category'    , # The name of the category that this label belongs to

    'categoryId'  , # The ID of this category. Used to create ground truth images
                    # on category level.

    'hasInstances', # Whether this label distinguishes between single instances or not

    'ignoreInEval', # Whether pixels having this class as ground truth label are ignored
                    # during evaluations or not

    'color'       , # The color of this label
    ] )

# Aeroscapes
aeroscapes = [
    #       name                     id    trainId   category            catId                    hasInstances      ignoreInEval   color
    Label(  'background'            ,  0 ,      255 , 'void'            , Category.void.value       , False        , True         , (  0,  0,  0) ),
    Label(  'person'                ,  1 ,      255 , 'human'           , Category.human.value      , False        , True         , (  1,  1,  1) ),
    Label(  'bike'                  ,  2 ,      255 , 'human'           , Category.human.value      , False        , True         , (  2,  2,  2) ),
    Label(  'car'                   ,  3 ,      255 , 'vehicle'         , Category.vehicle.value    , False        , True         , (  3,  3,  3) ),
    Label(  'drone'                 ,  4 ,      255 , 'obstacle'        , Category.obstacle.value   , False        , True         , (  4,  4,  4) ),
    Label(  'boat'                  ,  5 ,      255 , 'vehicle'         , Category.obstacle.value   , False        , True         , (  5,  5,  5) ),
    Label(  'animal'                ,  6 ,      255 , 'object'          , Category.obstacle.value   , False        , True         , (  6,  6,  6) ),
    Label(  'obstacle'              ,  7 ,        0 , 'obstacle'        , Category.obstacle.value   , False        , False        , (  7,  7,  7) ),
    Label(  'construction'          ,  8 ,        1 , 'construction'    , Category.void.value       , False        , False        , (  8,  8,  8) ),
    Label(  'vegetation'            ,  9 ,      255 , 'vegetation'      , Category.vegetation.value , False        , True         , (  9,  9,  9) ),
    Label(  'road'                  , 10 ,      255 , 'flat'            , Category.flat.value       , False        , True         , ( 10, 10, 10) ),
    Label(  'sky'                   , 11 ,        2 , 'void'            , Category.void.value       , False        , False        , ( 11, 11, 11) ),
]

# TU Graz
graz = [
    # name (as shown in dataset)      id    trainId   category            catId                         hasInstances   ignoreInEval       color
    Label(  'unlabeled'             ,  0 ,      255 , 'void'            , Category.void.value           , False        , True         , (  0,  0,  0) ),
    Label(  'person'                ,  1 ,      255 , 'human'           , Category.human.value          , False        , True         , (255, 22, 96) ),
    Label(  'bicycle'               ,  2 ,      255 , 'human'           , Category.human.value          , False        , True         , (119, 11, 32) ),
    Label(  'car'                   ,  3 ,      255 , 'vehicle'         , Category.vehicle.value        , False        , True         , (  9,143,150) ),
    Label(  'water'                 ,  4 ,      255 , 'water'           , Category.water.value          , False        , True         , ( 28, 42,168) ),
    Label(  'pool'                  ,  5 ,      255 , 'water'           , Category.water.value          , False        , True         , (254,148, 12) ),
    Label(  'wall'                  ,  6 ,      255 , 'construction'    , Category.construction.value   , False        , True         , (102,102,156) ),
    Label(  'window'                ,  7 ,        0 , 'construction'    , Category.construction.value   , False        , False        , (254,228, 12) ),
    Label(  'roof'                  ,  8 ,        1 , 'construction'    , Category.construction.value   , False        , False        , ( 70, 70, 70) ),
    Label(  'vegetation'            ,  9 ,      255 , 'vegetation'      , Category.vegetation.value     , False        , True         , (107,142, 35) ),
    Label(  'paved-area'            , 10 ,      255 , 'flat'            , Category.flat.value           , False        , True         , (128, 64,128) ),
    Label(  'grass'                 , 11 ,        2 , 'flat'            , Category.flat.value           , False        , False        , (  0,102,  0) ),
    Label(  'gravel'                , 12 ,        2 , 'flat'            , Category.flat.value           , False        , False        , (112,103, 87) ),
    Label(  'dirt'                  , 13 ,        2 , 'flat'            , Category.flat.value           , False        , False        , (130, 76,  0) ),
    Label(  'rocks'                 , 14 ,        2 , 'obstacle'        , Category.obstacle.value       , False        , False        , ( 48, 41, 30) ),
    Label(  'obstacle'              , 15 ,        2 , 'obstacle'        , Category.obstacle.value       , False        , False        , (  2,135,115) ),
    Label(  'dog'                   , 16 ,        2 , 'obstacle'        , Category.obstacle.value       , False        , False        , (102, 51,  0) ),
    Label(  'fence'                 , 17 ,        2 , 'obstacle'        , Category.obstacle.value       , False        , False        , (190,153,153) ),
    Label(  'fence-pole'            , 18 ,        2 , 'obstacle'        , Category.obstacle.value       , False        , False        , (153,153,153) ),
    Label(  'conflicting'           , 19 ,        2 , 'void'            , Category.void.value           , False        , False        , (255,  0,  0) ),
    Label(  'ar-marker'             , 20 ,        2 , 'void'            , Category.void.value           , False        , False        , (112,150,146) ),
    Label(  'bald-tree'             , 21 ,        2 , 'vegetation'      , Category.vegetation.value     , False        , False        , (190,250,190) ),
    Label(  'tree'                  , 22 ,        2 , 'vegetation'      , Category.vegetation.value     , False        , False        , ( 51, 51,  0) ),
    Label(  'door'                  , 23 ,        0 , 'construction'    , Category.construction.value   , False        , False        , (254,148, 12) )
    
    ]

# UAVid
uavid = [
    #       name                     id    trainId   category            catId                          hasInstances      ignoreInEval   color
    Label(  'background-clutter'    ,  0 ,      255 , 'void'            , Category.void.value           , False        , True         , (  0,  0,  0) ),
    Label(  'human'                 ,  1 ,      255 , 'human'           , Category.human.value          , False        , True         , ( 64, 64,  1) ),
    Label(  'moving-car'            ,  3 ,      255 , 'vehicle'         , Category.vehicle.value        , False        , True         , ( 64,  0,128) ),
    Label(  'static-car'            ,  4 ,      255 , 'vehicle'         , Category.vehicle.value        ,  False       , True         , (192,  0,192) ),
    Label(  'building'              ,  5 ,      255 , 'construction'    , Category.construction.value   , False        , True         , (128,  0,  0) ),
    Label(  'road'                  ,  6 ,      255 , 'flat'            , Category.flat.value           , False        , True         , (128, 64,128) ),
    Label(  'tree'                  ,  7 ,        0 , 'vegetation'      , Category.vegetation.value     , False        , False        , (  0,128,  0) ),
    Label(  'low-vegetation'        ,  8 ,        1 , 'flat'            , Category.flat.value           , False        , False        , (128,128,  0) )

]

# Cityscape
cityscape = [
    #       name                     id    trainId   category            catId     hasInstances   ignoreInEval   color
    Label(  'unlabeled'            ,  0 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
    Label(  'ego vehicle'          ,  1 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
    Label(  'rectification border' ,  2 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
    Label(  'out of roi'           ,  3 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
    Label(  'static'               ,  4 ,      255 , 'void'            , 0       , False        , True         , (  0,  0,  0) ),
    Label(  'dynamic'              ,  5 ,      255 , 'void'            , 0       , False        , True         , (111, 74,  0) ),
    Label(  'ground'               ,  6 ,      255 , 'void'            , 0       , False        , True         , ( 81,  0, 81) ),
    Label(  'road'                 ,  7 ,        0 , 'flat'            , 1       , False        , False        , (128, 64,128) ),
    Label(  'sidewalk'             ,  8 ,        1 , 'flat'            , 1       , False        , False        , (244, 35,232) ),
    Label(  'parking'              ,  9 ,      255 , 'flat'            , 1       , False        , True         , (250,170,160) ),
    Label(  'rail track'           , 10 ,      255 , 'flat'            , 1       , False        , True         , (230,150,140) ),
    Label(  'building'             , 11 ,        2 , 'construction'    , 2       , False        , False        , ( 70, 70, 70) ),
    Label(  'wall'                 , 12 ,        3 , 'construction'    , 2       , False        , False        , (102,102,156) ),
    Label(  'fence'                , 13 ,        4 , 'construction'    , 2       , False        , False        , (190,153,153) ),
    Label(  'guard rail'           , 14 ,      255 , 'construction'    , 2       , False        , True         , (180,165,180) ),
    Label(  'bridge'               , 15 ,      255 , 'construction'    , 2       , False        , True         , (150,100,100) ),
    Label(  'tunnel'               , 16 ,      255 , 'construction'    , 2       , False        , True         , (150,120, 90) ),
    Label(  'pole'                 , 17 ,        5 , 'object'          , 3       , False        , False        , (153,153,153) ),
    Label(  'polegroup'            , 18 ,      255 , 'object'          , 3       , False        , True         , (153,153,153) ),
    Label(  'traffic light'        , 19 ,        6 , 'object'          , 3       , False        , False        , (250,170, 30) ),
    Label(  'traffic sign'         , 20 ,        7 , 'object'          , 3       , False        , False        , (220,220,  0) ),
    Label(  'vegetation'           , 21 ,        8 , 'nature'          , 4       , False        , False        , (107,142, 35) ),
    Label(  'terrain'              , 22 ,        9 , 'nature'          , 4       , False        , False        , (152,251,152) ),
    Label(  'sky'                  , 23 ,       10 , 'sky'             , 5       , False        , False        , ( 70,130,180) ),
    Label(  'person'               , 24 ,       11 , 'human'           , 6       , True         , False        , (220, 20, 60) ),
    Label(  'rider'                , 25 ,       12 , 'human'           , 6       , True         , False        , (255,  0,  0) ),
    Label(  'car'                  , 26 ,       13 , 'vehicle'         , 7       , True         , False        , (  0,  0,142) ),
    Label(  'truck'                , 27 ,       14 , 'vehicle'         , 7       , True         , False        , (  0,  0, 70) ),
    Label(  'bus'                  , 28 ,       15 , 'vehicle'         , 7       , True         , False        , (  0, 60,100) ),
    Label(  'caravan'              , 29 ,      255 , 'vehicle'         , 7       , True         , True         , (  0,  0, 90) ),
    Label(  'trailer'              , 30 ,      255 , 'vehicle'         , 7       , True         , True         , (  0,  0,110) ),
    Label(  'train'                , 31 ,       16 , 'vehicle'         , 7       , True         , False        , (  0, 80,100) ),
    Label(  'motorcycle'           , 32 ,       17 , 'vehicle'         , 7       , True         , False        , (  0,  0,230) ),
    Label(  'bicycle'              , 33 ,       18 , 'vehicle'         , 7       , True         , False        , (119, 11, 32) ),
    Label(  'license plate'        , -1 ,       -1 , 'vehicle'         , 7       , False        , True         , (  0,  0,142) )
]