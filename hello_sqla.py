
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Message(Base):
    """
    
    """
    __tablename__ = 'Message'

    id = Column(Text(), primary_key=True, nullable=False )
    text = Column(Text(), nullable=False )
    language = Column(Enum('ar', 'bn', 'zh', 'cs', 'da', 'nl', 'en', 'fi', 'fr', 'de', 'el', 'hi', 'hu', 'id', 'ga', 'it', 'ja', 'ko', 'fa', 'pl', 'pt', 'ru', 'es', 'sv', 'th', 'tr', 'uk', 'vi', name='LanguageCode'))
    

    def __repr__(self):
        return f"Message(id={self.id},text={self.text},language={self.language},)"



    


