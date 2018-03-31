from app import db
from app.models import User, Post

u = User(username='susan', email='susan@ada.com')
db.session.add(u)
db.session.commit()
