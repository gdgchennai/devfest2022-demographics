import os

from gutils.services.api_client import GoogleApiClient
from gutils.services.enums import LoginType
from gutils.creds.google.service_account import ServiceAccountCreds
from gutils.services.spreadsheets.v4.objects.others import ValueRange


def update_sheet(sheet_id: str, data: ValueRange, worksheet_name: str) -> None:
    """update_sheet updates the give sheet with the given data

    Args:
        sheet_id (str): id of the sheet
        data (ValueRange): data to be updated
        worksheet_name (str): name of the worksheet
    """

    # G-Sheet service account config
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    config =  ServiceAccountCreds(
        project_id = os.getenv('GCP_PROJECT_ID'), 
        private_key_id = os.getenv('GCP_SERVICE_ACCOUNT_PRIVATE_KEY_ID'),
        private_key = os.getenv('GCP_SERVICE_ACCOUNT_PRIVATE_KEY'),
        client_email =os.getenv('GCP_SERVICE_ACCOUNT_CLIENT_EMAIL'),
        client_id = os.getenv('GCP_SERVICE_ACCOUNT_CLIENT_ID'),
        client_x509_cert_url = os.getenv('GCP_SERVICE_ACCOUNT_CLIENT_CERT_URL')
    )

    client = GoogleApiClient(scopes=scopes, config=config, login_type=LoginType.SERVICE_ACCOUNT)
    client.initialize()
    service = client.create_service("sheets", "v4")

    service.update_values(spreadsheet_id = sheet_id, body = data, sheet_range = worksheet_name)
