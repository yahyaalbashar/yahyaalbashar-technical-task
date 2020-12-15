from django.urls import path
from .views import( 
                    AddToFavView,
                    FavoriteDigimonListView,
                    DigimonDetailView,
                    DeleteDigimonView
                    )

urlpatterns = [
    path("add-digimon-to-fav",AddToFavView.as_view(),name="add_digimon_to_fav"),
    path("digimon-fav-list",FavoriteDigimonListView.as_view(),name="digimon_fav_list"),
    path("<slug>",DigimonDetailView.as_view(),name="digimon_detail"),
    path("delete/",DeleteDigimonView.as_view(),name="delete_digimon"),

]
