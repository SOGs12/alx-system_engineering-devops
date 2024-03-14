0x1A. Application server DevOps - SysAdmin

Tasks

Set up development with Python mandatory Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.
Requirements:

Install the net-tools package on your server: sudo apt install -y net-tools Git clone your AirBnB_clone_v2 on your web-01 server. Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000. Your Flask application object must be named app (This will allow us to run and check your code). Example:

Window 1:

Explain ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route

Serving Flask app "0-hello_route" (lazy loading)
Environment: production WARNING: Do not use the development server in a production environment. Use a production WSGI server instead.
Debug mode: off
Running on http://0.0.0.0:5000/ (Press CTRL+C to quit) 35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 - Window 2: ubuntu@229-web-01:/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/ Hello HBNB!ubuntu@229-web-01:/AirBnB_clone_v2$ Repo:
GitHub repository: alx-system_engineering-devops Directory: 0x1A-application_server File: README.md

Set up production with Gunicorn mandatory Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.
Requirements:

Install Gunicorn and any other libraries required by your application. The Flask application object should be called app. (This will allow us to run and check your code) You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point. In order to check your code, the checker will bind a Gunicorn instance to port 6000, so make sure nothing is listening on that port.
#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
