from flask import Blueprint, request, render_template, redirect, url_for
from models.user.roles import Role

role_ = Blueprint("role_", __name__, template_folder="views")