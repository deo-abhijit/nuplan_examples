import os 
from nuplan.database.nuplan_db_orm.nuplandb_wrapper import NuPlanDBWrapper

NUPLAN_DATA_ROOT = os.getenv('NUPLAN_DATA_ROOT', '/home/deo-abhijit/NuPlan/dataset')
NUPLAN_MAPS_ROOT = os.getenv('NUPLAN_MAPS_ROOT', '/home/deo-abhijit/NuPlan/maps')
NUPLAN_DB_FILES = os.getenv('NUPLAN_DB_FILES', "/home/deo-abhijit/NuPlan/dataset/nuplan-v1.1/splits/mini")
NUPLAN_MAP_VERSION = os.getenv('NUPLAN_MAP_VERSION', 'nuplan-maps-v1.0')



class Nuplan:
    def __init__(self, dataroot, mapsroot, db_files, map_version):
        
        self.db_wrapper = NuPlanDBWrapper(dataroot, mapsroot, db_files,map_version)
        
        for i in self.db_wrapper.log_dbs:
            print(i)
            break
        self._log = {}
        self._scene = {}
        self._lidar_pc = {}
        self._ego_pose = {}
        self._camera = {}
        self._image ={}
        self._lidar_box = {}
        self._traffic_light_status = {}
        self._lidar = {}
        self._scenario_tag = {}
        self._track = {}
        self._category = {}
        
        self.mappings = [self._log,
        self._scene ,
        self._lidar_pc ,
        self._ego_pose ,
        self._camera ,
        self._image ,
        self._lidar_box ,
        self._traffic_light_status ,
        self._lidar ,
        self._scenario_tag ,
        self._track ,
        self._category, 
        ]
            
    def _update_mappings(self, db_file):
        
        log_db = self.db_wrapper.get_log_db(db_file)
        
        self._log[log_db.log.token] = small_fn(log_db.log)
        
        for x in log_db.scene:
            self._scene[x.token] = small_fn(x)
            
        
        self._scene[log_db.scene.token] = small_fn(log_db.scene)
        self._lidar_pc[log_db.lidar_pc.token] = small_fn(log_db.lidar_pc)
        self._log[log_db.log.token] = small_fn(log_db.log)
        self._log[log_db.log.token] = small_fn(log_db.log)
        self._log[log_db.log.token] = small_fn(log_db.log)
        
    def _convert_to_dict(self,x):
                

def small_fn(x):
    tmp = {}
    for i in str(x).strip().split():
        key, val = map(str.strip, i.split(":"))
        tmp[key] = val 
    return tmp

def conver_log_to_mapping():
    pass 

        
"""

category            : 7
camera              : 8
lidar               : 1
ego_pose            : 51152
image               : 40800
lidar_pc            : 10200
track               : 6460
lidar_box           : 1280922
scene               : 26
scenario_tag        : 13812
traffic_light_status: 96994
"""

        
if __name__ =="__main__":
    nuplan = Nuplan(NUPLAN_DATA_ROOT, NUPLAN_MAPS_ROOT, NUPLAN_DB_FILES, NUPLAN_MAP_VERSION)