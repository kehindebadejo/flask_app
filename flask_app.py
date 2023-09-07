from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.now(pytz.utc).strftime('%A')

    # Get the current UTC time
    current_time = datetime.now(pytz.utc).strftime('%Y-%m-%d %H:%M:%S')

    # Construct Github URLs
    github_file_url = 'https://github.com/your_username/your_repo/blob/main/your_file.py'
    github_repo_url = 'https://github.com/kehindebadejo/flask_app'

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_utl': github_repo_url,
        'status_code': 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)


