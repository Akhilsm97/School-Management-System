
from django.conf.urls import url
from stgcs_admin import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('add_teachers/', views.add_teachers, name="add_teachers"),
    path('login/', views.login, name="login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('non_teaching/', views.non_teaching, name="non_teaching"),
    path('add_student/', views.add_student, name="add_student"),
    path('admins/', views.admins, name="admins"),
    path('student_profile/', views.student_profile, name="student_profile"),

    # Admin

    path('student_details_1/', views.student_details_1, name="student_details_1"),
    path('upper_primary/<str:departments>', views.upper, name="upper"),
    path('lower_primary/<str:departments>', views.lower, name="lower_primary"),
    path('secondary/<str:departments>', views.sec, name="secondary"),
    path('higher_secondary/<str:departments>', views.higher, name="higher_secondary"),

    path('higher_secondarys/<int:id>', views.higher_sec, name="higher_sec"),
    path('lower_pri/<int:id>', views.lower_pri, name="lower_pri"),
    path('upper_pri/<int:id>', views.upper_pri, name="upper_pri"),
    path('secondarys/<int:id>', views.secondarys, name="secondarys"),
    path('teacher_department/', views.teacher_department, name="teacher_department"),
    path('seat_lower_primary/', views.seat_lower_primary, name="seat_lower_primary"),
    path('seat_upper_primary/', views.seat_upper_primary, name="seat_upper_primary"),
    path('seat_secondary/', views.seat_secondary, name="seat_secondary"),
    path('seat_higher_secondary/', views.seat_higher_secondary, name="seat_higher_secondary"),
    path('allot_class/', views.allot_class, name="allot_class"),
    path('allot_class_details/<int:id>/<str:username>/<str:department>', views.allot_class_details, name="allot_class_details"),
    path('allot_subject/', views.allot_subject, name="allot_subject"),
    path('subject_allocat/<str:username>/<str:department>', views.subject_allocat, name="subject_allocat"),



     #Teachers

    path('teacher_profile/', views.teacher_profile, name="teacher_profile"),
    path('add_teacherss/', views.add_teacherss, name="add_teacherss"),
    path('teacher_view/<int:id>', views.teacher_view, name="teacher_view"),
    path('approved_teacher_view/', views.approved_teacher_view, name="approved_teacher_view"),
    path('approved_teacher/<str:username>', views.approved_teacher, name="approved_teacher"),
    path('teacher_full_details/<str:username>', views.teacher_full_details, name="teacher_full_details"),
    path('teacher_profileview/<str:username>', views.teacher_profileview, name="teacher_profileview"),
    path('verify_stud/<str:username>', views.verify_stud, name="verify_stud"),
    path('verify_stud_details/<str:username>/<str:teacher_name>', views.verify_stud_details, name="verify_stud_details"),
    path('students/<str:username>', views.students, name="students"),
    path('stud_full_details/<str:username>', views.stud_full_details, name="stud_full_details"),
    path('update_teacher_profile/<str:username>', views.update_teacher_profile, name="update_teacher_profile"),
    path('stud_attendence/<str:username>', views.stud_attendence, name="stud_attendence"),
    path('student_attendence/<str:username>/<str:reg_no>', views.student_attendence, name="student_attendence"),
    path('attendence/', views.attendence, name="attendence"),
    path('attendance_mark/<str:username>/<str:reg_no>/<str:dates>', views.attendance_mark, name="attendance_mark"),
    path('attendance_record/', views.attendance_record, name="attendance_record"),
    path('mark_upload/<str:username>', views.mark_upload, name="mark_upload"),
    path('upload_mark/<str:username>/<str:reg_no>', views.upload_mark, name="upload_mark"),
    path('mark_details/', views.mark_details, name="mark_details"),
    path('mark_edit/<str:username>/<str:reg_no>/<str:exam>', views.mark_edit, name="mark_edit"),
    path('class_fac/', views.class_fac, name="class_fac"),
    path('faculty_corner/', views.faculty_corner, name="faculty_corner"),
    path('class_announcement/<str:teacher_name>/<str:class_name>/', views.class_announcement, name="class_announcement"),
    path('announcement_delete/<int:id>/<str:teacher_name>/<str:class_name>/', views.announcement_delete, name="announcement_delete"),
    path('announcement_edit/<int:id>/<str:teacher_name>/<str:class_name>/', views.announcement_edit,name="announcement_edit"),
    path('faculaty_profile/', views.faculaty_profile ,name="faculaty_profile"),
    path('faculaty_dashboard/<str:teacher_name>', views.faculaty_dashboard, name="faculaty_dashboard"),
    path('add_portion/', views.add_portion, name="add_portion"),
    path('edit_portion/<int:id>', views.edit_portion, name="edit_portion"),
    path('class_announcement/<str:teacher_name>/<str:class_name>/', views.class_announcement, name="class_announcement"),
    path('announcement_delete/<int:id>/<str:teacher_name>/<str:class_name>/', views.announcement_delete, name="announcement_delete"),
    path('faculty_msg/<str:teacher_name>/<str:cls_teacher_name>/<str:cls>', views.faculty_msg, name="faculty_msg"),
    path('faculaty_alloted_cls/', views.faculaty_alloted_cls, name="faculaty_alloted_cls"),
    path('alloted_dashboard/<int:id>/<str:teacher_name>/<str:cls>', views.alloted_dashboard, name="alloted_dashboard"),



    #Manager

    path('manager_dashborad/', views.manager_dashborad, name="manager_dashborad"),
    path('manage_teacher_view/', views.manage_teacher_view, name="teacher_approve"),
    path('teacher_approve/<int:id>', views.teacher_approve, name="teacher_approve"),
    path('manager_approve_teachers/<int:id>', views.manager_approve_teachers, name="manager_approve_teachers"),

    path('testing/', views.testing, name="testing"),
    path('testing_2/', views.testing_2, name="testing_2"),



]