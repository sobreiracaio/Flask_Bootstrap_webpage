from community_site import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user (user_id):
    return User.query.get(int(user_id))


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String, nullable = False)
    email = database.Column(database.String, nullable = False, unique = True)
    password = database.Column(database.String, nullable = False)
    profile_photo = database.Column(database.String, default = "default.jpg")
    posts = database.relationship('Post', backref = "author", lazy = True)
    courses = database.Column(database.String, nullable = False, default = "Not informed")
    
    def count_posts(self):
        return len(self.posts)
    
    
class Post(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    title = database.Column(database.String, nullable = False)
    body = database.Column(database.Text, nullable = False)
    creation_date = database.Column(database.DateTime, nullable = False, default = datetime.now)
    id_user = database.Column(database.Integer, database.ForeignKey('user.id'), nullable = False)