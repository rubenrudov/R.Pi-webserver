from flask import Flask, render_template, request, redirect, url_for
import os
import yaml

app = Flask(__name__)


def get_factory_creds():
    try:
        with open("globals.yml", "r") as file:
            return yaml.safe_load(file)["all"]["factory"]

    except Exception as e:
        print(e)

    return None


def exe_playbook(command: str):
    """
    :param command: A command that runs the necessary ansible playbook
    :return: The result -> If the factory network creds were changed 0, else -1
    """
    # Remove comment on line 25 before executing in production mode.
    # os.system(command)

    with open("/etc/network/interfaces", 'r') as file:
        content = file.read()

        for word in get_factory_creds():
            if word in content:
                return -1

        return 0


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('/credential_set.html')

    else:
        print("Submitted credentials")

        # result = exe_playbook("ansible-playbook -i change_creds.yaml")  # TODO: Create and develop this playbook
        result = 0  # Hardcoded result until the playbook will be ready to use.

        # The task function should return value if the task went successfully, if does, green screen, else red screen.
        if result == 0:
            return redirect('/successful_change')

        return redirect('/unsuccessful_change')

        # TODO: Linux commands/ansible lineinfile module change web credentials from factory to home.
        #  ansible lineinfile functionality will change the web creds in /etc/network/interfaces wlan0 interface
        #  to the new creds.


@app.route("/instructs", methods=['GET'])
def instructs():
    return render_template('/instructs.html')


@app.route("/successful_change", methods=['GET', 'POST'])
def successful_setup():
    return render_template('/successful_change.html')


@app.route("/unsuccessful_change", methods=['GET'])
def unsuccessful_setup():
    return render_template('/unsuccessful_change.html')


@app.route("/reset_if_success", methods=['GET'])
def reset_if_success():
    print("RESET REMOTELY")

    # TODO: exe_playbook(restart and play the exit access point mode playbook)
    return render_template('/reset_loading.html')


@app.route("/reset_if_unsuccessful", methods=['GET'])
def reset_if_unsuccessful():
    print("RESET REMOTELY")

    # TODO: exe_playbook(just restart as access point)
    return render_template('/reset_loading.html')


if __name__ == '__main__':
    # In production, we change it to the static IP that we saved in hosts.yaml
    # Here we use 127.0.0.1 instead but before production we should change it to our static IP address.
    # IMPORTANT NOTE !!!: Make sure you refresh the port from time to time...
    app.run(host="192.168.1.233", port=5002)
