# python-appium-app-browserstack

This repository demonstrates how to run Appium Python mobile app tests on BrowserStack's real device cloud.

## Installation

### Requirements

1. Python 3.7+ or Python 2.7+ (refer [python-2-master branch](https://github.com/browserstack/python-appium-app-browserstack/tree/python-2-master))

    - If Python is not installed, follow these instructions:
        - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer exe
        - For Mac and Linux, run python --version to see what python version is pre-installed. If you want updated version download from [here](https://www.python.org/downloads/)

2. Pip

    - If pip is not installed, follow these instructions:
        - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following curl command:

        ```sh
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ```

        - After dowloading, run the file :

        ```sh
        python get-pip.py
        ```

### Dependencies

- Depending on whether you are running android or iOS tests, run :

```sh
pip install -r android/requirements.txt or pip install -r ios/requirements.txt
```

## Getting Started

Getting Started with Appium tests in Python on real BrowserStack devices couldn't be easier!

### **Run first test :**

- Switch to 'run_first_test' directory under [android examples](android/examples/run_first_test) or [ios examples](ios/examples/run_first_test)

- Follow the steps outlined in the documentation [Getting Started with Appium in Python](https://www.browserstack.com/app-automate/appium-python)

### **Speed up test execution with parallel testing :**

- Switch to 'run_prarallel_tests' directory under [android examples](android/examples/run_parallel_tests) or [ios examples](ios/examples/run_parallel_tests)

- Follow the steps outlined in the documentation [Getting Started with Appium in Python](https://www.browserstack.com/app-automate/appium-python)

### **Run Local tests for apps deployed in your development or testing environment :**

- Switch to 'run_local_test' directory under [android examples](android/examples/run_local_test) or [ios examples](ios/examples/run_local_test)

- Follow the steps outlined in the documentation [Getting Started with Appium in Python](https://www.browserstack.com/app-automate/appium-python)

**Note**: If you face any issues, refer [Getting Help](#Getting-Help)

## Integration with other python frameworks

For other Python frameworks samples, refer to following repositories :

- [Behave](https://github.com/browserstack/behave-appium-app-browserstack)
- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer [App-Automate testing frameworks documentation](https://www.browserstack.com/docs?product=app-automate)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).