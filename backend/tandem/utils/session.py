import uuid

def get_session_id(request):
    # get session ID
    session_id = request.session.get('chat_session_id')
    if not session_id:
        # Fallback, in case something goes wrong
        session_id = uuid.uuid4()
        request.session['chat_session_id'] = str(session_id)
        
    return session_id