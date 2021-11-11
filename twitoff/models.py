from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a DB object
DB = SQLAlchemy()

# Make a User table by creating a User class
class User(DB.Model):
    '''Creates a User table with SQLAlchemy'''
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True)

    # username column
    username = DB.Column(DB.String, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    
    def __repr__(self):
        return "<User: {}>".format(self.username)


# Make a Tweet table by creating a Tweet class
class Tweet(DB.Model):
    '''Creates a User table with SQLAlchemy'''
    # id column
    id = DB.Column(DB.BigInteger, primary_key=True)

    # text column. Unicode holds text, emojis, and links
    text = DB.Column(DB.Unicode(300), nullable=False)

    # Create a relationship between a tweet and a user
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)

    # Finalizing the relationship making sure it goes both ways. 
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))
    # Include a word embedding on a tweet
    vect = DB.Column(DB.PickleType, nullable=False)
    
    def __repr__(self):
        return "<Tweet: {}>".format(self.text)