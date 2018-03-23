from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route('/')
def index():
    env_default_value = 'NO ENV_VARIABLE DECLARATION FOUND'
    get_env_variable = os.getenv('ENV_VARIABLE', env_default_value)
    return render_template('index.html', env_variable=get_env_variable)


if __name__ == '__main__':
    # app.run(debug=True, threaded=True, host='0.0.0.0', port=8080)
    app.run(debug=True, threaded=True, port=8080)

