## 9. **`tests/test_config_loader.py`** (Test Configuration Loader)

import unittest
from utils.config_loader import load_config

class TestConfigLoader(unittest.TestCase):
    def test_load_config(self):
        config = load_config("config/google_ads.yaml")
        self.assertIn("developer_token", config)

if __name__ == "__main__":
    unittest.main()
