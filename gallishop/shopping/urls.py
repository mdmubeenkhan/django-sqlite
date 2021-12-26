from django.urls import path
from shopping.views import DisplayDetailsView, HomeView, AddItemsView, DisplayItemsView, DisplayItemListView, ItemsUpdateView, DeleteItemsView

urlpatterns = [
    path('home/', HomeView.as_view()),
    path('additems/', AddItemsView.as_view()),
    path('displayitems/', DisplayItemsView.as_view(), name='details'),
    path('listitems/', DisplayItemListView.as_view()),
    path('detail/<pk>', DisplayDetailsView.as_view()),
    path('update/<pk>', ItemsUpdateView.as_view()),
    path('delete/<pk>', DeleteItemsView.as_view(), name='details'),

]