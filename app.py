from flask import Flask, app, redirect, url_for, render_template, request
import smtplib
# import os
from email.message import EmailMessage

app = Flask(__name__)
msg = EmailMessage()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/success", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        # Getting client's info from the form
        cl_name = request.form["name"]
        cl_phone = request.form["phone"]
        cl_email = request.form["email"]
        cl_desc = request.form["desc"]

        msg['Subject'] = "Thanks For Contacting 64-Bit"
        msg['From'] = '64bit.h.p@gmail.com'
        msg['To'] = cl_email
        msg.set_content(f"""
             We got your Request {cl_name}.
             We will be contacting you shortly. Can we call you at {cl_phone}?
             You told us '{cl_desc}'.
             Thank You...
             """)
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('64bit.h.p@gmail.com', '64Bit@2021')
            smtp.send_message(msg)
            smtp.quit()
            print("Email Sent Successfully")
        return render_template("success.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
