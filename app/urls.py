from django.urls import path
from .views import index_func, BalanceList, DetailBalance, balance_edit, FrontedAppView

app_name = 'app'
urlpatterns = [
    path('', view=FrontedAppView.as_view(), name='index'),
    path('list/', view = BalanceList.as_view(), name='balance_list'),
    path('<int:pk>/', view = DetailBalance.as_view(), name='balance_detail'),
    path('add/', view = balance_edit, name='balance_add'),
    path('edit/<int:balance_id>/', view = balance_edit, name='balance_edit')
]
