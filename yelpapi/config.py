import os
import sys
from decouple import config
form utils import postgres_helper 


class Config
    """
    Base config for Staging API
    """
    db_conn = create_connection()
    
class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True
    
def get_config():
    """Set default config to ProductionConfig unless STAGING environment
    is set to false on Linux `export STAGING=False` or Windows Powershell
    `$Env:STAGING="False"`. Using os.environ directly will throw errors
    if not set.
    For pytest, plesae use ProductionConfig
    """
    if os.getenv("STAGING"):
        STAGING = os.getenv("STAGING")
    else:
        STAGING = "False"

    if STAGING == "True":
        return DevelopmentConfig()

    return ProductionConfig()