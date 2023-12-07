
import yaml

def load_config(CONFIG_FILE_PATH):
    with open(CONFIG_FILE_PATH, 'r') as stream:
        try:
            config_data = yaml.safe_load(stream)
            return config_data
        except yaml.YAMLError as e:
            print(f"Error loading YAML file: {e}")
            return None


if __name__ == "__main__":
    # config is a dict
    # config={'RDS_HOST':'database_host'}
    config = load_config(CONFIG_FILE_PATH)

    if config:
        # Access data from the loaded YAML file
       
        database_host = config.get('RDS_HOST', 'default_host')
        database_password = config.get('RDS_PASSWORD', 'default_password')
        database_user=config.get('RDS_USER','default_user')
        database_dbname=config.get('RDS_DATABASE','default_database')
        database_port=config.get('RDS_PORT','default_port')
        print(config)
       