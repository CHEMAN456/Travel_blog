from django.test import TestCase,Client
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class UserLoginViewTest(TestCase):
    
    def setUp(self):
        # Create a Test User
        
        self.username = 'testuser'
        self.password = 'testpass123'
        self.user = User.objects.create_user(username=self.username,password=self.password)
        self.client = Client()
        self.login_url = reverse('login')
        
    def test_login_valid_credentials(self):
        
        response = self.client.post(self.login_url,
           {'username':self.username,
            'password':self.password
            } 
        )
        
        self.assertEqual(response.status_code,302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)    
    
    def test_login_with_invalid_credentials(self):
        
        response = self.client.post(self.login_url,
           {'username':self.username,
            'password':'wrongpassword'
            } 
        )
        
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Invalid User, Try Again')
        self.assertFalse(response.wsgi_request.user.is_authenticated)     
        
