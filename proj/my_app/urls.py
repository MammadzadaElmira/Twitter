from django.urls import path
from .import views

urlpatterns = [
    path(
        "", views.index, name="home"
    ),
    path(
        "twit/<int:post_id>",
        views.post_detail_view,
        name="post_details"

    )
]