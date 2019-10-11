# Secret Santa

Small script that generates Secret Santa for a given list (__data.txt__). Once the matching done, it send an email telling the result.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have python installed on your machine. If you don't, you can install it like that:
```
# For MacOS
brew install python

# For linux
sudo apt-get install python
```

### Installing

A step by step series of examples that tell you how to get a development env running

First, clone the repo
````
git clone https://github.com/manneGd/SecretSantaPython.git
````

Then, open the file list.json and modify the value with your own. When it's done create a file __config.py__. Copy paste these information:
```
email_user = 'YOUR_EMAIL_ADDRESS'
email_password = 'YOUR_PASSWORD'
smtp = 'SMTP_SERVER'
port_smtp = SSL_SMTP_PORT
```

Finally, you can just execute the script:

```
python main.py
```

Done! All the people in your list.json file received an email.

## Versioning

Version 1.1

## Authors

* **Marie-Anne Grand** - *Initial work* - [manneGd](https://github.com/manneGD)

