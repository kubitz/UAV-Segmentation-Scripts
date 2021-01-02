from uavsegscripts import dataset_prep
import configparser
config = configparser.ConfigParser()                                     
config.read('config/default_config.ini')

dataset_to_prep="graz"
use_default_split=config.get("OUTPUT_SETTINGS","use_default_split")
use_train_ids=config.get("OUTPUT_SETTINGS","use_train_ids")

if use_train_ids:
    mode='train_id'
else:
    mode='label_id'

dataset_prep.prepare_dataset(config.get("DATASET_PATHS",dataset_prep),dataset_prep,mode=mode,use_default_split=use_default_split)

