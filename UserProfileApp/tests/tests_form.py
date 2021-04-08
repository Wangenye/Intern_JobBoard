# from django.test import TestCase
# from UserProfileApp.forms import CompanyDetailForm


# class FormTests(TestCase):

#     def  test_customerorder_form(self):
#         form = CompanyDetailForm(data={
#             'company_name':"Username",
#             'company_ceo':"10hgjh00",
#             'company_about': "Ttyuty01",
#             'company_email':"a@gmail.com",
#             'company_tel':"2541234567890",
#             'company_website':"https://www.google.com",
#             'company_location':"https://www.google.com",
#             'company_country':"Kenya",
#             'company_city':"Matuu",
#         })
#         self.assertTrue(form.is_valid())

#     def  test_customerorder_no_form(self):
#         form = CompanyDetailForm(data={})
#         self.assertEquals(len(form.errors),9)