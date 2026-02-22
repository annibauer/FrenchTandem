from ..models import Message
from django.db.models import Max


def save_message(role, user_message, session_id):
    Message.objects.create(role=role, content=user_message, session_id=session_id)
    


def get_messages_current_session(session_id):    
    chat_history = Message.objects.filter(session_id=session_id).order_by('timestamp').values("role", "content", "timestamp", "session_id")
    return chat_history

def get_complete_chat_history():
    chat_history = Message.objects.order_by("timestamp").values("role", "content", "timestamp", "session_id")
    return chat_history

def get_previous_chat_session():
    # Get the latest two session IDs
    latest_session_ids = (
        Message.objects
        .values('session_id')
        .annotate(latest_timestamp=Max('timestamp'))
        .order_by('-latest_timestamp')
    )
    chat_history = []
    # Get the latest two session IDs
    if latest_session_ids:
        session_current = latest_session_ids[0]['session_id']
        session_previous = latest_session_ids[1]['session_id']
        # Fetch chat history for the two sessions
        chat_history_previous_session = Message.objects.filter(session_id=session_previous).order_by('timestamp').values("role", "content", "timestamp", "session_id")
        chat_history_current_session = Message.objects.filter(session_id=session_current).order_by('timestamp').values("role", "content", "timestamp", "session_id")
        chat_history = chat_history_previous_session | chat_history_current_session
        
    return chat_history

