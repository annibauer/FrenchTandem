from rest_framework.response import Response
from .openai_api import openai_request
from .db_management import get_messages_current_session
from .text_analysis import analyze_reply
from ..utils.session import get_session_id

def tandem_chat(request):
    session_id = get_session_id(request)
    user_message = request.data.get('message', '')
    
    if not user_message:
        return Response({"error": "No message provided"}, status=400)
    
    try:
        reply = openai_request(user_message)
        analyze_reply(reply, user_message, session_id)
        chat_history = get_messages_current_session(session_id)
         

    except Exception as e:
        chat_history = []
        
    return chat_history