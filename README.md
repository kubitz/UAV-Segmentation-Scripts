# UAV-segmentation scripts
Collection of scripts for  preparation of datasets for semantic segmentation of UAV images

Those scripts were used to prepare and unify multiple datasets used to train a semantic segmetation model used in an Automatic Safe Emergency Landing application. 
It converts all of the supported datasets to a cityscape type structure. This is useful as most semantic segmentation repos out there support Cityscape. On top of this, this repo supports re-labelling. This means you can group and discard annotations. This is particularly useful when combining several datasets together. 

## User Guide

1. Download one/several of the datasets supported.
2. Update the configuration file:
    * `DATASETS_PATHS`: this should contain the root directory to the datasets.
    * `size_out`: all the labels/images will be resized to the value you enter here.
    * `use_default_split`: If `True`, the data splits given by the dataset authors will be used. Otherwise (or if the authors did not specify sets), a split will be generated (70/15/15). You can change the proportion of the data splits in `dataset_prep.py`
    * `use_train_ids`: if True, the `trainIds` will be used instead of the `labelIds`. For more details on the difference between the two. Please refer to `labels.py`
3. (optional) Create virtual environment
4. `pip3 install -r requirements.txt`
4. `python3 setup.py install`
5. Run `python3 scripts/run.py --dataset [insert dataset_name]`
6. Feel free raise an Issue, star, or do PRs :)
   

## Supported Dataset

| Dataset       | Number of images | Number of classes | Description                                                     | Perspective          |
| --------------- | ---------------- | ----------------- | --------------------------------------------------------------- | -------------------- |
| [Cityscape (2D fine)](https://www.cityscapes-dataset.com/)*| 5000 (50 seq)    | 30 | High-quality autonomous driving segmentation (not UAV)  | Ground Level         |
| [Aerospace](https://cutt.ly/phMhtsN)       | 3269  | 11  | images captured from commercial drone (5 to 50 meters altitude) | Mixed (forward/down) |
| [TU-GRAZ landing](https://cutt.ly/GhMhawL) | 592 | 20   | Segmentation for Urban environment for safe landing              | down                 |
| [UAVid](https://uavid.nl/)| 420 (42 seq)     | 8                 | Segmentation for Urban environment                              | forward              |

*Cityscape still being implemented. However, you can just refer to this [repo](https://github.com/mcordts/cityscapesScripts) in the meanwhile.

## Common Labels across datasets

| Dataset \ Labels    | road                        | person             | vehicle                             | building           | vegetation                         | background         |
|---------------------|-----------------------------|--------------------|-------------------------------------|--------------------|------------------------------------|--------------------|
| Cityscape (not UAV) | :heavy_check_mark:          | :heavy_check_mark: (person/rider)| :heavy_check_mark: (bus/truck/car)  | :heavy_check_mark: |  :heavy_check_mark:               | :heavy_check_mark: |
| Aerospace           | :heavy_check_mark:          | :heavy_check_mark: | :heavy_check_mark:                  | :heavy_check_mark: | :heavy_check_mark:                 | :heavy_check_mark: |
| TU-GRAZ landing     | :heavy_check_mark: (gravel) | :heavy_check_mark: | :heavy_check_mark:                  | :heavy_check_mark: (door/window/roof/wall)| :heavy_check_mark:(tree/gras)     | :heavy_check_mark: |
| UAVid               | :heavy_check_mark:          | :heavy_check_mark: | :heavy_check_mark: (static/dynamic) | :heavy_check_mark: | :heavy_check_mark: (tree/low veg.) | :heavy_check_mark: |

## Credits
Some of the code (particularly `label.py`) was based on this [repo](https://github.com/mcordts/cityscapesScripts).
