from PyQt5.QtCore import QThread, pyqtSignal
import schedule
import time
from core.campaign_creation import create_campaign
from core.report_generation import generate_daily_report
from core.google_ads_client import initialize_google_ads

class Worker(QThread):
    update_progress = pyqtSignal(int)
    update_log = pyqtSignal(str)

    def run(self):
        self.schedule_campaign_creation()

    def schedule_campaign_creation(self):
        schedule.every().day.at("09:00").do(self.create_campaign)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def create_campaign(self):
        client = initialize_google_ads()
        campaign_resource_name = create_campaign(client)
        self.update_log.emit(f"Created campaign with resource name: {campaign_resource_name}")
        self.update_progress.emit(100)
        csv_file = generate_daily_report(client, campaign_resource_name)
        self.update_log.emit(f"Daily report saved to {csv_file}")