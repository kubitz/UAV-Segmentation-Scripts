# UAV-segmentation scripts
Collection of scripts for  preparation of datasets for semantic segmentation of UAV images

Those scripts were used to prepare and unify multiple datasets used to train a semantic segmetation model used in an Automatic Safe Emergency Landing application. 


## Datasets Overview

| Dataset       | Number of images | Number of classes | Description                                                     | Perspective          |
| --------------- | ---------------- | ----------------- | --------------------------------------------------------------- | -------------------- |
| [Cityscape (2D fine)](https://www.cityscapes-dataset.com/)| 5000 (50 seq)    | 30 | High-quality autonomous driving segmentation (not UAV)  | Ground Level         |
| [Aerospace](https://cutt.ly/phMhtsN)       | 3269  | 11  | images captured from commercial drone (5 to 50 meters altitude) | Mixed (forward/down) |
| [TU-GRAZ landing](https://cutt.ly/GhMhawL) | 592 | 20   | Segmentation for Urban environment for safe landing              | down                 |
| [UAVid](https://uavid.nl/)| 420 (42 seq)     | 8                 | Segmentation for Urban environment                              | forward              |


## Common Labels across datasets

| Dataset \ Labels    | road         | person | vehicle              | building | vegetation          | background |
|---------------------|--------------|--------|----------------------|----------|---------------------|------------|
| Cityscape (not UAV) | [x]          | [x]    | [x] (bus/truck/car)   | [x]      | - [x]                 | [x]        |
| Aerospace           | [x]          | [x]    | [x]                  | [x]      | [x]                 | [x]        |
| TU-GRAZ landing     | [x] (gravel) | [x]    | [x]                  | [x]      | [x] (tree/gras)     | [x]        |
| UAVid               | [x]          | [x]    | [x] (static/dynamic) | [x]      | [x] (tree/low veg.) | [x]        |

