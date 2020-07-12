# python-appium-app-browserstack

This repository provides sample code to run tests using Appium with Python on BrowserStack’s real device cloud. It includes code required to integrate with BrowserStack cloud and tests written for BrowserStack’s sample Android and iOS apps.

## Documentation

Refer  [Getting Started using Appium with Python](https://www.browserstack.com/app-automate/appium-python)

## Installation

### Requirements

1. Python 3.5+ or Python 2.7+ (refer [python-2-master branch](https://github.com/browserstack/python-appium-app-browserstack/tree/python-2-master))

    - If Python is not installed, follow these instructions:
        - For Windows, download latest python version from [here](https://www.python.org/downloads/windows/) and run the installer exe
        - For Mac and Linux, run python --version to see what python version is pre-installed. If you want updated version download from [here](https://www.python.org/downloads/)

2. pip

    - If pip is not installed, follow these instructions:
        - Securely download get-pip.py by following this link: get-pip.py or use following curl command:

        ```sh
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        ```

        ```sh
        python get-pip.py
        ```

### Dependencies

- Depending on your use case, switch to android/ or ios/ folder and run -

```sh
pip install -r requirements.txt
```

## Getting Started

Getting Started with Python Appium tests on real BrowserStack devices couldn't be easier!

### **Run first test in 3 simple steps :**

1. #### Upload App

    - Upload your android app apk or iOS app ipa file, or Upload one of the Browserstack’s sample app [WikipediaSampleAndroidApp](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) | [BStackSampleiOSApp](https://www.browserstack.com/app-automate/sample-apps/ios/BStackSampleApp.ipa)

        Note: Update username and accesskey with BrowserStack credentials (Find your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    ``` sh
    curl -u "username:accesskey" -X POST "https://api.browserstack.com/app-automate/upload" -F "file=@/path/to/app/file/Application-debug.apk"
    ```

    - Copy the 'app_url' (bs://\<hashed-app-id>) returned in the response and save it

2. #### Configure and run tests

    - Open file android/BrowserStackAndroid.py to run android tests or ios/BrowserStackIOS.py to run iOS tests

    - Update BrowserStack credentials - userName & accessKey (Find  your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    - Update the desired_caps "app" capability with app_url (bs://\<hashed-app-id>) received in upload app API response

    - If you have uploaded your app instead of BrowserStack sample app, update the tests accordingly

    - Run tests with following command

    ```sh
    python android/BrowserStackAndroid.py or python ios/BrowserStackIOS.py
    ```

3. #### Thats it! view your tests results on [BrowserStack App Automate dashboard](https://app-automate.browserstack.com/)

### **If your app is deployed on development or testing environment, try BrowserStack Local Testing**

1. #### Upload app

    - Upload your android app apk or iOS app ipa file, or Upload one of the Browserstack’s sample app [LocalAndroidSample.apk](https://www.browserstack.com/app-automate/sample-apps/android/LocalSample.apk) | [LocaliOSSample.ipa](https://www.browserstack.com/app-automate/sample-apps/ios/LocalSample.ipa)

        Note: Update your BrowserStack credentials - username and accesskey (Find your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    ``` sh
    curl -u "username:accesskey" -X POST "https://api.browserstack.com/app-automate/upload" -F "file=@/path/to/app/file/Application-debug.apk"
    ```

    - Copy the 'app_url'(bs://\<hashed-app-id>) returned in the response and save it

2. #### Configure and run local tests

    - Open file android/LocalSampleAndroid.py for android tests or ios/LocalSampleIOS.py for iOS tests

    - Update BrowserStack credentials - userName & accessKey (Find  your BrowserStack credentials [here](https://www.browserstack.com/accounts/settings))

    - Update the desired_caps "app" capability with app_url (bs://\<hashed-app-id>) received in upload app API response

    - If you have uploaded your app instead of sample app, update the tests accordingly

    - Run tests with following command

    ```sh
    python android/LocalSampleAndroid.py or python ios/LocalSampleIOS.py
    ```

3. #### Thats it! View your tests results on [BrowserStack App Automate dashboard](https://app-automate.browserstack.com/)

## Integration with other python frameworks

For other Python frameworks samples, refer to following reposoritories :

- [Behave](https://github.com/browserstack/behave-appium-app-browserstack)
- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)

Note: For other test frameworks supported by App-Automate refer [App-Automate testing frameworks documentation](https://www.browserstack.com/docs?product=app-automate)

## Getting Help

If you are running into any issues or have any queries, please check [Browserstack Support page](https://www.browserstack.com/support/app-automate) or [get in touch with us](https://www.browserstack.com/contact?ref=help).