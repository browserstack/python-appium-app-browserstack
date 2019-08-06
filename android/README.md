## Dependencies

For installing the required packages, use the following command

```
$ pip3 install -r requirements.txt
```

## Running your tests

- Do remember to switch the BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY with your own browserstack credentials.
- Upload your Native App (.apk file) to BrowserStack servers using upload API and update the app capability:

  ```
  curl -u "username:accesskey" -X POST "https://api.browserstack.com/app-automate/upload" -F "file=@/path/to/app/file/Application-debug.apk"
  ```

- If you do not have an .apk file and looking to simply try App Automate, you can download our [sample app](https://www.browserstack.com/app-automate/sample-apps/android/WikipediaSample.apk) and upload to the BrowserStack servers using the above API.
- Run ```python3 BrowserStackAndroid.py```
- For LocalSample tests, you can use our [local sample app](https://www.browserstack.com/app-automate/sample-apps/android/LocalSample.apk).
- Run ```python3 LocalSampleAndroid.py```
- Update the desired capability "app" with the App URL returned from the above API call

## Notes
* You can view your test results on the [BrowserStack App Automate dashboard](https://www.browserstack.com/app-automate)
* Refer [Get Started](https://www.browserstack.com/app-automate/appium-python) document to configure the capabilities

For frameworks integration with BrowserStack, refer to their individual repositories -

- [Lettuce](https://github.com/browserstack/lettuce-appium-app-browserstack)
- [Behave](https://github.com/browserstack/behave-appium-app-browserstack)

For python 2 support refer the branch
- [python-2-master](https://github.com/browserstack/python-appium-app-browserstack/tree/python-2-master)
