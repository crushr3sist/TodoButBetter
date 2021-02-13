from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

    path("createList/", create_list),
    path("List/", view_lists),
    path("", home_app),
    path("deletion/", deleteall, name="deletion"),
    path(r"deleteTask/<int:todo_id>/", deleteTask)


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

