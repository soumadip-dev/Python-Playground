from typing import List, Optional
from pydantic import BaseModel


# Recursive Model: A model that references itself
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None


# Resolve the forward reference
Comment.model_rebuild()


# Create a comment with nested replies
comment = Comment(
    id=1,
    content="Anyone knows a good Python course?",
    replies=[
        Comment(
            id=2,
            content="Try the freeCodeCamp Python course.",
            replies=[Comment(id=3, content="Thanks! I'll check it out.")],
        ),
        Comment(id=4, content="I recommend Corey Schafer's tutorials."),
    ],
)

# Convert the model into a dictionary
print(comment.model_dump())
