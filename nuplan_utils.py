
from nuplan.database.nuplan_db_orm.nuplandb_wrapper import NuPlanDBWrapper


def get_all_scenario_metadata(db_file_name:str) -> dict:
    """
    using a db file, returns all the metadata that is needed to to create scenario object. 
    """
    
    db_file = NuPlanDBWrapper(db_file_name)
    
    return {}