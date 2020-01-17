from twilio.rest import Client


class Sending:
    ''' this model is for sending sms with twilio'''
    from_='+15627312373'
    to= '+254798863355'
    
    account_sid = 'AC2337805f2c4adaf746eb84920714cd43'
    auth_token = '40cb89c7316248f5c550a594b54ba072'
      
    def __init__(self,body):
            self.body=body
            

    '''verification function. it verifies twilio credentials'''
    def verify(self):
        pass

    def send_sms(self):
        
        client=Client(self.account_sid,self.auth_token)
        print('auths recieved')
        message= client.messages.create(to=self.to ,from_=self.from_, body=self.body)
        print('message sent')
