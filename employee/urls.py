
from django.urls import path,include
from employee.views import EmployeeViewSet, DepartmentViewSet, RoleViewSet
from rest_framework.routers import DefaultRouter
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

router = DefaultRouter()

router.register(r'employee', EmployeeViewSet, basename='employee')
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'role', RoleViewSet, basename='role')



urlpatterns = [
    path('', include(router.urls)),  # handles /api/employee/
    # path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

