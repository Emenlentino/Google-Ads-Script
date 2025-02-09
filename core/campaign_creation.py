from rich.console import Console

def create_campaign(client):
    console = Console()
    campaign_operation = client.get_type('CampaignOperation', version='v8')
    campaign = campaign_operation.create

    campaign.name = 'Automated Campaign'
    campaign.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
    campaign.status = client.enums.CampaignStatusEnum.PAUSED

    response = client.service.campaign.mutate_campaigns(
        customer_id='YOUR_CUSTOMER_ID',
        operations=[campaign_operation]
    )

    campaign_resource_name = response.results[0].resource_name
    console.log(f"[bold green]Created campaign with resource name: {campaign_resource_name}[/bold green]")
    return campaign_resource_name