from google.ads.googleads.client import GoogleAdsClient

def initialize_google_ads():
    client = GoogleAdsClient.load_from_storage('config/google_ads.yaml')
    return client