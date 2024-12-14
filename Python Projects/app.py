# Import necessary modules
from flask import Flask, render_template  # Flask to serve web pages and render templates
import requests  # Requests to fetch data from APIs

app = Flask(__name__)

# Function to fetch IP information using the ipapi.co API
def get_ip_info():
    try:
        # Make a GET request to the ipapi API 
        response = requests.get('https://ipapi.co/json/')
        data = response.json()  

        if 'error' in data:
            return None  

        # Return a list of dictionary containing the IP and other relevant datas
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

# Define the home route 
@app.route('/')
def home():
    ip_info = get_ip_info()  
    return render_template('index.html', ip_info=ip_info)  # Render the HTML template and pass the IP info

#debug start
if __name__ == '__main__':
    app.run(debug=True)
