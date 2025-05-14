#!/usr/bin/python3
"""
Flask Routing
"""
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0.', port=5000)

    @app.route('/', strict_slashes=False)
    def hello_Abnb():
        """
        Display welcome message
        """
        return 'Hello and Welcome'

    @app.route('/kbnb', strict_slashes=False)
    def kbnb():
        """
        Display welcome test like welcome to Kenya
        """
        return 'Welcome to Africa'
