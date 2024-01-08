import requests
import configparser

# Load configuration file
config = configparser.ConfigParser()
config.read('config.conf')

GMAIL_ADDRESS = config['BREVO']['GMAIL_ADDRESS']
GMAIL_NAME = config['BREVO']['GMAIL_Name']
BREVO_API = config['BREVO']['API']

def sendOTP(address,otp):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API,
        "content-type": "application/json"
    }
    payload = {
        "sender": {
            "name": GMAIL_NAME,
            "email": GMAIL_ADDRESS
        },
        "to": [
            {
                "email": address,
            }
        ],
        "subject": "OTP Verification",
        "htmlContent": f'''<!DOCTYPE html>
                            <html>
                            <head>
                                <title>OTP Verification</title>
                            </head>
                            <body>
                                <h3>OTP Verification</h3>
                                <p>Hello USER,</p>
                                <p>Your One-Time Password (OTP) for verification is: <strong>{otp}</strong></p>
                                <p>Please use this OTP to complete your verification process. This OTP will expire in 30 minutes.</p>
                                <p>If you did not request this OTP, please ignore this email.</p>
                                <p>Thank you for using our service!</p>
                                <p>Best regards,<br>MST Automations</p>
                            </body>
                            </html>
                        ''' 
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)

    if response.status_code in range (200,299):
        return True
    else:
        #print("Email sending failed")
        return False

def sendMail(address,name,token):
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "accept": "application/json",
        "api-key": BREVO_API,
        "content-type": "application/json"
    }
    payload = {
        "sender": {
            "name": GMAIL_NAME,
            "email": GMAIL_ADDRESS
        },
        "to": [
            {
                "email": address,
            }
        ],
        "subject": "Your Tokens are Ready",
        "htmlContent": f'''<!DOCTYPE html>
                            <html>
                            <head>
                                <title>OTP Verification</title>
                            </head>
                            <body>
                                <h3>Welcome</h3>
                                <p>Hello {name},</p>
                                <p>Your Tokens has been created. Please keep them safe</p>  
                                <p><stron>{token}</stron></p>
                                <p>Thank you for using our service!</p>
                                <p>Best regards,<br>MST Automations</p>
                            </body>
                            </html>
                        ''' 
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)

    if response.status_code in range (200,299):
        return True
    else:
        #print("Email sending failed")
        return False    
