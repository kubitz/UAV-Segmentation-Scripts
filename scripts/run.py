from uavsegscripts import dataset_prep
import configparser
import argparse
import os

parser = argparse.ArgumentParser(description='Convert datasets to Cityscape format')
parser.add_argument('--dataset', choices=['graz', 'uavid', 'aeroscape'],
                    action='store', dest='dataset_name',
                    help='chose dataset to process', required=True)
parser.add_argument('--mode', choices=['train_id','label_id'], default='train_id',
                    action='store', dest='mode',
                    help='chose whether the output labels are based on the trainIds or labelIds (see labels.py for more info')
parser.add_argument('--use_default_split', type=bool, default=True,
                    action='store', dest='use_default_split',
                    help='use splits by dataset authors, or re-split data in 70-15-15')

args = parser.parse_args()

os.chdir('..')
ini_path = os.path.join(os.getcwd(),'config','default_config.ini')
config = configparser.ConfigParser()                                     
config.read(ini_path)
path=config.get('DATASET_PATHS',args.dataset_name)

dataset_prep.prepare_dataset(path,args.dataset_name,mode=args.mode,use_default_split=args.use_default_split)
