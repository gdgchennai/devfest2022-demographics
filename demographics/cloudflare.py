import os

import requests


def update_counter(count: str | int) -> None:
    """update_counter updates the counter in the cloudflare KV store

    Args:
        count (str | int): The value of the key `count`
    """
    email = os.getenv('CLOUDFLARE_EMAIL')
    api_key = os.getenv('CLOUDFLARE_API_TOKEN')
    account_id = os.getenv('CLOUDFLARE_ACCOUNT_ID')
    namespace_id = os.getenv('CLOUDFLARE_NAMESPACE_ID')
    key = "count"
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/storage/kv/namespaces/{namespace_id}/values/{key}"
    headers = {
        "X-Auth-Email": email,
        "X-Auth-Key": api_key,
        "Content-Type": "text/plain"
    }
    try:
        requests.put(url, headers=headers, data=str(count))        
    except Exception:
        print("Error updating KV store")
