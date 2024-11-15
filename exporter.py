from hello_sqla import Base, Message as SQLMessage
from hello import Message, LanguageCode
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import yaml

# Connect to SQLite database 
engine = create_engine('sqlite:///hello.db')

# Export messages from database
messages = []
with Session(engine) as session:
    sql_messages = session.query(SQLMessage).all()
    for sql_msg in sql_messages:
        msg = Message(
            id=sql_msg.id,
            text=sql_msg.text,
            language=LanguageCode(sql_msg.language)
        )
        messages.append(msg)

# Convert messages to dicts
data = {'messages': [
    {
        'id': msg.id,
        'text': msg.text,
        'language': str(msg.language)
    } for msg in messages
]}

# Write to YAML file
with open('exported_messages.yaml', 'w', encoding='utf-8') as f:
    yaml.safe_dump(data, f, allow_unicode=True)

print(f"Exported {len(messages)} messages to exported_messages.yaml")