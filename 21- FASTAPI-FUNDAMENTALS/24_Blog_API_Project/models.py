from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# Database model for blog posts
class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
