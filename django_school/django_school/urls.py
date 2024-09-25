from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from classroom.views import classroom, students, teachers
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', include('classroom.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('logout/', LogoutView.as_view(next_page='signup'), name='logout'),
]
