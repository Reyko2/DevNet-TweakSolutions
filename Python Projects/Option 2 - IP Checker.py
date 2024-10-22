import requests
import json


def get_ip_info():
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()

        if 'error' in data:
            print("Error: Unable to retrieve IP information.")
            return None

        return {
            'ip': data['ip'],
            'city': data['city'],
            'region': data['region'],
            'country': data['country_name'],
            'ipv6': data.get('ipv6', 'Not available'),
            'isp': data['org'],
            'asn': data['asn'],
            'lat': data['latitude'],
            'lon': data['longitude']
        }
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def display_ip_info(ip_info):
    print("\n--- IP Address Information ---")
    print(f"IPv4 Address: {ip_info['ip']}")
    print(f"IPv6 Address: {ip_info['ipv6']}")
    print(f"Location: {ip_info['city']}, {ip_info['region']}, {ip_info['country']}")
    print(f"ISP: {ip_info['isp']}")
    print(f"ASN: {ip_info['asn']}")
    print(f"Latitude: {ip_info['lat']}, Longitude: {ip_info['lon']}")


if __name__ == '__main__':
    print("Fetching IP address information...")
    ip_info = get_ip_info()

    if ip_info:
        display_ip_info(ip_info)
    else:
        print("Unable to fetch IP information. Please try again later.")
