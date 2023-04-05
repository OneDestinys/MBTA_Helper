from flask import Flask, request, render_template, url_for
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.post('/nearest_mbta', methods = ['POST'])
def nearest_mbta():
    # address = request.form.get('address')
    # mbta_info = find_stop_near(address)
    return render_template('mbta_station.html')




    
