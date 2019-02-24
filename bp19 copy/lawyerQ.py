from flask import Flask
import numpy as np
from flask import render_template
from flask import request



app = Flask(__name__)

@app.route('/')
def PageReturn():
    return render_template('user.html')
@app.route("/help", methods = ["POST"])
def Help():
    x = int(request.form.get("uzbekistan"))
    y = int(request.form.get("kyrgistan"))
    g = str(request.form.get("test"))
    reqs = []
    reqs.append((g,(x,y)))
    print(f"string is {str(reqs)}")
    import smtplib
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.login("y444444y@hotmail.com", "")
    subject = ""
    text = f"User at {str(reqs[0][1])} says {str(reqs[0][0])}"
    msg = "Subject: {}\n\n{}".format(subject, text)
    print(msg)
    server.sendmail("y444444y@hotmail.com", "8608782363@vtext.com", msg)
    server.close()
    return(f"Your message '{str(reqs[0][0])}' is successfully delivered!")
    
app.run(debug=True)

