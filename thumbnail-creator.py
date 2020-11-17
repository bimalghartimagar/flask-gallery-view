import os
from shutil import copyfile
from configparser import ConfigParser
import conf

from PIL import Image

def process_thumbnail_creation(gallery_path: str):

  if os.path.isdir(gallery_path):
    for folder in os.listdir(gallery_path):
      try:
        thumbnails_folder_path = f'{os.getcwd()}{os.sep}thumbnails{os.sep}{folder}'
        os.makedirs(thumbnails_folder_path, exist_ok=False)

        source_folder_path = f'{gallery_path}{os.path.sep}{folder}'
        for file in os.listdir(source_folder_path):
          if (os.path.splitext(file)[1]).lower() == '.jpg':
            source_file_path = f'{source_folder_path}{os.sep}{file}'
            source_image = Image.open(source_file_path)

            copy_of_source_image = source_image.copy()

            copy_of_source_image.thumbnail((1000, 1000))

            thumbnails_file_path = f'{thumbnails_folder_path}{os.sep}{file}'
            
            copy_of_source_image.save(thumbnails_file_path)

      except FileExistsError:
        continue

if __name__ == "__main__":
  config = ConfigParser()
  config.read_dict(conf.cfg)
  
  gallery_path = config.get('gallery_view', 'original_path')
  process_thumbnail_creation(gallery_path)
