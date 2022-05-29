from rest_framework.routers import DefaultRouter
from first_rest.views import StudentViewSet, StudentModelViewSet, CollegeModelViewSet


router = DefaultRouter()

# router.register(r'studen-op', StudentViewSet, basename= "student")
router.register(r'studen-op', StudentModelViewSet, basename= "student")
# router.register(r'college-op', CollegeModelViewSet, basename= "college")


