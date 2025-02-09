# my_project/core/campaign_creation.py
def create_campaign(api_client, campaign_data):
    try:
        campaign_service = api_client.get_service("CampaignService")
        operation = campaign_service.mutate_campaigns(
            customer_id=campaign_data['customer_id'],
            operations=campaign_data['operations'],
        )
        return operation
    except Exception as e:
        raise RuntimeError(f"Error creating campaign: {str(e)}")