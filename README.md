# python-appium-app-browserstack

This repository demonstrates how to run Appium Python tests on BrowserStack App Automate.

## Based on

These code samples are currently based on:

- **Appium-Python-Client:** `2.6.1`
- **Protocol:** `W3C`

## Setup

### Requirements

1. Python 3.7+

   > **_NOTE:_** Since v1.0.0, only Python 3.7+ is supported.

   - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer executable
   - For Mac and Linux, run `python --version` to see what python version is pre-installed. If you want a different version download from [here](https://www.python.org/downloads/)

2. Package Manager pip

   Note : `pip` comes installed with python 3.4+

   - If `pip` is not installed, follow these instructions:

     - Securely download get-pip.py by following this link: [get-pip.py](https://bootstrap.pypa.io/get-pip.py) or use following cURL command to download it:

     ```sh
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     ```

     - After dowloading, run the file :

       - For Python 3

         ```sh
         python3 get-pip.py
         ```

### Install the dependencies

To install the dependencies, run the following command in project's base directory:

- For Python 3

  ```sh
  pip3 install -r requirements.txt
  ```

## Getting Started

Getting Started with Appium tests in Python on BrowserStack couldn't be easier!

### **Run your first test :**

Open `Android` or `iOS` folder :

- If you have uploaded your app then add the app id to the `browserstack.yml` config file, or you can directly specify the path to your app in the `browserstack.yml` file.

- Run `browserstack-sdk python browserstack_sample.py`

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

---

### **Use Local testing for apps that access resources hosted in development or testing environments :**

Open `Android` or `iOS` folder :

- Ensure that `browserstackLocal` capability is set to `true` in the `browserstack.yml` file

- If you have uploaded your app then add the app id to the `browserstack.yml` config file, or you can directly specify the path to your app in the `browserstack.yml` file.

- Run `browserstack-sdk python browserstack_sample_local.py`

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

## Integration with other python frameworks

For other Python frameworks samples, refer to following repositories :

- [Behave](https://github.com/browserstack/behave-appium-app-browserstack)
- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer our [Developer documentation](https://www.browserstack.com/docs/)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).
