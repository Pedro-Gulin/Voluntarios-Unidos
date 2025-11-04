from flask import Blueprint, request, render_template, redirect, url_for, flash
from models.user.users import Users
from models.user.roles import Role
from models import db

user = Blueprint("user", __name__, template_folder="views")

@user.route('/register_user')
def register_user():
    roles = Role.get_role()
    return render_template("register_user.html", roles=roles)

@user.route('/add_user', methods=['POST'])
def add_user():
    global users 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role_name = request.form['role_type_']
        
        Users.save_user(email, password, role_name)
        return render_template("home.html")
    
@user.route('/edit_user')
def edit_user():
    email = request.args.get('email')
    user = Users.get_single_user(email)
    roles = Role.get_role()

    return render_template("update_user.html", user=user, roles=roles)

@user.route('/updt_user', methods=['POST'])
def updt_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role_name = request.form['role']

        user = Users.get_single_user(email)
        role = Role.get_single_role(role_name)

        user.password = password
        user.role_id = role.id

        db.session.commit()
        return redirect("users")

#@user.route('/del_user')
#def del_user():
    #email = request.args.get('email')
    #user = Users.get_single_user(email)
    
    #return render_template("remove_user.html", user=user)

@user.route('/del_user', methods=['GET'])
def del_user():
    email = request.args.get("email")

    user = Users.get_single_user(email)
    role = Role.get_role()

    if user:
        if user.role.name == "Admin":
            flash("O usuario eh um admin, nao da pra remover")
        else:
            db.session.delete(user)
            db.session.commit()

    return redirect("/users")