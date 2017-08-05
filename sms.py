from flask import Flask
from africastalking.AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException 

app = Flask(__name__)

@app.route("/sms")
def sms():
        # Specify your login credentials
    username = "jkuat"
    apikey   = "30e34507d42910e827b2ed32c6ffe53019f42feacf1a7e905c753196dd4454bd"

    to      = "+254704085038"
    message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"
    gateway = AfricasTalkingGateway(username, apikey)
    try:
    
        results = gateway.sendMessage(to, message)
        
        for recipient in results:
            # status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)

    return "hello world"


if __name__ == '__main__':
app.run(debug=True,host='0.0.0.0')
