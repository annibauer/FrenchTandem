from rest_framework.decorators import api_view
from rest_framework.response import Response
from dotenv import load_dotenv

from .services.db_management import get_complete_chat_history, get_previous_chat_session
from .services.tandem_chat import tandem_chat

load_dotenv()

# chat with tandem
@api_view(['POST'])
def chat_with_tandem(request):
    chat_history = tandem_chat(request)    
    return Response({"history": list(chat_history)})


# load_all_chat_history
@api_view(['GET'])
def load_all_chat_history(arg):
    chat_history = get_complete_chat_history()
    return Response({"history": list(chat_history)})

# load previous two sessions messages
@api_view(['GET'])
def load_prev_session(arg):
    chat_history = get_previous_chat_session()    
    return Response({"history": list(chat_history)})