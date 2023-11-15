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

# **GET */ :*** Redirect to list of users. (We’ll fix this in a later step).

# **GET */users :*** Show all users. Make these links to view the detail page for the user. Have a link here to the add-user form.

# **GET */users/new :*** Show an add form for users

# **POST */users/new :*** Process the add form, adding a new user and going back to ***/users***

# **GET */users/[user-id] :***Show information about the given user. Have a button to get to their edit page, and to delete the user.

# **GET */users/[user-id]/edit :*** Show the edit page for a user. Have a cancel button that returns to the detail page for a user, and a save button that updates the user.

# **POST */users/[user-id]/edit :***Process the edit form, returning the user to the ***/users*** page.

# **POST */users/[user-id]/delete :*** Delete the user.

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
    users = User.query.all()
    return render_template("user-list.html", users=users)

# Viewing a user's detail page
@app.route('/users/<user_id>')
def user_detail(user_id):
    """Profile page for individual user"""
    user = User.query.get(user_id)
    return render_template("profile.html", user=user)

# Editing user info
@app.route('/users/<user_id>/edit')
def user_edit(user_id):
    """A form for editing a user profile"""
    user = User.query.get(user_id)
    return render_template("user-update.html", user=user)

# Posting updated user info
@app.route('/users/<user_id>/edit', methods=["POST"])
def user_update(user_id):
    """Handling user update form submission"""
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    image_url = request.form["image-url"]
    user = User.query.get(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url
    db.session.add(user)
    db.session.commit()
    return render_template("/users/{user.id}")


# Creating a new user
@app.route('/users/new')
def register_form():
    """A form for registering a new user"""
    return render_template("register.html")

# Creating a new user
@app.route('/users/new', methods=["POST"])
def create_user():
    """Handling user registration form submission"""
    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    image_url = request.form["image-url"]
    new_user = User(first_name=first_name, last_name=last_name)
    # add case where image url is provided
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"/users/{new_user.id}")