"""
* __________________
* 
* [2016] - [2017] CaseCrunch Systems Ltd
* All Rights Reserved.
* 
* NOTICE:  All information contained herein is, and remains
* the property of CaseCrunch Systems Ltd and its suppliers,
* if any.  The intellectual and technical concepts contained
* herein are proprietary to CaseCrunch Systems Ltd
* and its suppliers and may be covered by U.S. and Foreign Patents,
* patents in process, and are protected by trade secret or copyright law.
* Dissemination of this information or reproduction of this material
* is strictly forbidden unless prior written permission is obtained
* from CaseCrunch Systems Ltd.
"""

# imports various libraries

from flask import Flask, render_template, request
from flask import send_from_directory

# defines variables and connects with postgresql db on heroku

app=Flask(__name__)


# defines database structure

# app routes

@app.route("/",methods=["GET", "POST"])
def index():

	if request.method == 'POST':

		print("Post request going through")
		name = request.form['name']
		email = request.form['email']
		subject = request.form['subject']
		message = request.form['message']
		print("Items: ",name,email,subject,message)
		insert_answer(name,email,subject,message)
		return render_template("index_submission.html")

	if request.method == 'GET':

		print("Get request going through")
		return render_template("index.html")

@app.route("/terms",methods=["GET"])
def terms():

	return render_template("terms.html")



if __name__ == '__main__':
	app.debug=True
	app.run(port=5599)


