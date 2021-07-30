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


## Website routes ##

```html
<h2>Example of code</h2>

<!DOCTYPE html>
<html lang="en">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <meta charset="UTF-8">
        <title>Sasha .Ltd set-up</title>

         <style>

            .bg-light {
                background: #FFF !important;
                align-items: center !important;
            }

            .nav-link {
                font-size: medium !important;
                padding-top: 20px !important;
                margin-top: 7px;
                margin-bottom: 7px;
            }

            .nav-link:hover {
               color: rgb(33, 162, 136) !important;
               transition: 0.2s !important;
            }

            .active {
                border-bottom: 1px solid black !important;
            }

            .active:hover {
               border-bottom: 1px solid rgb(33, 162, 136) !important;
               transition: 0.2s !important;
            }

            .btn-success {
                background: rgb(33, 162, 136) !important;
                border-radius: none !important;
            }

            .btn-success:hover {
                background: rgb(41,191,161) !important;
                transition: .0s ease;
            }

            .btn-lg {
                border-radius: 0px;
            }

            .form-control {
                border-color: rgb(41,191,161) !important;
            }
        </style>
    </head>
    <body class="cover text-center">
        <nav class="navbar navbar-expand navbar-light bg-light" aria-label="Fourth navbar example">
            <div class="container-fluid">
              <a class="navbar-brand" href="https://sashaintuitive.com/">
                  <img src="https://img1.wsimg.com/isteam/ip/95002212-4611-42c4-92bf-b72332290bb0/sasha%20logo.png/:/rs=h:75,cg:true,m/qt=q:100/ll">
              </a>

              <div class="collapse navbar-collapse" id="navbarsExample04">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Set-up</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="/instructs">Instructions</a>
                  </li>
                </ul>
              </div>
            </div>
        </nav>

        <main class="form-signin">
          <form method="post" style="margin-left: 25%; margin-right: 25%; margin-top: 5%;">
            <h1 class="h3 mb-3 fw-normal">Please type your network credentials here</h1>
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingInput" placeholder="NETWORK">
              <label for="floatingInput">Network name</label>
            </div>
            <br/>
            <div class="form-floating">
              <input type="password" class="form-control" id="floatingPassword" placeholder="PASSWORD">
              <label for="floatingPassword">Network password</label>
            </div>
            <br/>
            <div class="form-floating">
              <input type="text" class="form-control" id="floatingSshKey" placeholder="SSH-KEY">
              <label for="floatingPassword">Public SSH key</label>
            </div>
            <br/>
            <button class="w-100 btn btn-lg btn-success" type="submit">Submit</button>
          </form>
        </main>
        <div class="text-center mt-auto text-white-50" style="bottom: 0; position: absolute; width: 100%; text-align: center;">
            <p class="mt-5 mb-3 text-muted float-bottom">Copyright © 2017 SASHA Intuitive Ltd - All Rights Reserved.</p>
        </div>
    </body>
</html>
```

## Who do I talk to:
* [Ruby Rudov](https://github.com/rubenrudov)
* [Vitaly Grinberg](https://github.com/vitus133)
