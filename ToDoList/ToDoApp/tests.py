from django.test import TestCase
from django.contrib auth.models.User
from django.urls import reverse
from models import ListType
import datetime
from .forms import NewListForm


class ListTypeTest(TestCase):
   #set up one time sample data
  class ListTypeTest(TestCase):
    def test_string(self):
       type=ListType(listtitle=Shopping)
       self.assertEqual(str(ListType), type.listtitle)

    def test_string(self):
       type=ListType(listcreatedate= datetime.date (2019,6.10)
       self.assertEqual(str(ListType), type.listcreatedate)

    def test_string(self):
       type=ListType(listcreatetime= datetime.time (12,15)
       self.assertEqual(str(ListType), type.listcreatetime)

    def test_string(self):
       type=ListType(listitem= 'toothpaste')
       self.assertEqual(str(ListType), type.listitem)

    def test_string(self):
       type=ListType(listduedate= datetime.date(2019,6,11)
       self.assertEqual(str(ListType), type.listduedate)

    def test_string(self):
       type=ListType(listduetime= datetime.time (15,00)
       self.assertEqual(str(ListType), type.listduetime)

    def test_string(self):
       type=ListType(listpriority='urgent')
       self.assertEqual(str(ListType), type.listpriority)

class NewListFormTest(TestCase):
    def setUp(self):
        self.user2=User.objects.create(username='user1', password='P@ssw0rd1')
        self.type2=TechType.objects.create(listtitle= Saturday)
    
    def test_NewListForm (self):
        data={
            'listcreatedate' : datetime.date(2019,6,28),
            'listcreatetime' : datetime.time(12,15),
            'listpriority' : Urgent,
         
        }
        form = NewListForm(data=data)
        self.assertTrue(form.is_valid)

    def test_NewListForm Invalid(self):
        data={
            'listcreatedate' : datetime.date(2019,6,28),
            'listcreatetime' : datetime.time(12,15),
            'listpriority' : Urgent,
        }
        form = NewListForm (data=data)
        self.assertFalse(form.is_valid())    

   
   
   
   
        