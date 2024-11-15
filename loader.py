from hello_sqla import Base, Message as SQLMessage
from hello import Message, LanguageCode
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import yaml

# Create SQLite database and tables
engine = create_engine('sqlite:///hello.db')
Base.metadata.create_all(engine)

# Load messages from YAML and convert to LinkML objects
with open('messages.yaml') as f:
    data = yaml.safe_load(f)
    messages = [Message(**msg) for msg in data['messages']]

# Insert messages into database
with Session(engine) as session:
    for msg in messages:
        sql_msg = SQLMessage(
            id=str(msg.id),
            text=msg.text,
            language=str(msg.language)  # Convert LanguageCode to string
        )
        session.add(sql_msg)
    session.commit()

# Verify data
with Session(engine) as session:
    stored_messages = session.query(SQLMessage).all()
    print(f"Loaded {len(stored_messages)} messages")
    for msg in stored_messages[:3]:
        print(f"{msg.id}: {msg.language} - {msg.text}")
