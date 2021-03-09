from fullstack_backend.extensions import db


class PostCategory(db.Model):
    """Association table for mapping posts to categories and vice versa"""

    __tablename__ = "post_categories"
    __table_args__ = (
        db.UniqueConstraint("post_id", "category_id", name="_post_category_uix"),
    )

    """Columns"""
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    category_id = db.Column(
        db.Integer, db.ForeignKey("categories.id"), primary_key=True
    )

    """Relationships"""
    # Parent
    post = db.relationship("Post", back_populates="_post_categories")
    # Child
    category = db.relationship("Category", back_populates="posts", lazy="joined")

    def __init__(self, category=None, post=None):
        self.category = category
        self.post = post

    def __repr__(self):
        return f"<PostCategory - Post {self.post_id}/Category {self.category_id}>"
