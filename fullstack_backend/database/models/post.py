from sqlalchemy.ext.associationproxy import association_proxy

from fullstack_backend.extensions import db

from ..mixins import (
    Column,
    PaginatedAPIMixin,
    PkModel,
    SerializableMixin,
    TimestampMixin,
    reference_col,
    relationship,
)


class Post(PkModel, TimestampMixin, SerializableMixin, PaginatedAPIMixin):
    """Model for blog posts"""

    __tablename__ = "posts"

    """Columns"""
    # id
    # time_created
    # time_updated
    content = Column(db.Text)

    """Relationships"""
    _post_categories = relationship(
        "PostCategory", back_populates="post", cascade="all, delete-orphan"
    )
    categories = association_proxy("_post_categories", "category")

    def __repr__(self):
        return f"<Post #{self.id} - created {self.time_created}>"
