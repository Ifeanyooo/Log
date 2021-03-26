from flask import Flask, render_template

from wtform_fields import *
from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'


app.config['SQLALCHEMY_DATABASE_URI']='postgres://odswxbnnicpepx:b9ee959f6e603d9dc12f40dc672738bb4633eee26f340de81d0e4af1519c607e@ec2-35-171-57-132.compute-1.amazonaws.com:5432/d6hhutq5eg5jlm'

db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def index():

   reg_form = RegistrationForm()

   if reg_form.validate_on_submit():
   	   username = reg_form.username.data
   	   password = reg_form.password.data


   	   user_object = User.query.filter_by(username=username).first()
   	   if user_object:
   	   	    return "Someone else has taken this username!"

   	   	# Add user to db
   	   user = User(username=username, password=password)
   	   db.session.add(user)
   	   db.session.commit()
   	   return "Inserted into DB!"

   	
   return render_template("index.html", form=reg_form)


if __name__ == "__main__":
	app.run(debug=True)