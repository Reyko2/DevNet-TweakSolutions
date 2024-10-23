from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_ip_info():
    try:
        response = requests.get('https://ipapi.co/json/')
        data = response.json()

        if 'error' in data:
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
        return None

@app.route('/')
def home():
    ip_info = get_ip_info()
    return render_template('index.html', ip_info=ip_info)

if __name__ == '__main__':
    app.run(debug=True)
