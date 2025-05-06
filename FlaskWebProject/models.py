from datetime import datetime
from FlaskWebProject import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'USERS'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    __tablename__ = 'POSTS'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    body = db.Column(db.String(800), nullable=False)
    author = db.Column(db.String(75), nullable=False)
    image_path = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('USERS.id'), nullable=False)

    def __repr__(self):
        # return f'<Post {self.title}>'
        return '<Post {}>'.format(self.body)

    def save_changes(self, form, file, userId, new=False):
        self.title = form.title.data
        self.author = form.author.data
        self.body = form.body.data
        self.user_id = userId

        if file:
            filename = secure_filename(file.filename);
            fileextension = filename.rsplit('.',1)[1];
            Randomfilename = id_generator();
            filename = Randomfilename + '.' + fileextension;
            try:
                # blob_container_client.upload_blob(name=filename, data=file, overwrite=True)
                blob_service.create_blob_from_stream(blob_container, filename, file)
                if(self.image_path):
                    # blob_container_client.delete_blob(self.image_path)
                    blob_service.delete_blob(blob_container, self.image_path)
            except Exception:
                flash(Exception)
            self.image_path =  filename
        if new:
            db.session.add(self)
        db.session.commit()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
