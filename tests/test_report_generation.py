import unittest
from core.report_generation import generate_daily_report
from core.google_ads_client import initialize_google_ads

class TestReportGeneration(unittest.TestCase):
    def test_generate_daily_report(self):
        client = initialize_google_ads()
        campaign_resource_name = "RESOURCE_NAME"
        csv_file = generate_daily_report(client, campaign_resource_name)
        self.assertTrue(csv_file.endswith('.csv'))

if _name_ == '_main_':
    unittest.main()