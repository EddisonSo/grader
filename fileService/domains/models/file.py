from sqlalchemy.orm import mapped_column
from domains.models.base import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy import String, DateTime
from uuid import uuid4

class File(Base):
    __tablename__ = "files"
    id = mapped_column(UUID(as_uuid=True),
                            primary_key=True,
                            default=uuid4)
    mapped_name = mapped_column(String(64),
                            nullable=True)
    upload_time = mapped_column(DateTime(timezone=True),
                            server_default=func.now())


    def get_id(self):
        return self.id

    def get_mapped_name(self):
        return self.mapped_name

    def set_mapped_name(self, name):
        self.mapped_name = name

    def get_upload_time(self):
        return self.upload_time
    
