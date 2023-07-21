from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
   path('admin/', admin.site.urls),
   path('',views.home,name="home"),
   path('',views.getPredictions,name="getPredictions"),
   path('',views.classify_image,name="classify_image"),
   #path('',views.class_number_to_name,name="class_number_to_name"),
   #path('',views.load_saved_artifacts,name="load_saved_artifacts"),
   #path('',views.get_cropped_image_if_2_eyes,name=" get_cropped_image_if_2_eyes"),
   #path('',views.get_b64_test_image_for_virat,name="get_b64_test_image_for_virat"),
   #path('',views. get_cv2_image_from_base64_string,name=" get_cv2_image_from_base64_string")
]
