import httpx
from functools import wraps

# HTTPX object
limits = httpx.Limits(max_keepalive_connections=35, max_connections=77)
timeout = httpx.Timeout(10.0, read=None)
super_httpx = httpx.Client(limits=limits, timeout=timeout)
# HTTPX

def http_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except httpx.RequestError as e:
            # Handle network-related errors here
            print(f"An error occurred while making a request: {e}")
        except httpx.HTTPStatusError as e:
            # Handle HTTP status errors (e.g., 4XX, 5XX responses) here
            print(f"Request returned an unfavorable HTTP status: {e.response.status_code}")
        except httpx.TimeoutException as e:
            # Handle timeout errors here
            print("The request timed out.")
        except Exception as e:
            # Handle other exceptions that may occur
            print(f"An unexpected error occurred: {e}")
        # Return None or some default value/error indication if needed
        return None
    return wrapper

@http_error_handler
def fetch_data(url):
    response = super_httpx.get(url)  # Use the super_httpx client here
    response.raise_for_status()  # This will raise HTTPStatusError for 4XX and 5XX responses
    return response.json()

# Example call
result = fetch_data("https://example.com")
print(result)
