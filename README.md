# HRTI

HRTI is a simple UI automation framework for Android devices using python. 

## Installation

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pipenv.

```bash
pip install pipenv
```
2. In project root directory */hrti run the following command:
```bash
pipenv install
```
This will install all required dependencies required to run the project (Including appium v2.X)
if it fails to install it. Install it manually via this site: [appium](https://appium.io/docs/en/2.1/)

## Usage
--> apk is already in the folder. If not, download it from google play & extract it to your laptop as apk file

```python
1. # in .env file change your credentials to login to app. 

2. # in /utils/driver_manager.py change your desired caps for your android device & AutomationName

3. # in /utils/driver_manager.py change default IP & PORT for appium server (localhost:4723) to your desired

4. lift appium server manually: (it will run on localhost:4723) 
# run this command  in your root project folder to run all of your tests in ./tests folder
python3 -m pipenv run pytest

5. # if you tag your tests with annotations run your tests with this command:
python3 -m pipenv run pytest tagged_test.py
```