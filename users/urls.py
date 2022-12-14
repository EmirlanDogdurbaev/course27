from django.urls import path
from users.views import home, profile, RegisterView, detail, View_create_note, View_delete_note, View_update_note,View_user_notes

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('<int:book_id>/', detail, name='detail'),
    path('notes/', View_user_notes.as_view(), name='notes'),
    path('notes/<int:id>/update_note/', View_update_note.as_view(), name='update'),
    path('notes/<int:id>/delete_note/', View_delete_note.as_view(), name='delete'),
    path('notes/add_note/', View_create_note.as_view(), name='add'),
]
