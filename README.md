# MQTT to Deep Intelligence connector

Connector to read data from MQTT and dump it into [Deep Intelligence](https://deepint.net/)

## How to install tool

First install prerequisites
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```
Then install tool, for that purpose go to the repository root and run the following command

```bash
sudo python3 -m pip install . --upgrade
```

## Usage

Once installed, the application can be accesed via terminal with the command `mqtt-deepint-connector`. A execution example is attached bellow:
```bash
sudo mqtt-deepint-connector localhost 1883 my_mqtt_user my_mqtt_password my_mqtt_channel1,mymqtt_channel2,my_mqtt_channel2 9CGcK2E3kStQD48eZNC09nkvj571hzVQFz-266zogxEb1kLHMEd1_1fQCRFrrimlRoizinLVv2r5peOWnHw65g 0000014729441860-c02e07b1-9dfcdc46-d0bh1467 0000017b8236f33d-ce2f5dba-bf4x21a4-34eb0562 00000a7c3b912f45-7118g293-aefb1518-71b2g442 example-id 0 FALSE
```

It also attaches a help mode as follows:
```
mqtt-deepint-connector --help
Usage: mqtt-deepint-connector [OPTIONS] [MQTT_BROKER] [MQTT_PORT] [MQTT_USER]
                              [MQTT_PASSWORD] [MQTT_TOPICS]
                              [DEEPINT_AUTH_TOKEN] [DEEPINT_ORGANIZATION_ID]
                              [DEEPINT_WORKSPACE_ID] [DEEPINT_SOURCE_ID]
                              [MQTT_CLIENT_ID] [MQTT_NUM_MESSAGE_LIMIT]
                              [QUIET_MODE_SET]

  While running dumps messages received from MQTT into deepint.

Arguments:
  [MQTT_BROKER]              MQTT's broker IP
  [MQTT_PORT]                MQTT's broker port
  [MQTT_USER]                MQTT's broker user
  [MQTT_PASSWORD]            MQTT's broker password
  [MQTT_TOPICS]              topics from data comes from
  [DEEPINT_AUTH_TOKEN]       Authentication token for Deep Intelligence
  [DEEPINT_ORGANIZATION_ID]  Deep intelligence organization's id, where source
                             is located

  [DEEPINT_WORKSPACE_ID]     Deep intelligence workspace's id, where source is
                             located

  [DEEPINT_SOURCE_ID]        Deep intelligence source's id, where data will be
                             dumped

  [MQTT_CLIENT_ID]           MQTT's client id. If not provided, an UUIDv4 will
                             be generated

  [MQTT_NUM_MESSAGE_LIMIT]   number of messages to store before dumpt to Deep
                             Intelligence. If set to 0 each message is send
                             [default: 10]

  [QUIET_MODE_SET]            if set to true no logging information is
                              provided.  [default: False]


Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.
```

## How to deploy tool

For deploying the application in the `deploy` folder, two deployment medium are attached:
- A Linux Systemd unit
- A PM2 deployment script

### Install Linux Systemd Unit

1. install package as follows in `Usage` function
2. go to deploy folder
3. configure systemd unit replacing the variables between `<` and `>`
4. copy the unit file to folder `/etc/systemd/system` as follows: `cp deploy/mqtt-deepint-connector.service /etc/systemd/system/mqtt-deepint-connector.service`
5. enable unit with `sudo systemctl enable mqtt-deepint-connector.service`
6. start service with `sudo systemctl start mqtt-deepint-connector.service`

```
[Unit] 
Description=MQTT Deep Intelligence connector
After=multiuser.target
StartLimitIntervalSec=0 
 
[Service] 
Type=simple
ExecStart=mqtt-deepint-connector <MQTT_BROKER> <MQTT_PORT> <MQTT_USER> <MQTT_PASSWORD> <MQTT_TOPICS> <DEEPINT_AUTH_TOKEN> <DEEPINT_ORGANIZATION_ID> <DEEPINT_WORKSPACE_ID> <DEEPINT_SOURCE_ID> <MQTT_CLIENT_ID> <MQTT_NUM_MESSAGE_LIMIT> <QUIET_MODE_SET> 
 
[Install] 
WantedBy=multi-user.target
```

#### Install PM2 file

1. install Node.js and npm with `sudo apt install nodejs npm -y`
2. install PM2 with `sudo npm install -g pm2`
3. configure systemd unit replacing the variables between `<` and `>`
4. register the serbvice with `sudo pm2 start mqtt-deepint-connector.pm2.json`
5. enable the service with `sudo pm2 startup`

```
{
  "apps" : [
    {
      "name": "mqtt-deepint-connector",
      "interpreter": "/bin/bash",
      "script": "mqtt-deepint-connector",
      "args": "<MQTT_BROKER> <MQTT_PORT> <MQTT_USER> <MQTT_PASSWORD> <MQTT_TOPICS> <DEEPINT_AUTH_TOKEN> <DEEPINT_ORGANIZATION_ID> <DEEPINT_WORKSPACE_ID> <DEEPINT_SOURCE_ID> <MQTT_CLIENT_ID> <MQTT_NUM_MESSAGE_LIMIT> <QUIET_MODE_SET>",
      "out_file": "/var/log/mqtt-deepint-connector.log",
      "error_file": "/var/log/mqtt-deepint-connector.log"
    }
  ]
}
```
