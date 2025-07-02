from main import app, database
from models import User, Post

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     user = User(username = "Caio", email="caio@caio.com", password="123456")
#     user2 = User(username = "Jao", email="Jao@jao.com", password="123456")

#     database.session.add(user)
#     database.session.add(user2)

#     database.session.commit()

# with app.app_context():
#     user_test = User.query.filter_by(id=1).first()
#     print(user_test.email)

# with app.app_context():
#     my_post = Post(id_user = 1, title = "First", body = "Contents")
#     database.session.add(my_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.author.email)

with app.app_context():
    database.drop_all()
    database.create_all()