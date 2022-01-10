from flask import Flask, app, render_template, request
import smtplib
from email.message import EmailMessage
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# This is for flask and email integration
app = Flask(__name__)
msg = EmailMessage()
# This is for flask and email integration

# This is the Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Client(db.Model):
#     cl_id = db.Column(db.Integer, primary_key=True, nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     phone = db.Column(db.String(10), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     desc = db.Column(db.String(500))
#     date_contacted = db.Column(db.DateTime,
#                                nullable=False,
#                                default=datetime.utcnow)

#     def __repr__(self):
#         # self.name = name
#         # self.phone = phone
#         # self.email = email
#         # self.desc = desc
#         return f"Client({self.name}, {self.email}, {self.phone})"

# This is the Database


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

        # Adding to the database
        # our_client = Client(cl_name, cl_phone, cl_email, cl_desc)
        # db.session.add(our_client)
        # db.session.commit()
        # print('Added to DB successfully')
        # Adding to the database

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
