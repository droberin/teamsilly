from setuptools import setup

setup(
    name='teamsilly',
    version='0.1.0',
    packages=['teamsnotifier'],
    url='https://github.com/droberin/teamsilly',
    license='MIT',
    author='Roberto Salgado',
    author_email='drober@gmail.com',
    description='Teams Messaging through Inbound Webhook',
    installs_requires=['requests>=2.0']
)
