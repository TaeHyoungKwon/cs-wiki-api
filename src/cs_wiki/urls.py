from django.urls import path, include

from cs_wiki.views import CategoryListView, NoteListView, AllPageCountView, IssueListView, AllPageListView, PageDetailView

urlpatterns = [
    path("mock-category-list", CategoryListView.as_view()),
    path("notes/", NoteListView.as_view()),
    path("all_page_count/", AllPageCountView.as_view()),
    path("issues/", IssueListView.as_view()),
    path("page/<int:page_id>", PageDetailView.as_view()),
]
