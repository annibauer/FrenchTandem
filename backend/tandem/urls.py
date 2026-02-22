from django.urls import path
from .views import chat_with_tandem, load_all_chat_history, load_prev_session

urlpatterns = [
    path('chat/', chat_with_tandem),
    path("load_sessions/", load_all_chat_history),
    path("load_previous_sessions/", load_prev_session)
]
