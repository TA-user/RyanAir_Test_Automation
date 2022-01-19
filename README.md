# RyanAirTestAutomation
**PythonTestAutomationFramework**

**Description**

Test Automation Framework for web automation of  "https://www.ryanair.com".

Main technologies are used in project:

- Python == 3.10
- pytest == 6.2.5
- Selenium == 3.141.0

* Framework is based on Page Object Model. 
* Reporting implemented by using Allure report.
* Logging to external files implemented using Loguru

The project is being developed during the iTechArt internship.

# How to install it

Make sure you have python3.10 installed on your machine by typing in cmd 

    ``$ python3 --version`` 

if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1)  Clone repository: 

    ``$ clone https://github.com/TA-user/RyanAir_Test_Automation.git``

2)  You have to install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

3)  Make sure you have pipenv by typing in cmd 
  
    ``$ pipenv --version`` 
  
If not - you have to install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/

    ``$ pip install --user pipenv``

4) Install dependencies:

    ``$ pipenv install``

5) Add your own credentials (**USERNAME** and **PASSWORD**) for logging to 'https://www.ryanair.com' 

There are 2 way of credentials entry:

a) You can type your credentials in file ``config.py``:

**class DefaultCreds**
* USERNAME = ``'type here'``
* PASSWORD = ``'type here'``

b) OR you can enter them directly in command using options 'username' and 'password' (see example below).

# How to run it

1) If you decided not to type credentials to ``config.py`` for logging to 'https://www.ryanair.com', 
you should define them directly in command. Use options 'username' and 'password':

Example:

    ``$ python -m pytest -v --username=your_username --password=your_password --alluredir=allure_reports/``

2) Any test could be run in following browsers:

    - Chrome
    - Firefox
    - Edge
   
Use option --browser_name to define browser, you want to execute test in:

     ``$ python -m pytest -v --browser_name=chrome --alluredir=allure_reports/``
     ``$ python -m pytest -v --browser_name=firefox --alluredir=allure_reports/``
     ``$ python -m pytest -v --browser_name=edge --alluredir=allure_reports/``

By default, tests are executed in Chrome

3) Smoke tests have been implementing to test basic functionality. 

To execute them use commands below:

* Test to verify guest can Log in:

    ``$ python -m pytest -v -m "authorization and smoke"  --alluredir=allure_reports/``

* Test to verify user can order a flight:  

    ``$ python -m pytest -v -m "flights_order and smoke" --alluredir=allure_reports/``

* Test to verify user can hire a car:

    ``$ python -m pytest -v -m "car_hire and smoke" --alluredir=allure_reports/``

* Test to verify user can book a hotel:

    ``$``

* All smoke tests:

    ``$ python -m pytest -v -m smoke --alluredir=allure_reports/``

* To open allure reports use: 

    ``$ allure serve allure_reports/``

The logs are stored at ``logs.debug.log`` and ``logs.errors.log`` files. 
File will be overwritten after starting the next test.
