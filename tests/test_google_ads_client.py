## 10. **`tests/test_google_ads_client.py`** (Test Google Ads Client)

import unittest
from core.google_ads_client import initialize_google_ads

class TestGoogleAdsClient(unittest.TestCase):
    def test_initialize_google_ads(self):
        try:
            client = initialize_google_ads()
            self.assertIsNotNone(client)
        except Exception as e:
            self.fail(f"Initialization failed: {e}")

if __name__ == "__main__":
    unittest.main()
