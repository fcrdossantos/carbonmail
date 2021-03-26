from carbonmail import list_editor, email_sender
from carbonmail.database.initialize import initialize as initialize_db
from carbonmail.email_sender.manager import initialize as initialize_sender

initialize_db()
initialize_sender()
