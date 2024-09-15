import requests

# Terra API settings
API_URL = 'https://api.tryterra.co/v2'
API_KEY = 'your_terra_api_key_here'
AUTH_TOKEN = 'user_auth_token'  # You will get this after user authorization

# Function to get user's wearable data
def get_wearable_data(endpoint, token):
    headers = {
        'Authorization': f'Bearer {token}',
        'X-API-Key': API_KEY
    }
    response = requests.get(f'{API_URL}/{endpoint}', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

# Example: Retrieve daily activity data
activity_data = get_wearable_data('activity', AUTH_TOKEN)
print(activity_data)
