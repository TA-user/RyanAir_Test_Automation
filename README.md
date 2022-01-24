# RyanAirTestAutomation
**PythonTestAutomationFramework**

**Description**

Test Automation Framework for web automation of  "https://www.ryanair.com".

Main technologies are used in project:


- Python == 3.10
- pytest == 6.2.5
- Selenium == 3.141.0
- Docker == 20.10.12
- Selenoid == 1.10.7
- allure-pytest == 2.9.45
- Loguru == 0.5.3

* Framework is based on Page Object Model.
* Tests could be executed within Docker container by using Selenoid.
* Reporting implemented by using Allure report.
* Logging to external files implemented using Loguru

The project is being developed during the ITechArt internship.

# 1) How to install it

1.1)Make sure you have python3.10 installed on your machine by typing in cmd 

    ``$ python3 --version`` 

if not - go to https://realpython.com/installing-python/#step-1-download-the-python-3-installer.

1.2) Clone repository: 

    ``$ clone https://github.com/TA-user/RyanAir_Test_Automation.git``

1.3) You have to install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

1.4) Make sure you have pipenv by typing in cmd 
  
    ``$ pipenv --version`` 
  
If not - you have to install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/

    ``$ pip install --user pipenv``

1.5) Install dependencies:

    ``$ pipenv install``

1.6) Add your own credentials (**USERNAME** and **PASSWORD**) for logging to 'https://www.ryanair.com' 

There are 2 way of credentials entry:

a) You can type your credentials in file ``config.py``:

**class DefaultCreds**
* USERNAME = ``'type here'``
* PASSWORD = ``'type here'``

b) OR you can enter them directly in command using options '--username' and '--password' (see example below).

1.7) For executing tests with Selenoid you need to perform the following actions:

    - Make sure you have recent Docker (https://www.docker.com/) version installed.
    - Download Configuration Manager (Selenoid quick installation binary - https://aerokube.com/cm/latest/)  
      for your platform from releases page (https://github.com/aerokube/cm/releases/tag/1.8.1)
    - On Linux or Mac give execution permissions to binary:
        $ chmod +x cm
    - $ ./cm selenoid start --vnc
    - $ ./cm selenoid-ui start
    
# 2) How to run it

2.1) If you decide not to type credentials to ``config.py`` for logging to 'https://www.ryanair.com', 
you should define them directly in command. Use options 'username' and 'password':

Example:

    ``$ python -m pytest -v --username=your_username --password=your_password --alluredir=allure_reports/``

2.2) Any test could be run in following browsers:

    - Chrome
    - Firefox
    - Opera
   
Use option --browser_name to define browser, you want to execute test in:

     ``$ python -m pytest -v --browser_name=chrome --alluredir=allure_reports/``
     ``$ python -m pytest -v --browser_name=firefox --alluredir=allure_reports/``
     ``$ python -m pytest -v --browser_name=opera --alluredir=allure_reports/``

By default, tests are executed in Chrome

2.3) Smoke tests have been implementing to test basic functionality. 

To execute them use commands below:

* Test to verify guest can Log in:

    ``$ python -m pytest -v -m "authorization and smoke"  --alluredir=allure_reports/ --launch_mode=local --browser_name="browser you want to execute tests in"``

* Test to verify user can order a flight:  

    ``$ python -m pytest -v -m "flights_order and smoke" --alluredir=allure_reports/ --launch_mode=local --browser_name="browser you want to execute tests in"`` 

* Test to verify user can hire a car:

    ``$ python -m pytest -v -m "car_hire and smoke" --alluredir=allure_reports/ --launch_mode=local --browser_name="browser you want to execute tests in"``

* Test to verify user can book a hotel:

    ``$ python -m pytest -v -m "hotel_booking and smoke" --alluredir=allure_reports/ --launch_mode=local --browser_name="browser you want to execute tests in"``

* All smoke tests:

    ``$ python -m pytest -v -m smoke --alluredir=allure_reports/ --launch_mode=local --browser_name="browser you want to execute tests in"``

2.4) If you want to execute tests using Selenoid, use commands below:

* Test to verify guest can Log in:

    ``$ python -m pytest -v -m "authorization and smoke"  --alluredir=allure_reports/ --browser_name="browser you want to execute tests in"``

* Test to verify user can order a flight:  

    ``$ python -m pytest -v -m "flights_order and smoke" --alluredir=allure_reports/ --browser_name="browser you want to execute tests in"`` 

* Test to verify user can hire a car:

    ``$ python -m pytest -v -m "car_hire and smoke" --alluredir=allure_reports/ --browser_name="browser you want to execute tests in"``

* Test to verify user can book a hotel:

    ``$ python -m pytest -v -m "hotel_booking and smoke" --alluredir=allure_reports/ --browser_name="browser you want to execute tests in"``

* All smoke tests:

    ``$ python -m pytest -v -m smoke --alluredir=allure_reports/ --browser_name="browser you want to execute tests in"``

If you use Selenoid, your tests could be executed with following browsers: Chrome 97.0, Firefox 96.0 or Opera 82.0.

# 3) How to see the report

To open allure reports use: 

    ``$ allure serve allure_reports/``

The logs are stored at ``logs.debug.log`` and ``logs.errors.log`` files. 
File will be overwritten after starting the next test.
