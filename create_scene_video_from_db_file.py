import os
from collections import defaultdict
import cv2 
from nuplan.database.nuplan_db_orm.nuplandb_wrapper import NuPlanDBWrapper
from tqdm import tqdm 
import pathlib 
import argparse




    

def main():
    parser = argparse.ArgumentParser()
    
    
    
    
    
    parser.add_argument("--db_file_name")
    args = parser.parse_args()
    
    
    
    NUPLAN_DATA_ROOT = os.getenv('NUPLAN_DATA_ROOT', '/home/deo-abhijit/NuPlan/dataset')
    NUPLAN_MAPS_ROOT = os.getenv('NUPLAN_MAPS_ROOT', '/home/deo-abhijit/NuPlan/maps')
    NUPLAN_DB_FILES = os.getenv('NUPLAN_DB_FILES', "/home/deo-abhijit/NuPlan/dataset/nuplan-v1.1/splits/mini")
    NUPLAN_MAP_VERSION = os.getenv('NUPLAN_MAP_VERSION', 'nuplan-maps-v1.0')



    nuplandb_wrapper = NuPlanDBWrapper(
        data_root=NUPLAN_DATA_ROOT,
        map_root=NUPLAN_MAPS_ROOT,
        db_files=NUPLAN_DB_FILES,
        map_version=NUPLAN_MAP_VERSION,
    )

    db_file_name = args.db_file_name
    log_db = nuplandb_wrapper.get_log_db(db_file_name)
    mapping_ = defaultdict(str)
    for i in log_db.scenario_tag:
        mapping_[i.lidar_pc_token] = i.type

    images = defaultdict(list)
    for i in tqdm(log_db.image):
        images[i.camera.channel].append([i.filename_jpg, mapping_[i.lidar_pc.token]])
    print(images.keys())

    NUPLAN_DATA_ROOT = pathlib.Path(NUPLAN_DATA_ROOT)

    sensor_blob_path = pathlib.Path("/home/deo-abhijit/NuPlan/dataset/nuplan-v1.1/sensor_blobs")
    

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    video_path = f"{db_file_name}_video.mp4"
    video = cv2.VideoWriter(video_path, fourcc, 10, (1920,1080), True)
    #zip_object = zip([images[i] for i in cams])
    counter = 0
    for i in tqdm(images['CAM_F0']):
        counter +=1 
        data_path= sensor_blob_path/f"{i[0]}"
        data = cv2.imread(str(data_path))
        text = i[1]
        
        font = cv2.FONT_HERSHEY_SIMPLEX  
        org = (50, 50) 
        fontScale = 1
        color = (255, 0, 0) 
        thickness = 2
        
        data = cv2.putText(data, text, org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 

        

        video.write(data)

    video.release()


if __name__ == "__main__":
    #python create_scene_video_from_db_files.py --db_file_name 2021.07.16.18.06.21_veh-38_04933_05307 --cams 
    main()
    
    """
    image = cv2.imread(path) 
    font = cv2.FONT_HERSHEY_SIMPLEX  
    org = (50, 50) 
    fontScale = 1
    color = (255, 0, 0) 
    thickness = 2
   
# Using cv2.putText() method 
image = cv2.putText(image, 'OpenCV', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
    """