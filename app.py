#from twilio.rest import Client
from flask import Flask, redirect, url_for,render_template
app= Flask(__name__)
import os
import cloudinary.uploader
cloudinary.config( 
    cloud_name = "dqe3ctrik", 
    api_key = "676391596632685", 
    api_secret = "lzdXvAQ1HZ4QmHwVDXIY2JGPOPQ" 
)
@app.route("/")
def home():
    cloudinary.uploader.upload("https://mausam.imd.gov.in/Radar/ppz_goa.gif", 
    public_id = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"))
   
    return render_template('index.html')

    

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure




if __name__=="__main__":
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
