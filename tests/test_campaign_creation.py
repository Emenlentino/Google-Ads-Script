import unittest
from core.campaign_creation import create_campaign
from core.google_ads_client import initialize_google_ads

class TestCampaignCreation(unittest.TestCase):
    def test_create_campaign(self):
        client = initialize_google_ads()
        campaign_resource_name = create_campaign(client)
        self.assertIsNotNone(campaign_resource_name)

if _name_ == '_main_':
    unittest.main()