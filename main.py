# Updated Project Structure for Testing

## 1. **`main.py`** (Entry Point)

from rich.console import Console
from ui.main_window import MainWindow
from core.google_ads_client import initialize_google_ads
from utils.logger import setup_logging

console = Console()

if __name__ == "__main__":
    try:
        # Initialize rich logging
        setup_logging(console)
        console.rule("[bold blue]Starting Google Ads Bot[/bold blue]")

        # Initialize Google Ads API Client
        google_ads_client = initialize_google_ads()
        console.log("[green]Google Ads Client initialized successfully.[/green]")

        # Start the Main Window (placeholder functionality for UI demo)
        main_window = MainWindow(console)
        main_window.start()

    except Exception as e:
        console.log(f"[red]An error occurred: {e}[/red]")
