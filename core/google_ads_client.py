## 5. **`core/google_ads_client.py`** (Google Ads Client Initialization)

from google.ads.googleads.client import GoogleAdsClient
from utils.config_loader import load_config
from rich.console import Console

console = Console()

def initialize_google_ads(config_path="config/google_ads.yaml"):
    config = load_config(config_path)

    # Ensure "use_proto_plus" key is present
    if "use_proto_plus" not in config:
        console.log("[yellow]Adding 'use_proto_plus' key to configuration.[/yellow]")
        config["use_proto_plus"] = True  # Default to True; adjust if needed

    try:
        # Initialize the Google Ads API Client
        client = GoogleAdsClient.load_from_dict(config)
        return client
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Google Ads Client: {e}")
