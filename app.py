from flask import Flask, request, render_template, url_for
from mbta_helper import find_stop_near
from random_joke import get_joke

app = Flask(__name__)


@app.get('/')
def home():
    return render_template('index.html')



@app.post('/nearest_mbta')
def nearest_station():
    try:
        address = request.form.get('address')
        mbta_info = find_stop_near(address)
        joke = get_joke()
        # print(mbta_info)
        return render_template('mbta_station.html', mbta_info = mbta_info, joke = joke)
    except: 
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

    
