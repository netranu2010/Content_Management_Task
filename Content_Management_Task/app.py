"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
from content import content
from content import get_services
from content import save_services
a=get_services(1)
b=save_services()
app = Flask(__name__)


# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def index():
    """Renders a sample page."""
    return render_template('index.html', title=content.contentid)
    
@app.route('/service')
def service():
    return render_template('service.html', title=content.contentid, a=a, b=b)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
