import requests
import pytest
from utils.config_reader import ConfigReader
from utils.api_helper import APIHelper
  
@pytest.mark.api
class TestAPI:
    def test_get_users_contains_michael(self):
      self.api = APIHelper(ConfigReader.get_api_url())
      resp = self.api.call_get_api("/users/1")
      print(f'kết quả trả về :{resp}')
    #   assert resp.status_code == 200    
      
      email = resp.get("email")
      assert email == "Sincere@april.biz"
