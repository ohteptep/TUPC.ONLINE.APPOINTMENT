from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name = 'landingpage'),
    path('alumni/', views.alumni, name = 'alumni'),
    path('adminlogin/', views.adminlogin, name = 'adminlogin'),
    path('bookappointment/', views.bookappointment, name = 'bookappointment'), 
    path('library/', views.library, name = 'library'),
    path('oaa/', views.oaa, name = 'oaa'),
    path('ocr/', views.ocr, name = 'ocr'),
    path('ogs/', views.ogs, name = 'ogs'),
    path('ohs/', views.ohs, name = 'ohs'),
    path('osa/', views.osa, name = 'osa'),
    path('securitydept/', views.securitydept, name = 'securitydept'),
    path('signupadmin/', views.signupadmin, name = 'signupadmin'),
    path('signupstudent/', views.signupstudent, name = 'signupstudent'),
    path('studentlogin/', views.studentlogin, name = 'studentlogin'),
    path('uitc/', views.uitc, name = 'uitc'),
    path('usg/', views.usg, name = 'usg'),
    path('alumniform/', views.alumniform, name = 'alumniform'),
    path('guardianform/', views.guardianform, name = 'guardianform'),
    path('studentform/', views.studentform, name = 'studentform'),

    path('confirm1/<oaa_id>', views.confirm1, name = 'confirm1'),
    path('denied1/<oaa_id>', views.denied1, name = 'denied1'),
    path('confirm2/<oaa_id>', views.confirm2, name = 'confirm2'),
    path('denied2/<oaa_id>', views.denied2, name = 'denied2'),
    path('confirm3/<oaa_id>', views.confirm3, name = 'confirm3'),
    path('denied3/<oaa_id>', views.denied3, name = 'denied3'),

    path('confirm4/<ocr_id>', views.confirm4, name = 'confirm4'),
    path('denied4/<ocr_id>', views.denied4, name = 'denied4'),
    path('confirm5/<ocr_id>', views.confirm5, name = 'confirm5'),
    path('denied5/<ocr_id>', views.denied5, name = 'denied5'),
    path('confirm6/<ocr_id>', views.confirm6, name = 'confirm6'),
    path('denied6/<ocr_id>', views.denied6, name = 'denied6'),

    path('confirm7/<alumni_id>', views.confirm7, name = 'confirm7'),
    path('denied7/<alumni_id>', views.denied7, name = 'denied7'),
    path('confirm8/<alumni_id>', views.confirm8, name = 'confirm8'),
    path('denied8/<alumni_id>', views.denied8, name = 'denied8'),
    path('confirm9/<alumni_id>', views.confirm9, name = 'confirm9'),
    path('denied9/<alumni_id>', views.denied9, name = 'denied9'),
    
    path('confirm10/<library_id>', views.confirm10, name = 'confirm10'),
    path('denied10/<library_id>', views.denied10, name = 'denied10'),
    path('confirm11/<library_id>', views.confirm11, name = 'confirm11'),
    path('denied11/<library_id>', views.denied11, name = 'denied11'),
    path('confirm12/<library_id>', views.confirm12, name = 'confirm12'),
    path('denied12/<library_id>', views.denied12, name = 'denied12'),

    path('confirm13/<ogs_id>', views.confirm13, name = 'confirm13'),
    path('denied13/<ogs_id>', views.denied13, name = 'denied13'),
    path('confirm14/<ogs_id>', views.confirm14, name = 'confirm14'),
    path('denied14/<ogs_id>', views.denied14, name = 'denied14'),
    path('confirm15/<ogs_id>', views.confirm15, name = 'confirm15'),
    path('denied15/<ogs_id>', views.denied15, name = 'denied15'),

    path('confirm16/<ohs_id>', views.confirm16, name = 'confirm16'),
    path('denied16/<ohs_id>', views.denied16, name = 'denied16'),
    path('confirm17/<ohs_id>', views.confirm17, name = 'confirm17'),
    path('denied17/<ohs_id>', views.denied17, name = 'denied17'),
    path('confirm18/<ohs_id>', views.confirm18, name = 'confirm18'),
    path('denied18/<ohs_id>', views.denied18, name = 'denied18'),

    path('confirm19/<osa_id>', views.confirm19, name = 'confirm19'),
    path('denied19/<osa_id>', views.denied19, name = 'denied19'),
    path('confirm20/<osa_id>', views.confirm20, name = 'confirm20'),
    path('denied20/<osa_id>', views.denied20, name = 'denied20'),
    path('confirm21/<osa_id>', views.confirm21, name = 'confirm21'),
    path('denied21/<osa_id>', views.denied21, name = 'denied21'),

    path('confirm22/<uitc_id>', views.confirm22, name = 'confirm22'),
    path('denied22/<uitc_id>', views.denied22, name = 'denied22'),
    path('confirm23/<uitc_id>', views.confirm23, name = 'confirm23'),
    path('denied23/<uitc_id>', views.denied23, name = 'denied23'),
    path('confirm24/<uitc_id>', views.confirm24, name = 'confirm24'),
    path('denied24/<uitc_id>', views.denied24, name = 'denied24'),

    path('confirm25/<usg_id>', views.confirm25, name = 'confirm25'),
    path('denied25/<usg_id>', views.denied25, name = 'denied25'),
    path('confirm26/<usg_id>', views.confirm26, name = 'confirm26'),
    path('denied26/<usg_id>', views.denied26, name = 'denied26'),
    path('confirm27/<usg_id>', views.confirm27, name = 'confirm27'),
    path('denied27/<usg_id>', views.denied27, name = 'denied27'),


    path('delete1/<sec_id>', views.delete1, name = 'delete1'),
    path('delete2/<sec_id>', views.delete2, name = 'delete2'),
    path('delete3/<sec_id>', views.delete3, name = 'delete3'),

    path('refresh/', views.refresh, name = 'refresh'),
    path('logout/', views.logoutuser, name = 'logout'),
    path('logoutwa/', views.logoutuserwa, name = 'logoutwa'),

    path('viewing1/<oaa_id>', views.viewing1, name = 'viewing1'),
    path('viewing2/<oaa_id>', views.viewing2, name = 'viewing2'),
    path('viewing3/<oaa_id>', views.viewing3, name = 'viewing3'),

    path('cssform/', views.cssform, name = 'cssform'),

    path('finish/', views.finish, name = 'finish'),
    path('PDFile/', views.PDFile, name = 'PDFile'),
    path('Back/', views.Back, name = 'Back'),

]