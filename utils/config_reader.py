import json #Dùng để đọc file .json,    Chuyển nội dung JSON → Python dictionary
import os   #Dùng để làm việc với đường dẫn file
 
class ConfigReader: #Lưu nội dung file testsetting.json sau khi load
    _config = None
   
    @staticmethod #Gọi trực tiếp qua class , Không cần tạo object . VD config = ConfigReader()  
    def load_config():
        """Load configuration from testsetting.json if not already loaded"""
        if ConfigReader._config is None: #Nếu chưa load config thì mới đọc file
            # Xác định đường dẫn tới file testsetting.json
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testsetting.json') 
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config
   
    @staticmethod # goi truc tiep
    def get_base_url():
        """Get the base URL from the configuration"""
        return ConfigReader.load_config()['base_url']
    
    @staticmethod
    def get_api_url():
        return ConfigReader.load_config()['api_url']

    @staticmethod
    def get_username():
        """Get the username from the configuration"""
        return ConfigReader.load_config()['credentials']['username']
   
    @staticmethod
    def get_password():
        """Get the password from the configuration"""
        return ConfigReader.load_config()['credentials']['password']
    
    @staticmethod 
    def get_timeout():
        return ConfigReader.load_config()['timeout']