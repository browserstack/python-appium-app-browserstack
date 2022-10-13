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

### Run your first test :

**1. Upload your Android or iOS App**

Upload your Android app (.apk or .aab file) or iOS app (.ipa file) to BrowserStack servers using our REST API. Here is an example cURL request :

```
curl -u "YOUR_USERNAME:YOUR_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@/path/to/apk/file"
```

Ensure that @ symbol is prepended to the file path in the above request. Please note the `app_url` value returned in the API response. We will use this to set the application under test while configuring the test later on.

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) or [sample iOS app](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa).

**2. Configure and run your first test**

Open `browserstack_sample.py` file in `Android` or `iOS` folder :

- Replace `YOUR_USERNAME` & `YOUR_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` wkth the URL obtained from app upload step

- Set the device and OS version

- If you have uploaded your own app update the test case

- Run `python browserstack_sample.py`

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

---

### **Use Local testing for apps that access resources hosted in development or testing environments :**

**1. Upload your Android or iOS App**

Upload your Android app (.apk or .aab file) or iOS app (.ipa file) that access resources hosted on your internal or test environments to BrowserStack servers using our REST API. Here is an example cURL request :

```
curl -u "YOUR_USERNAME:YOUR_ACCESS_KEY" \
-X POST "https://api-cloud.browserstack.com/app-automate/upload" \
-F "file=@/path/to/apk/file"
```

Ensure that @ symbol is prepended to the file path in the above request. Please note the `app_url` value returned in the API response. We will use this to set the application under test while configuring the test later on.

**Note**: If you do not have an .apk or .ipa file and are looking to simply try App Automate, you can download and test using our [sample Android Local app](https://www.browserstack.com/app-automate/sample-apps/android/LocalSample.apk) or [sample iOS Local app](https://www.browserstack.com/app-automate/sample-apps/ios/LocalSample.ipa).

**2. Configure and run your local test**

Open `browserstack_sample_local` file in `Android` or `iOS` folder :

- Replace `YOUR_USERNAME` & `YOUR_ACCESS_KEY` with your BrowserStack access credentials. Get your BrowserStack access credentials from [here](https://www.browserstack.com/accounts/settings)

- Replace `bs://<app-id>` wkth the URL obtained from app upload step

- Set the device and OS version

- Ensure that `local` capability is set to `true`. Within the test script, there is code snippet that automatically establishes Local Testing connection to BrowserStack servers using Python binding for BrowserStack Local.

- If you have uploaded your own app update the test case

- Run `python browserstack_sample_local.py`

- You can access the test execution results, and debugging information such as video recording, network logs on [App Automate dashboard](https://app-automate.browserstack.com/dashboard)

## Integration with other python frameworks

For other Python frameworks samples, refer to following repositories :

- [Behave](https://github.com/browserstack/behave-appium-app-browserstack)
- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer our [Developer documentation](https://www.browserstack.com/docs/)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).
