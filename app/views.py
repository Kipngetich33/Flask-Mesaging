# views.py

from flask import render_template

from app import app

import africastalking

# Initialize SDK
username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "d9135795e446b9b25430f33da3be70c79d868428898fdb7b356f9eb0cb06bcf4" # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)
# Initialize a service e.g. SMS
sms = africastalking.SMS

@app.route('/')
def index():
    print("*"*80)
    print(sms)
    # Use the service synchronously
    response = sms.send("Hello Kipngetich!", ["+254712567583",""])
    print(response)
    return render_template("index.html")

@app.route('/about')
def about():
    class VOICE:
        def __init__(self):
            # Set your app credentials
            self.username = "sandbox"
            self.api_key = "d9135795e446b9b25430f33da3be70c79d868428898fdb7b356f9eb0cb06bcf4"
            # Initialize the SDK
            africastalking.initialize(self.username, self.api_key)
            # Get the voice service
            self.voice = africastalking.Voice

        def call(self):
            # Set your Africa's Talking phone number in international format
            callFrom = "+254712567583"
            # Set the numbers you want to call to in a comma-separated list
            callTo   = ["+254706852152"]
            try:
                # Make the call
                result = self.voice.call(callFrom, callTo)
                print (result)
            except Exception as e:
                print ("Encountered an error while making the call:%s" %str(e))

    # create an instance
    call_instance = VOICE()
    call_instance.call()
    return render_template("about.html")