# python-appium-app-browserstack

This repository demonstrates how to run Appium tests using Python on BrowserStack App Automate.

## Setup

### Requirements

1. Python 3.7+ or Python 2.7+

    - If Python is not installed, follow these instructions:
        - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
        - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

2. Package Manager `pip`

    - If `pip` is not installed, follow these instructions:
        - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following cURL command to download it:

        ```sh
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ```

        - After dowloading, run the file :

        ```sh
        python3(or python) get-pip.py
        ```

        Note : `pip` comes installed with Python 2.7.9+ and python 3.4+

### Install the dependencies

To install the dependencies for Android tests, run :

```sh
pip3(or pip) install -r android/requirements.txt
```

Or,

To install the dependencies for iOS tests, run :

```sh
pip3(or pip) install -r ios/requirements.txt
```

## Getting Started

Getting Started with Appium tests in Python on real BrowserStack devices couldn't be easier!

### **Run first test :**

- Switch to `run-first-test` directory under [Android examples](android/examples/run-first-test) or [iOS examples](ios/examples/run-first-test)

- Follow the steps outlined in the documentation [Getting Started with your first test on App Automate](https://www.browserstack.com/docs/app-automate/appium/getting-started/python)

### **Speed up test execution with parallel testing :**

- Switch to `run-prarallel-tests` directory under [Android examples](android/examples/run-parallel-tests) or [iOS examples](ios/examples/run-parallel-tests)

- Follow the steps outlined in the documentation [Getting Started with Parallel testing on App Automate](https://www.browserstack.com/docs/app-automate/appium/getting-started/python/parallelize-tests)

### **Use Local testing for apps that access resources hosted in development or testing environments :**

- Switch to `run-local-test` directory under [Android examples](android/examples/run-local-test) or [iOS examples](ios/examples/run-local-test)

- Follow the steps outlined in the documentation [Getting Started with Local testing on App Automate](https://www.browserstack.com/docs/app-automate/appium/getting-started/python/local-testing)

**Note**: If you face any issues, refer [Getting Help section](#Getting-Help)

## Integration with other python frameworks

For other Python frameworks samples, refer to following repositories :

- [Behave](https://github.com/browserstack/behave-appium-app-browserstack)
- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer [App-Automate testing frameworks documentation](https://www.browserstack.com/docs?product=app-automate)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).