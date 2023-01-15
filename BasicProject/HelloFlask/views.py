"""
This script contains the definition of routes and views for the application.
"""
from flask import Flask
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    """Renders a sample page."""
    return "Hello Flask!"

