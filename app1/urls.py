from django.urls import path
from . import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

# from .views import portfolio, blur_image_view, image_view, check_password_image, blur_image_view_01, image_view_01, blur_image_view_02, image_view_02, blur_image_view_03, image_view_03
from .views import projects, blur_image_view, image_view, check_password_image, blur_image_view_01, image_view_01, blur_image_view_02, image_view_02, blur_image_view_03, image_view_03, getApiprojectDetails
 
urlpatterns = [
    path(
        "check-password-image/<str:password>/", check_password_image, name="projects"
    ),
    path('api/getdetails/<str:data>/<str:idx>/', getApiprojectDetails, name="Api Details"),
    path("projects/<str:password>/", projects, name="projects"),
    path("projects/", projects, name="projects"),
    path("blur-image-view/<int:image_id>/", blur_image_view, name="blur_image_view"),
    path("image-view/<str:password>/<int:image_id>/", image_view, name="image_view"),
    # ------------
    path("blur-image-view-01/<int:image_id>/", blur_image_view_01, name="blur_image_view_01"),
    path("image-view-01/<str:password>/<int:image_id>/", image_view_01, name="image_view_01"),
    # -------------
    path("blur-image-view-02/<int:image_id>/", blur_image_view_02, name="blur_image_view_02"),
    path("image-view-02/<str:password>/<int:image_id>/", image_view_02, name="image_view_02"),
    # -------------
    path("blur-image-view-03/<int:image_id>/", blur_image_view_03, name="blur_image_view_03"),
    path("image-view-03/<str:password>/<int:image_id>/", image_view_03, name="image_view_03"),

]


if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

