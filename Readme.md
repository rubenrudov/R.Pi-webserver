# Web server - Sasha .Ltd wheelchair network setting

This README would document the necessary steps for set up and run the webserver for letting the 
user use his/her network credentials for begin using Sasha's wheelchair.

## What is the purpose of this repository ?

* Version control of the development process
* Instructs and system summarize for future technicians.
* Collaboration platform for team members.

## Background:

* After provisioning the sdcard and the R.Pi and powering it on
  the web credentials in /etc/network/interface will be the credentials
  of the factory wifi, we have to change it to the customer's network credentials (LED blinks for alerting this).
* For that reason, we'll turn on the A.P mode of the R.Pi using the reset button (A long press).
* This action will activate the A.P mode and a webserver that runs on the static ip we created during the provision.
* The webserver hosts a webapp in which the user will write the net credentials.
* After the user submits the form, the chair will wait for reset,
after reset (triple-press on the reset button) the R.Pi will use the new web credentials, and the AP mode will be forced stop using another playbook. 

## Contribution guidelines for team members:
* Download the repo
* Create new project on your IDE and drag the files there.
* Configure your project venv.  
* Run: ```pip install -r requirements.txt``` in your terminal.
* Configure globals.yaml with factory network creds, then you'll be ready to go.
* Use ```python main.py``` for running the server.
* ###### The server runs on the configed host & port, make sure you change the port from time to time. If you start getting "Internal server error" you should try to fix it using that method, that could be a reason for the error because port might be overloaded...


## Who do I talk to:
* [Ruby Rudov](https://github.com/rubenrudov)
* [Vitaly Grinberg](https://github.com/vitus133)
