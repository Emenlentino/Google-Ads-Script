# AI-Powered Google Ads Automation

This project leverages AI-powered analytics, dynamic campaign management, and a user-friendly GUI to automate interactions with the Google Ads API. The tool empowers users to efficiently manage, monitor, and optimize their Google Ads campaigns with predictive insights and detailed reporting.

## Features

- **AI-Powered Analytics**: Integrates machine learning to predict campaign performance and optimize strategies.
- **Dynamic Campaign Management**: Automates campaign creation and adjustments based on real-time market data.
- **Modern GUI**: A sleek, intuitive interface for visualizing progress and interacting with campaign data.
- **Rich Text Logs**: Enhanced logging for better clarity and tracking.
- **Automated Reporting**: Generates and saves detailed campaign performance reports in CSV format.
- **Scheduling**: Automates campaign and reporting tasks for seamless daily execution.

## Key Structure

```plaintext
my_project/
├── main.py
├── config/
│   └── google_ads.yaml
├── core/
│   ├── campaign_creation.py
│   ├── report_generation.py
│   └── google_ads_client.py
├── ai/
│   └── predictive_model.py
├── tests/
│   ├── test_campaign_creation.py
│   └── test_report_generation.py
├── ui/
│   ├── main_window.py
│   └── worker.py
├── utils/
│   ├── logging.py
│   └── config_loader.py
└── requirements.txt
```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/Google-Ads-Bot.git
   cd Google-Ads-Bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the Google Ads API**:
   - Update the `config/google_ads.yaml` file with your Google Ads credentials and configuration.

## Usage

1. **Run the Application**:
   ```bash
   python main.py
   ```

2. **Features via GUI**:
   - Monitor campaign progress.
   - Generate performance reports.
   - Manage campaigns dynamically.

## Testing

Run the test suite to ensure all components work as expected:
```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **PyQt5** for the GUI framework.
- **Google Ads API** for campaign management tools.
- **Rich** library for enhanced terminal output.

---

> "Technology is best when it brings people together." - Matt Mullenweg

