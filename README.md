# Blog example with pyramid
In this repo, I want create a simple blog with pyramid following the example
that is located in the website.

The main reason for create this blog is learn about this framework and
its possibilities.

## Install the dependencies
* Clone the repository
* Initialize virtualenv
* Activate the virtualenv: source /bin/activate (unix)
* Install the project dependencies: pip install -r requirements.txt


## Run the application

- To setup the application:
* /bin/python setup.py develop

- To initialize the db:
* /bin/initialize_pyramid_blogr_db development.ini

- To run application:
* /bin/pserve development.ini
