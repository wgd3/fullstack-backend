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


class Category(PkModel, SerializableMixin, PaginatedAPIMixin):
    """Model for categories which group posts together"""

    __tablename__ = "categories"

    """Columns"""
    # id
    # time_created
    # time_updated
    name = Column(db.String, unique=True, nullable=False)

    posts = relationship(
        "PostCategory", back_populates="category", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category {self.name}>"
