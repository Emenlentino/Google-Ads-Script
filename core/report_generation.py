import pandas as pd
from datetime import datetime
from rich.console import Console

def generate_daily_report(client, campaign_resource_name):
    console = Console()
    query = f"""
    SELECT
      campaign.id,
      campaign.name,
      metrics.impressions,
      metrics.clicks,
      metrics.cost_micros,
      metrics.conversions,
      metrics.conversion_rate
    FROM
      campaign
    WHERE
      campaign.resource_name = '{campaign_resource_name}'
    """
    response = client.service.google_ads.search_stream(customer_id='YOUR_CUSTOMER_ID', query=query)

    report_data = []
    for batch in response:
        for row in batch.results:
            campaign = row.campaign
            metrics = row.metrics
            report_data.append({
                'Campaign ID': campaign.id.value,
                'Campaign Name': campaign.name.value,
                'Impressions': metrics.impressions,
                'Clicks': metrics.clicks,
                'Cost (Micros)': metrics.cost_micros,
                'Conversions': metrics.conversions,
                'Conversion Rate': metrics.conversion_rate,
                'Date': datetime.now().strftime('%Y-%m-%d')
            })

    df = pd.DataFrame(report_data)
    csv_file = 'daily_campaign_report.csv'
    df.to_csv(csv_file, mode='a', index=False, header=not pd.read_csv(csv_file).empty)
    console.log(f"[bold blue]Daily report saved to {csv_file}[/bold blue]")
    return csv_file