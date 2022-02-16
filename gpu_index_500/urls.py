from django.urls import path
from . import views

urlpatterns = [
	path('', views.week_index, name='week_index'),
    path('month', views.month_index, name='month_index'),
    path('year', views.year_index, name='year_index'),
    path('series/<int:series_num>', views.series_courier, name='series'),
    path('specific/<int:stock_num>/<int:year>/<int:month>', views.specific_courier, name='specific'),
    path('visitor', views.visitor_courier, name='visitor'),
]
