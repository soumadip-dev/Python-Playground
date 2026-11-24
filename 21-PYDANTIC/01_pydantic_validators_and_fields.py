from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
    computed_field,
)


class User(BaseModel):
    # Field: Define validation rules for individual fields
    username: str = Field(
        min_length=4,
        max_length=20,
        description="Username must be between 4 and 20 characters",
        examples=["soumadip_dev"],
    )
    handle: str = Field(
        ...,
        min_length=4,
        max_length=20,
        description="Handle must be between 4 and 20 characters",
        examples=["@soumadip"],
    )
    age: int = Field(
        ...,
        gt=18,
        description="User must be above 18",
        examples=[21],
    )

    password: str
    confirm_pass: str

    # field_validator: Validate a specific field
    @field_validator("username")
    @classmethod
    def username_must_be_lowercase(cls, value):
        if not value.islower():
            raise ValueError("Username must be lowercase")
        return value

    # field_validator: Normalize pattern before validation
    @field_validator("handle", mode="before")
    @classmethod
    def normalize_handle(cls, value):
        cleaned_value = value.strip().lower()
        if not cleaned_value.startswith("@"):
            value = f"@{cleaned_value}"
        return value

    # model_validator: Validate multiple fields together
    @model_validator(mode="after")
    def password_match(self):
        if self.password != self.confirm_pass:
            raise ValueError("Passwords do not match")
        return self

    # computed_field: Calculate a value from existing fields
    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18


# Valid data
user = User(
    username="soumadip",
    handle="  Soumadip_Dev  ",
    age=23,
    password="12345678",
    confirm_pass="12345678",
)

print(user)
print(user.handle)
print(user.is_adult)
