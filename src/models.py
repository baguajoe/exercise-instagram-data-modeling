import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(256), nullable=False)

    def to_dict(self):
        return {
            "id": self.id, 
            "username": self.username,
            "email": self.email,
        }
    
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    post_media = Column(String(512), nullable=False)
    post_text = Column(String(512), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    comments = relationship("Comment", backref= "post")
    likes = relationship("PostLike", backref="post")


class PostLike(Base):
    __tablename__ = 'post_like'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1024), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    likes = relationship("CommentLike", backref="comment") 
    dislikes = relationship("CommentDislike", backref="comment") 

class CommentLike(Base):
    __tablename__ = 'comment_like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    comment_id = Column(Integer, ForeignKey("comment.id"))

class CommentDislike(Base):
    __tablename__ = 'comment_dislike'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey("comment.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
