# works with both python 2 and 3
from __future__ import print_function

import africastalking

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

if __name__ == '__main__':
    VOICE().call()