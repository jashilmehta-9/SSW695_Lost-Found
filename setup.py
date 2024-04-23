from setuptools import setup, find_packages

setup(
    name='SSW695_Lost-Found',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=3.2',  # Make sure to match your Django version requirement
        'gunicorn',     # Commonly used WSGI for running Django on Heroku
        # Add other dependencies necessary for your project
    ],
)
