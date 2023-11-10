from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
# from models import db, connect_db
from models import db, connect_db, User

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


@app.route('/')
def root():
    """Homepage redirects to list of users."""
    return redirect("/users")

# Viewing a user's detail page
@app.route('/users')
def user_listing():
    """List of registered users."""
    return render_template("user-list.html")

# Viewing a user's detail page
@app.route('/user-detail/<user_id>')
def user_detail(user_id):
    """Profile page for individual user"""
    return render_template("profile.html", user_id=user_id)

# Editing user info
@app.route('/user-update/<user_id>')
def user_edit(user_id):
    """A form for editing a user profile"""
    return render_template("user-update.html", user_id=user_id)

# Creating a new user
@app.route('/register')
def new_user():
    """A form for registering a new user"""
    return render_template("register.html")
