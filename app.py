from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html', api_key=os.getenv('GOOGLE_MAPS_API_KEY'))

if __name__ == '__main__':
    app.run(debug=True)
