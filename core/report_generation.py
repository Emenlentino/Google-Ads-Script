# my_project/core/report_generation.py
def generate_report(api_client, report_query):
    try:
        report_service = api_client.get_service("GoogleAdsService")
        response = report_service.search(
            customer_id=report_query['customer_id'],
            query=report_query['query']
        )
        return [row for row in response]
    except Exception as e:
        raise RuntimeError(f"Error generating report: {str(e)}")